# XOR Encryption

Un program care realizează criptarea / decriptarea XOR, precum si spargerea unei criptari asemanatoare, scris in Python 3.

## Utilizare
##### Criptare:
```
python encrypt.py cheie fisier_input fisier_output
```
Această comandă va cripta textul din fișierul text fisier_input în fișierul binar fisier_output, folosind cheia 'cheie'.

##### Decriptare:
```
python decrypt.py fisier_output cheie fisier_input_recuperat
```
Această comandă va decripta textul din fișierul binar fisier_output în fișierul text fisier_input_recuperat, folosind cheia 'cheie'.

##### Spargerea parolei în funcție de input și output:
```
python3 input_output_cracker.py fisier_input fisier_output
```
Această comandă va afișa în consolă parola care a fost folosită pentru a cripta fișierul fisier_input în fisier_output. Programul aplică operația XOR între caracterele de pe aceleași poziții din fisier_input și fisier_ouput (input XOR (input XOR key) = key) și afișează cel mai scurt repeating pattern (care este chiar parola folosită pentru criptare).

##### Spargerea parolei folosind doar fisierul output:
```
python3 find_key.py fisier_output
```
Pentru a sparge o parola folosind doar fisierul output, am folosit cateva observatii:
* Distanta Hamming dintre 2 litere (numarul de biti de 1 din XOR-ul lor) este, in medie, foarte mica
* Distanta Hamming dintre (a ^ key) si (b ^ key) este egala cu distanta Hamming dintre a si b pentru orice litere a, b si orice cheie key de lungime 1 
* Un text in limba romana nu are caracterele distribuite la intamplare, astfel ca ne putem folosi de cele mai populare caractere pentru a gasi cea mai probabila cheie

Astfel, algoritmul de spargere a parolei consta in: 
* Gasirea celor mai folosite caractere din limba romana (calculate la runtime folosind un text la intamplare in limba romana, gasit in fisierul text_romana.txt), 
* Decodarea fisierului output din baza 64 in string
* Gasirea celei mai probabile lungimi a parolei, incercand toate variantele len de la 10 la 15 si calculand suma distantelor Hamming dintre toate substring-urile consecutive de lungime len si alegerea lungimii pentru care distanta medie e minima
* Gasirea cheii, incercand toate caracterele posibile pentru fiecare pozitie si alegandu-l pe cel pentru care textul decriptat cu ajutorul lui contine cele mai multe caractere populare ale limbii romane, gasite anterior

## Confruntare
Link Repo adversari: https://github.com/vali2wd/XOR_Encryption-ASC-  
Parola: parolamea2021

## Membrii echipei
* Vlad Ciocoiu
* Alex Pascu
* Andrei Nicula
