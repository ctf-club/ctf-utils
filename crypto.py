# Crypto library for CTFs

english_freqs = {'e': .1202,
                 't': .910,
                 'a': .812,
                 'o': .768,
                 'i': .731,
                 'n': 6.95,
                 's': .628,
                 'r': .602,
                 'h': .592,
                 'd': .432,
                 'l': .398,
                 'u': .288,
                 'c': .271,
                 'm': .261,
                 'f': .230,
                 'y': .211,
                 'w': .209,
                 'g': .203,
                 'p': .182,
                 'b': .149,
                 'v': .111,
                 'k': .069,
                 'x': .017,
                 'q': .011,
                 'j': .010,
                 'z': .007}


def letter_frequencies(text):
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
    """
    Splits the text into keylen different strings, where the ith
    character of the text is placed into the `i % keylen` returned string.
    """
    results = [""] * keylen
    for i in range(0, len(text)):
        results[i % keylen] += text[i]

    return results


def repeated_xor(ciphertext, keylen, non_printable_chars=[10]):
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
