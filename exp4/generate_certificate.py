# -*- coding: utf-8 -*-
import subprocess, os, sys, hashlib

# Ask for cert details
country = input("Country Code (e.g., IN): ").strip() or "IN"
state = input("State: ").strip() or "NA"
locality = input("Locality/City: ").strip() or "NA"
organization = input("Organization Name: ").strip() or "Org"
org_unit = input("Organizational Unit: ").strip() or "Unit"
common_name = input("Common Name (e.g., localhost): ").strip() or "localhost"

# Absolute base path
BASE_DIR = "/home/raghu/Documents/NSELab/exp4"

# ---- NEW FEATURE 1: Auto create dir ----
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
    print("\nCreated base directory:", BASE_DIR)

PRIVATE_KEY_FILE = os.path.join(BASE_DIR, "private.key")
CERT_FILE = os.path.join(BASE_DIR, "certificate.crt")

def run(cmd):
    r = subprocess.run(cmd, text=True, shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        print("Error:", r.stderr)
        sys.exit(1)
    return r.stdout

# Gen private key
print("\nGenerating private key...")
run(f"openssl genpkey -algorithm RSA -out \"{PRIVATE_KEY_FILE}\" -pkeyopt rsa_keygen_bits:2048")

# Gen cert
print("Generating self-signed certificate...")
subj = f"/C={country}/ST={state}/L={locality}/O={organization}/OU={org_unit}/CN={common_name}"
run(f"openssl req -new -x509 -key \"{PRIVATE_KEY_FILE}\" -out \"{CERT_FILE}\" -days 365 -subj \"{subj}\"")

print("Done. Cert saved at:", CERT_FILE)

# ---- NEW FEATURE 2: Print cert fingerprint ----
with open(CERT_FILE, "rb") as f:
    fp = hashlib.sha256(f.read()).hexdigest()
    print("\nCert Fingerprint (SHA-256):", fp)
