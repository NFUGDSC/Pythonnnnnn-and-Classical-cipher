def Ceacar_encrypt(P, offset):
    C = ""
    for i in range(len(P)):
        if not P[i].isalpha():
            C += " "
        C += chr((ord(P[i])-ord("a")+offset) % 26+ord("a"))
    return C


def Ceacar_decrypt_enum(C):
    for offset in range(1,26):
        P = ""
        for i in range(len(C)):
            if not C[i].isalpha():
                P += " "
            P += chr((ord(C[i])-ord("a")-offset) % 26+ord("a"))
        print(P,offset)


Plaintext = "abcdefghijklmnopqrstuvwxyz"
Cipertext = Ceacar_encrypt(Plaintext, 3)
print(Cipertext)
Ceacar_decrypt_enum(Cipertext)
