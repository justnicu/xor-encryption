import sys
import base64

output = sys.argv[1]

# functie care gaseste cele mai folosite caractere 
# dintr-un text random in limba romana
def get_popular_chars(str):
    dict = {}
    for c in str:
        if not c in dict:
            dict[c] = 0
        dict[c] += 1

    ans = ""
    for i in range(10):
        mx = 'a'
        for key in dict:
            if dict[key] > dict[mx]:
                mx = key
        dict[mx] = 0
        ans += mx

    return ans

# functie care imparte un text in string-uri formate din caractere 
# care vor fi criptate folosind acelasi caracter din cheie
def divide_text(text, key_len):
    v = []
    for pos in range(key_len):
        curr_block = ""
        for i in range(pos, len(text), key_len):
            curr_block += text[i]
        v.append(curr_block)
    return v

# distanta hamming intre 2 texte
def hamming_dist(a, b):
    dist = 0
    for idx in range(len(a)):
        x = ord(a[idx]) ^ ord(b[idx])

        bits = 0
        while x:
            bits += x & 1
            x >>= 1
        dist += bits
    return dist

# functie care returneaza cea mai probabila lungime a cheii
# bazandu-se pe faptul ca distanta hamming dintre litere este una foarte mica, 
# iar operatia xor nu schimba distanta hamming dintre 2 string uri.
# Astfel cea mai probabila lungime este cea care da distanta hamming minima 
# intre blocuri consecutive de lungime key_len
def get_key_len(text):
    best = None
    best_len = 0

    for key_len in range(10, 16):
        avg = []
        for i in range(0, len(text) - 2 * key_len, key_len):
            first_block = text[i:i+key_len]
            second_block = text[i+key_len:i + 2*key_len]

            dist = hamming_dist(first_block, second_block)
            avg.append(dist / key_len)

        # calculam distanta hamming medie
        # daca e minima, updatam lungimea
        average = sum(avg) / len(avg)
        if best == None or best > average:
            best = average
            best_len = key_len

    print("Lungimea cheii: " + str(best_len))
    return best_len

# functie care gaseste cheia printr-un brute-force,
# alegand pe fiecare pozitie caracterul din care rezulta cele mai multe caractere 
# dintre cele mai populare caractere gasite anterior 
def get_key(text, key_len, common_letters):

    # textul impartit pe bucati care sunt criptate cu acelasi caracter din cheie
    divided_text = divide_text(text, key_len)

    # toate caracterele posibile din cheie
    possible_key_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    key = ''
    
    for block in divided_text:
        high_score = 0
        best_char = ''
    
        for c in possible_key_chars:
            x = [chr(ord(c) ^ ord(char)) for char in block]

            # gasim scorul caracterului
            curr_score = 0
            for k in x:
                if k in common_letters:
                    curr_score += 1

            # updatam caracterul daca am gasit unul mai bun
            if curr_score > high_score:
                high_score = curr_score
                best_char = c
        
        key += best_char
    
    return key

# gasim caracterele populare
caractere_populare = ''
with open("text_romana.txt", 'r') as f:
    caractere_populare = get_popular_chars(f.read())
    print("Caracterele populare: " + caractere_populare)

# decodam fisierul din baza 64
output_text = ''
with open(output, 'r') as f:
    output_text = f.read()
output_text = base64.b64decode(output_text).decode('utf-8')

# gasim cheia
key = get_key(output_text, get_key_len(output_text), caractere_populare)
print("Cheie: " + key)



