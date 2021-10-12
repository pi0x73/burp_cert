#!/usr/bin/python3

#UGLY SCRIPT OF CONVERTING THE BURPSUITE CERTIFICATE FROM .DER TO .PEM

import ssl
from cryptography import x509
import os
import urllib.request


url = 'http://127.0.0.1:8080/cert'
response = urllib.request.urlopen(url)
burp_cert = response.read()

burp_cert_PEM = ssl.DER_cert_to_PEM_cert(burp_cert);

print("[!]saved at burp.pem.")

with open("burp.pem", "a") as o:
    o.write(burp_cert_PEM)
