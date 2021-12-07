# XOR Encryption

Un program care realizează criptarea / decriptarea XOR, scris in Python 3.

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
Această comandă va afișa în consolă parola care a fost folosită pentru a cripta fișierul fisier_input în fisier_output. Programul aplica operația XOR între caracterele de pe aceleași poziții din fisier_input și fisier_ouput (input XOR (input XOR key) = key) și afișează cel mai scurt repeating pattern (care este chiar parola folosită pentru criptare).

## Membrii echipei:
* Vlad Ciocoiu
* Alex Pascu
* Andrei Nicula
