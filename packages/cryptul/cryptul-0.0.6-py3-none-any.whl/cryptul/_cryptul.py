import math
import random
from string import printable

from Crypto.Util.number import GCD, bytes_to_long, inverse, isPrime
from Crypto.Util.Padding import pad
from sympy import Mod, integer_nthroot, sqrt
from sympy.ntheory import factorint
from factordb.factordb import FactorDB
from sympy.ntheory import discrete_log as dlog

# Remember:
# from Crypto.Util.number import long_to_bytes
# import hashlib
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# from sympy.ntheory.modular import crt
# from Crypto.Util.number import inverse
# Add: Mersenne Twister solver, integer n-th root, modular n-th root

# CyberChallenge
CCIT_FLAG_CHARS = [c for c in printable if c.isalnum()] + ["_", "{", "}"]

# pwntools

# def send(data: bytes):
#     r.sendlineafter(b"> ", data)


# def choose(selection: bytes):
#     if selection in [b"0", b"1", b"2"]:
#         send(selection)
#     else:
#         raise ValueError("Invalid Choice")

# Bits operations


def xor(a: bytes, b: bytes, strict: bool = True) -> bytes:
    if strict and len(a) != len(b):
        raise ValueError(
            "When strict=True you can't xor two bytes variables with different lengths"
        )

    if len(a) < len(b):
        c = a
        a = b
        b = c

    # Now we have that len(a) >= len(b)

    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i % len(b)])
    result = bytes(result)

    return result


def flip(to_flip: bytes, initial_value: bytes, final_value: bytes) -> bytes:
    """
    We know that:
    to_flip XOR message = initial_value

    We want find flipped such that
    flipped XOR message = final_value

    Go like this:
    to_flip XOR message = initial_value <=>
    message = to_flip XOR initial_value

    flipped XOR message = final_value <=>
    flipped = final_value XOR message
    """
    assert (
        len(to_flip) == len(initial_value) == len(final_value)
    ), "All lengths must be the same"

    message = xor(to_flip, initial_value)
    flipped = xor(message, final_value)

    return flipped


# Block ciphers


def split_in_blocks(message: bytes, block_length: int):
    number_of_full_blocks = len(message) // block_length

    blocks = [
        message[i * block_length: (i + 1) * block_length]
        for i in range(number_of_full_blocks)
    ]

    if len(message) % block_length != 0:
        blocks.append(pad(message[number_of_full_blocks + 1:], block_length))

    return blocks


# Stream ciphers

# CBC mode


class CBCCracker:
    def __init__(
        self,
        encrypt,
        decrypt,
        block_size: int,
    ):
        self.encrypt = encrypt
        self.decrypt = decrypt
        self.block_size = block_size

        """
        encrypt: Function that returns the ciphertext given the plaintext
        decrypt: Function that returns the plaintext given the ciphertext
        """

    # to_flip: bytes, initial_value: bytes, final_value: bytes

    def flip_iv(self, ct: bytes, final_pt: bytes, iv_to_flip: bytes = None):
        assert (
            len(ct) == self.block_size
        ), f"The ciphertext must have the same length of the block ({self.block_size} bytes)"

        if iv_to_flip == None:
            iv_to_flip = b"A" * self.block_size

        initial_pt = self.decrypt(ct, iv_to_flip)

        iv_flipped = flip(iv_to_flip, initial_pt, final_pt)

        return iv_flipped

    def crack_fixed_iv_with_decrypt(self, final_pt: bytes):
        """
        Returns a ciphertext and an IV that, when decrypted, becames the plaintext final_pt.
        You need to use the decryption function
        """

        final_pt = pad(final_pt, self.block_size)

        final_pt_blocks = split_in_blocks(final_pt, self.block_size)[::-1]

        # iterate on the blocks in reverse order
        final_ct_blocks = [b"A" * self.block_size]
        i = 0
        while i < len(final_pt_blocks):
            new_ct_block = self.flip_iv(final_ct_blocks[i], final_pt_blocks[i])
            final_ct_blocks.append(b"A" * self.block_size)

        # The last element is the IV
        final_iv = final_ct_blocks[-1]
        # Remove last element and restore original order
        final_ct_blocks = final_ct_blocks[:-1][::-1]
        final_ct = b"".join(final_ct_blocks)

        return final_ct, final_iv

    def crack_fixed_iv_with_encrypt(
        self, initial_iv: bytes, final_pt: bytes, initial_pt: bytes = None
    ):
        """
        Returns a ciphertext and an IV such that, when decrypted, the first block becames the first block of the plaintext final_pt. You need to use the encryption function once.
        """
        if initial_pt == None:
            initial_pt = b"A" * self.block_size

        # final_pt = pad(final_pt, self.block_size)
        # initial_pt = pad(initial_pt, self.block_size)

        assert (
            len(initial_iv) == self.block_size
        ), f"The initial IV must have length equal to the block length ({self.block_size})"
        # assert (
        #     len(final_pt) > 0 and len(final_pt) % self.block_size == 0
        # ), f"The final plaintext must have length that is a positive multiple of the block length ({self.block_size})"
        # assert (
        #     len(final_pt) > 0 and len(initial_pt) % self.block_size == 0
        # ), f"The initial plaintext must have length that is a positive multiple of the block length ({self.block_size})"
        # assert len(final_pt) == len(
        #     initial_pt
        # ), f"The final and the initial plaintext must have the same length"

        ct = self.encrypt(initial_pt)
        final_iv = flip(
            initial_iv, initial_pt[: self.block_size], final_pt[: self.block_size]
        )

        return ct, final_iv


