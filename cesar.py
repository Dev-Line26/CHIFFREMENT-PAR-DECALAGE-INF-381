from collections import Counter

def decaler(texte, k):
    resultat = []
    for c in texte:
        if c.isascii() and c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultat.append(chr((ord(c)-base + k)%26 + base))
        else:
            resultat.append(c)
    return "".join(resultat)

def chiffrer(texte, k):
    return decaler(texte, k)

def dechiffrer(texte, k):
    return decaler(texte, -k)

def force_brute(texte):
    return [(k, dechiffrer(texte, k)) for k in range(26)]

def cle_par_frequence(texte, lettre_frequente="E"):
    lettres=[c.upper() for c in texte if c.isascii() and c.isalpha()]
    if not lettres:
        return None
    plus_frequente= Counter(lettres).most_common(1)[0][0]
    return (ord(plus_frequente) - ord(lettre_frequente.upper()))%26

def menu():
    while True:
        print("\n== chiffrement par decalage ===")
        print("1. Chiffrer\n2. Dechiffer\n3. force_brute\n4. Analyse de frequence\n0. Quitter")
        choix= input("choix : ").strip()
        if choix == "0":
            break
        if choix not in{"1", "2", "3", "4"}:
            print("Choix invalide")
            continue
       
        if choix in {"1","2"}:
            try:
                k=int(input("cle (entier): "))
            except ValueError:
                print("La cle doit etre un entier.")
                continue
            
            print("Resultat:", (chiffrer if choix == "1" else dechiffrer)(texte , k))
        elif choix == "3":
            for k, t in force_brute(texte):
                print(f"k={k:2d} : {t}")
        else:
            k= cle_par_frequence(texte)
            if k is None:
                print("Aucune lettre a analyser.")
            else:
                print(f"Cle probable: {k}")
                print("Texte probable :", dechiffrer(texte ,k))
                    

if __name__ == "__main__":
    menu()