# -*- coding: utf-8 -*-
import hashlib, random, time

# Caesar Cipher
class CaesarCipher:
    def process(self, message, key, mode=1):
        result = ""
        shift = (key % 26) if mode == 1 else (-key % 26)  # handles negative keys too
        
        for char in message:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result

if __name__ == "__main__":
    c = CaesarCipher()
    msg = input("Enter message: ")
    key = int(input("Enter key: "))
    opt = int(input("1 = Encrypt, 2 = Decrypt: "))

    out = c.process(msg, key, 1 if opt == 1 else 2)
    print("Result:", out)
