from sys import argv

fin, password, fout = argv[1:4]

# citim textul criptat
with open(fin, "rb") as f:
    s = f.read().decode("utf8")

string_length = len(s)
pass_length = len(password)

# decriptam textul folosin cheia
res = ""
for i in range(string_length):
    ch = chr(ord(s[i]) ^ ord(password[i % pass_length]))
    res += ch

# afisam textul decriptat
with open(fout, "w") as f:
    f.write(res)