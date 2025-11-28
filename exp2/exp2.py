# -*- coding: utf-8 -*-
import hashlib, sys

sender_file = "/home/Kanav/Documents/network-security-lab/exp2/sender.txt"

def file_hash(path, algo="sha256"):
    try:
        h = hashlib.new(algo)
        with open(path, "rb") as f:
            h.update(f.read())
        return h.hexdigest()
    except FileNotFoundError:
        print("File not found:", path)
        sys.exit(1)
    except ValueError:
        print("Invalid hash algorithm")
        sys.exit(1)

def check(h1, h2):
    return "✅ Match" if h1 == h2 else "❌ No Match"

# ---- Step 1: hash sender file ----
algo = input("Algo? (sha256/md5): ").strip().lower() or "sha256"
sender_hash = file_hash(sender_file, algo)
print("\nSender Hash:", sender_hash)

# ---- Step 2: hash receiver file ----
receiver_file = input("Receiver file path: ").strip()
receiver_hash = file_hash(receiver_file, algo)
print("\nReceiver Hash:", receiver_hash)

# ---- New Feature 2: clean hash verification ----
print("\nVerification result:", check(sender_hash, receiver_hash))