# RSA

class RSACracker:
    def __init__(self, n=None, e=65537, d=None, p=None, q=None, phi=None):
        self.n = n
        self.e = e
        self.p = p
        self.q = q
        self.phi = phi
        self.d = d

        if p and q:
            self.n = p * q
            self.phi = (p - 1) * (q - 1)

        if self.phi:
            self.d = inverse(self.e, self.phi)

    def encrypt(self, message: int):
        assert self.n and self.e, "Not enough information provided: n and e are missing"
        return pow(message, self.e, self.n)

    def decrypt(self, enc_message: int):
        assert self.n and self.d, "Not enough information provided: n and d are missing"
        return pow(enc_message, self.d, self.n)

    # def get_d(self):
    #     self.d = inverse(self.e, self.phi)

    #     return self.d

    def factorize_n(self, check_factordb=True):
        """
        This attack can be used if n is small, if it's easy to find a factor or if the factors are really close
        """

        if check_factordb:
            f = FactorDB(self.n)
            f.connect()
            status = f.get_status()

            assert status == "FF", "Can't find factors on factordb"
            
            factors = f.get_factor_list()

            assert len(factors) == 2, "n is not a product of two distinct primes"
        else:
            factors = factorint(self.n)

            assert len(factors) == 2, "n has not 2 factors"

            for factor in factors.keys():
                assert factors[factor] == 1, "At least a prime factor of n has multiplicity greater than 1"

            factors = list(factors.keys())

        self.p, self.q = factors[0], factors[1]
        self.phi = (self.p - 1) * (self.q - 1)

        return self.p, self.q
    
    def solve_discrete_log(self, message: int, cipher: int):
        # cipher^d = message mod n
        self.d = dlog(self.n, message, cipher)

        return self.d

class RSAOracleCracker:
    # TEMP - IMPR
    pass

class DiffieHellmanCracker:
    def __init__(self, g=None, p=None, pubA=None, pubB=None, privA=None, privB=None, shared_secret=None):
        self.g = g
        self.p = p
        self.pubA = pubA
        self.pubB = pubB
        self.privA = privA
        self.privB = privB
        self.shared_secret = shared_secret

        if g and p:
            if privA:
                self.pubA = pow(g,privA, p)
            
            if privB:
                self.pubB = pow(g, privB, p)
        
    def solve_discrete_log(self):
        if self.pubA:
            self.privA = dlog(self.p, self.pubA, self.g)
        
        if self.pubB:
            self.privB = dlog(self.p, self.pubB, self.g)

        self.shared_secret = pow(self.pubA, self.privB, self.p)


# Hashing functions
# MAC (Message Authentication Cose)

# Digital Signature

# DSA (Digital Signature Algorithm)


