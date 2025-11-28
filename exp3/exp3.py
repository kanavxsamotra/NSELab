# -*- coding: utf-8 -*-
import hashlib, random

user_secrets = {"alice": "alice_secret_key", "bob": "bob_secret_key"}
used_nonces = set()
success = fail = 0  # ---- NEW FEATURE 1: track attempts ----

def generate_nonce():
    return str(random.randint(100000, 999999))

def hash_response(n, s, u):
    return hashlib.sha256((n + s + u).encode()).hexdigest()

user = input("User? (alice/bob): ").strip().lower() or "bob"  # ---- NEW FEATURE 2: quick user switch ----
secret = user_secrets.get(user)
nonce = generate_nonce()
print("Nonce:", nonce)

resp = hash_response(nonce, secret, user)
print("Response:", resp)

if nonce in used_nonces:
    print("Replay detected")
    fail += 1
else:
    if resp == hash_response(nonce, secret, user):
        print("Auth OK for", user)
        used_nonces.add(nonce)
        success += 1
    else:
        print("Auth Failed")
        fail += 1

print("\nStats → Success:", success, "| Fail:", fail)
