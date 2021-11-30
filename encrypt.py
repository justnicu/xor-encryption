# biblioteca pentru folosirea argumentelor din command lime
from sys import argv

# destructuring, echivalent cu a da variabilelor valorile din argv, in ordine
password, fin, fout = argv[1:4]

# citim input-ul
with open(fin) as f:
    s = f.read()

string_length = len(s)
pass_length = len(password)

# criptam input-ul aplicand xor pe fiecare caracter 
# cu caracterul corespunzator din cheie 
res = ""
for i in range(string_length):
    ch = chr(ord(s[i]) ^ ord(password[i % pass_length]))
    res += ch

# scriem textul criptat in fisiserul output
with open(fout, "wb") as f:
    byte_res = bytearray(res, "utf8")
    f.write(byte_res)