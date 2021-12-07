import sys
import base64

input_txt = sys.argv[1]
output_txt = sys.argv[2]
original = ''
encrypted = ''
key = ''
with open(input_txt) as input:
    original = input.read()
with open(output_txt) as output:
    encrypted = output.read()
    encrypted = base64.b64decode(encrypted)
    encrypted = encrypted.decode("utf-8")
for idx in range(len(original)):
    key += chr(ord(original[idx]) ^ ord(encrypted[idx]))
for i in range(1, len(key)):
    if key[:2 * i] == key[:i] * 2:
        print(key[:i])
        exit(0)
