# Crypto library for CTFs

import itertools

english_freqs = {'e': .1202,
                 't': .0910,
                 'a': .0812,
                 'o': .0768,
                 'i': .0731,
                 'n': .0695,
                 's': .0628,
                 'r': .0602,
                 'h': .0592,
                 'd': .0432,
                 'l': .0398,
                 'u': .0288,
                 'c': .0271,
                 'm': .0261,
                 'f': .0230,
                 'y': .0211,
                 'w': .0209,
                 'g': .0203,
                 'p': .0182,
                 'b': .0149,
                 'v': .0111,
                 'k': .0069,
                 'x': .0017,
                 'q': .0011,
                 'j': .0010,
                 'z': .0007}


def letter_frequencies(text):
    """Returns a dictionary mapping each letter to it's corresponding frequency
    in the given text
    """
    text = text.lower()
    freqs = {}
    for c in text:
        if c in freqs:
            freqs[c] += 1.0
        else:
            freqs[c] = 1.0

    for c in freqs.keys():
        freqs[c] /= len(text)

    return freqs


def split(text, keylen):
    """Splits the text into keylen different strings, where the ith
    character of the text is placed into the `i % keylen` returned string.
    """
    results = [""] * keylen
    for i in range(0, len(text)):
        results[i % keylen] += text[i]

    return results


def repeated_xor(m, k):
    """Applies the key k to the message m with a repeated XOR"""
    return map(lambda t: chr(ord(t[0]) ^ ord(t[1])), zip(m, itertools.cycle(k)))

def crack_repeated_xor(ciphertext, keylen, non_printable_chars=[10]):
    """Given a ciphertext and a key length, returns a list of lists where each
    inner list contains all possible bytes that could have been XORed with the
    corresponding byte of the plaintext to get the given ciphertext, assuming
    the plaintext only consists of printable ascii characters and excluding the
    characters given in non_printable_chars.
    """
    possible_keys = []
    split_strs = split(ciphertext, keylen)
    for i in range(0, len(split_strs)):
        possible_keys.append([])
        s = split_strs[i]

        for key in range(0, 256):
            # XOR the current byte with all the bytes in the string
            res = ""
            for c in s:
                res += str(chr(ord(c) ^ key))

            # Check if all characters are valid ascii
            good = True
            for c in res:
                if not (ord(c) in non_printable_chars or
                        (ord(c) >= 32 and ord(c) <= 127)):
                    good = False
                    break

            if good:
                possible_keys[i].append(key)

    return possible_keys


def b2i(s):
    """Takes a string of bytes and converts it to an arbitrary precision int
    (with no trailing 'L')
    """
    return int(s.encode('hex').rstrip('L'), 16)


def i2b(i):
    """Takes an integer and converts it to a string of bytes"""
    res = '%x' % i

    # Make sure the hex string is of even length
    if len(res) % 2 != 0:
        res = '0' + res

    return res.decode('hex')


def xor_list(s1, s2):
    """XORs the bytes of two lists together"""
    return ''.join(map(lambda t: chr(ord(t[0]) ^ ord(t[1])), zip(s1, s2)))


def blocks(m, bsize=16):
    """Splits a message into an array of blocks"""
    return [m[i:i + bsize] for i in range(0, len(m), bsize)]

def egcd(a, b):
    """Extended euclidean algorithm"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mult_inv(a, m):
    """Multiplicative inverse"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m