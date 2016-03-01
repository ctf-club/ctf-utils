from crypto import *

def test_letter_frequencies():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alph_freqs = letter_frequencies(alphabet)
    for i, j in alph_freqs.iteritems():
        assert j == 1.0/26.0

def test_split():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    empty = ""
    assert split(empty, 4) == ["","","",""]
    assert split(alphabet, 2) == ["acegikmoqsuwy","bdfhjlnprtvxz"]
    assert split(alphabet, 3) == ["adgjmpsvy","behknqtwz","cfilorux"]
    assert split(alphabet, 26) == ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def test_shift():
    test_str = "a"
    for i in range(0, 25):
        assert shift(test_str, i) == chr(ord("a") + i)

def test_repeated_xor():
    pass

def test_crack_repeated_xor():
    pass

def test_b2i():
    pass

def test_i2b():
    pass

def test_xor_list():
    pass

def test_blocks():
    pass

def test_egcd():
    pass

def test_mult_inv():
    pass

def test_crack_caeser_cipher():
    with open("cae_cipher.txt", 'r') as file:
        text = file.read().replace('\n','') 
    with open("plain.txt", 'r') as file:
        plain = file.read().replace('\n','') 

    assert crack_caeser_cipher(text)[0][2] == plain

def test_vigenere_encrypt():
    with open("vig_cipher.txt", 'r') as file:
        text = file.read().replace('\n','') 
    with open("plain.txt", 'r') as file:
        plain = file.read().replace('\n','') 

    assert vigenere_encrypt(plain, "lemon") == text

def test_get_vigenere_key_length():
    with open("vig_cipher.txt", 'r') as file:
        text = file.read().replace('\n','') 
    assert get_vigenere_key_length(text)[0] == 5 #key is lemon


def test_crack_vigenere_cipher():
    with open("vig_cipher.txt", 'r') as file:
        text = file.read().replace('\n','') 
    with open("plain.txt", 'r') as file:
        plain = file.read().replace('\n','') 

    assert crack_vigenere_cipher(text)[0][2] == plain

def main():
    test_split()
    test_shift()
    test_letter_frequencies()
    test_crack_caeser_cipher()
    test_vigenere_encrypt()
    test_get_vigenere_key_length()    
    test_crack_vigenere_cipher()


if __name__ == "__main__":
    main()
    
