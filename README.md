ctf-utils
=========

Utilities for participating in CTF competitions.

Currently supports:
- Cracking Caesar ciphers
- Cracking Vigenere ciphers
- Cracking repeated XOR ciphers
- Number theory functions: `egcd`, `mult_inv`
- Utility functions: `blocks`, `b2i`, `i2b`

TODO:
- Implement `get_vigenere_key_length()`

Possible improvements:
- Use the [word break algorithm](http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/) algorithm with the cipher cracking algorithms
- Use [bigram](https://en.wikipedia.org/wiki/Bigram) frequencies with the cipher cracking algorithms
