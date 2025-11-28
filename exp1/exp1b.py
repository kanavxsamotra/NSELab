# -*- coding: utf-8 -*-
class VigenereCipher:

    # ---- NEW FEATURE 1: extend key cleanly to match only letters length ----
    def _extend_key(self, message, key):
        key = key.upper()
        letters = [c for c in message if c.isalpha()]
        return ''.join(key[i % len(key)] for i in range(len(letters)))

    def encrypt(self, message, key):
        extended_key = self._extend_key(message, key)
        result = []
        k = 0

        for char in message:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                shift = ord(extended_key[k]) - 65
                enc = chr((ord(char.upper()) - 65 + shift) % 26 + offset)
                result.append(enc.lower() if char.islower() else enc)
                k += 1
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, message, key):
        extended_key = self._extend_key(message, key)
        result = []
        k = 0

        for char in message:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                shift = ord(extended_key[k]) - 65
                dec = chr((ord(char.upper()) - 65 - shift + 26) % 26 + offset)
                result.append(dec.lower() if char.islower() else dec)
                k += 1
            else:
                result.append(char)
        return ''.join(result)


# ---- NEW FEATURE 2: show 26 shift preview (tiny breaking aid) ----
def show_shifts(text):
    print("\n26-Shift preview:")
    for s in range(26):
        out = ""
        for c in text:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                out += chr((ord(c) - base + s) % 26 + base)
            else:
                out += c
        print(f"{s:2}:", out)


if __name__ == "__main__":
    v = VigenereCipher()
    msg = input("Enter message: ")
    key = input("Enter key: ")

    ct = v.encrypt(msg, key)
    print("Encrypted:", ct)

    pt = v.decrypt(ct, key)
    print("Decrypted:", pt)

    # optional analysis
    show_shifts(ct)
