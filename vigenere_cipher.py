def vigenere_encrypt(P, Key):
    C = ""
    count=0
    for i in range(len(P)):
        if not P[i].isalpha():
            C += " "
        elif P[i]>="A" and P[i]<="Z":
            C += chr((ord(P[i])+ord(Key[count%len(Key)])) % 26+ord("A"))
        else:
            C += chr((ord(P[i])+ord(Key[count%len(Key)])) % 26+ord("a"))
        count+=1
    return C


def vigenere_decrypt(C, Key):
    P = ""
    count = 0
    for i in range(len(C)):
        if not C[i].isalpha():
            P += " "
        elif C[i] >= "A" and C[i] <= "Z":
            P += chr((ord(C[i])-ord(Key[count % len(Key)])) % 26+ord("A"))
        else:
            P += chr((ord(C[i])-ord(Key[count % len(Key)])) % 26+ord("a"))
        count += 1
    return P

Plaintext = "ATTACKATDAWN"
Cipertext = vigenere_encrypt(Plaintext, "LEMON")
print(Cipertext)
print(vigenere_decrypt(Cipertext, "LEMON"))