class DSACracker:
    def __init__(
        self,
        p: int,
        q: int,
        H,
        g: int = None,
        y: int = None,
        h: int = None,
        x: int = None,
        k=None,
        check=True,
    ):
        """
        H is the hashing function
        q is the smallest public prime in DSA
        m1 is the first message
        m2 is the second message
        (r1, s1) is the first signature
        (r2, s2) is the second signature
        """

        if check:
            if not (
                isinstance(p, int),
                isinstance(q, int) and isinstance(
                    g, int) and isinstance(y, int),
            ):
                raise ValueError("p, q, g, y must be an integers")

            if not isinstance(k, int):
                if k != None:
                    raise ValueError("k must be an integer or None")
            else:
                if not (1 <= k <= (q - 1)):
                    raise ValueError(
                        "h must be greater or equal to 2 and less than or equal to p-2"
                    )

            if not isinstance(h, int):
                if h != None:
                    raise ValueError("h must be an integer or None")
            else:
                if not (2 <= h <= (p - 2)):
                    raise ValueError(
                        "h must be greater or equal to 2 and less than or equal to p-2"
                    )

            if not isinstance(g, int):
                if g != None:
                    raise ValueError("g must be an integer or None")
                else:
                    if h == None:
                        raise ValueError(
                            "You have to set as integer at least one between h and g"
                        )
                    else:
                        g = pow(h, (p - 1) // q, p)
            else:
                if h != None:
                    if g != pow(h, (p - 1) // q, p):
                        raise ValueError(
                            "g must be equal to pow(h, (p - 1) // q, p)")

            if not isinstance(y, int):
                if y != None:
                    raise ValueError("y must be an integer or None")
                else:
                    if x == None:
                        raise ValueError(
                            "You have to set as integer at least one between x and y"
                        )
                    else:
                        y = pow(g, x, p)
            else:
                if x != None:
                    if y != pow(g, x, p):
                        raise ValueError("y must be equal to pow(g, x, p)")

            if not isinstance(x, int):
                if x != None:
                    raise ValueError("x must be an integer or None")
            else:
                if not (1 <= x <= (q - 1)):
                    raise ValueError(
                        "x must be greater or equal to 1 and less than or equal to q-1"
                    )

                if y != pow(g, x, p):
                    raise ValueError("y must be equal to pow(g, x, p)")

            if not isPrime(p):
                raise ValueError("p must be a prime number")

            if not isPrime(q):
                raise ValueError("q must be a prime number")

            if Mod(p - 1, q) != 0:
                raise ValueError("q must divide p-1.")

        self.q = q
        self.p = p
        self.g = g
        self.y = y
        self.H = H
        self.h = h
        self.x = x
        self.k = k

    def sign(self, message: int, k=None):
        random_seed = False
        if k is None:
            if self.k != None:
                k = self.k
            else:
                random_seed = True

        if random_seed:
            s = 0
            while s == 0:
                k = random.randint(1, self.q - 1)
                r = Mod(pow(self.g, k, self.p), self.q)
                s = (inverse(k, self.q) * Mod(self.H(message) + self.x * r), self.q)
        else:
            r = Mod(pow(self.g, k, self.p), self.q)
            # r = pow(self.g, k, self.p) % self.q
            s = inverse(k, self.q) * Mod(self.H(message) + self.x * r, self.q)

        return r, s

    def verify(self, message: int, r: int, s: int):
        a = pow(self.g, self.H(message) *
                Mod(inverse(s, self.q), self.q), self.p)
        b = pow(self.y, Mod(r * inverse(s, self.q), self.q), self.p)

        is_signature_valid = (a * b % self.p) % self.q == r

        return is_signature_valid

    def get_x_given_message_and_seed(self, m, r: int, s: int, k=None) -> int:
        """
        m is the message
        (r, s) is the signature of m
        k is the seed m was generated with, if it's None, it defaults to self.k
        """

        if k == None:
            k = self.k

            if k == None:
                raise ValueError("Nonce is not set")

        a = Mod(k * s - self.H(m), self.q)
        b = inverse(r, self.q)
        x = Mod(a * b, self.q)

        self.x = x

        return x

    def get_x_given_same_seed_messages(
        self, m1, m2, r1: int, s1: int, r2: int, s2: int
    ) -> int:
        """
        We recover the private key x if the signatures have been generated with the same nonce
        """
        z = inverse((r2 * s1 - r1 * s2), self.q)
        x = Mod((s2 * self.H(m1) - s1 * self.H(m2)) * z, self.q)

        self.x = x

        return x

    def get_seed_given_linear_relation(
        self, m, s1: int, s2: int, l: int
    ) -> tuple[int, int]:
        """
        Given the message m and two signatures of m (r1, s1), (r2, s2) generated respectively with k and k+l, we recover the seed k. Actually we get two possible values of k, therefore we return the couple (k1, k2)
        """
        d = Mod(pow(self.g, l, self.p), self.q)
        c = Mod(s2 - d * s1, self.q)
        z = self.H(m)

        # a = -((c + s2) * l + (d - 1) * z)
        # b = sqrt(a**2 - 4 * c * l * (s2 * l + (d + 1) * z))
        # print(f"{b = }")
        # e = inverse(2 * c, self.q)

        f = inverse(c, self.q)
        k0 = Mod(-f * (s2 * l + z * (d - 1)), self.q)

        # k1 = Mod((a + b) * e, self.q)
        # k2 = Mod((a - b) * e, self.q)

        return k0  # , k1, k2


# RNG (Random number generation)
class LCGCracker:
    def __init__(self, x: list[int] = None, n=None, a=None, b=None):
        self.x = x
        self.n = n
        self.a = a
        self.b = b

    def next(self):
        assert self.x and len(
            self.x) >= 1, "At least one value of x is required"

        last_index = len(self.x) - 1
        next_value = Mod(self.a * self.x[last_index] + self.b, self.n)
        self.x.append(next_value)

        return next_value

    def get_b(self):
        assert self.n, "n is required"
        assert self.a, "a is required"
        assert self.x and len(
            self.x) >= 2, "At least two values of x are required"

        self.b = Mod(self.x[1] - self.a * self.x[0], self.n)

        return self.b

    def get_a(self):
        assert self.n, "n is required"
        assert self.x and len(
            self.x) >= 3, "At least three values of x are required"

        h = self.x[2] - self.x[1]
        f = self.x[1] - self.x[0]

        self.a = Mod(h * inverse(f, self.n), self.n)

        return self.a

    def get_n(self):
        """
        Let x be a sequence generated with LCG, we want to get the modulus n, with this approach we can get it if we have "enough" values of x
        """
        assert self.x and len(
            self.x) >= 4, "At least four values of x are required"

        t = [self.x[i + 1] - self.x[i] for i in range(len(self.x) - 1)]
        z = [t[i - 1] * t[i + 1] - t[i] ** 2 for i in range(1, len(t) - 1)]
        self.n = math.gcd(*z)

        return self.n
