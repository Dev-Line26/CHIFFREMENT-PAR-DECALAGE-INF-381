from cesar import chiffrer, dechiffrer, force_brute, cle_par_frequence

MESSAGE = "OH FKLIIUHPHQW HV IDFLOH"


def test_aller_retour():
    assert dechiffrer(chiffrer("BONJOUR", 5), 5) == "BONJOUR"

def test_exercice_3():
    assert dechiffrer(MESSAGE, 3) == "LE CHIFFREMENT ES FACILE"

def test_cle_0():
    assert chiffrer("Bonjour", 0) == "Bonjour"

def test_cle_26():
    assert chiffrer("Abc xyz", 26) == "Abc xyz"

def test_cle_negative():
    assert chiffrer("DEF", -3) == "ABC"

def test_cle_superieure_a_26():
    assert chiffrer("ABC", 29) == chiffrer("ABC", 3) == "DEF"

def test_casse_conservee():
    assert chiffrer("AbC", 1) == "BcD"

def test_ponctuation_et_chiffres():
    assert chiffrer("a, b! 123", 1) == "b, c! 123"

def test_accents_inchanges():
    assert chiffrer("été", 3) == "éwé"

def test_texte_vide():
    assert chiffrer("", 7) == ""

def test_force_brute_contient_la_solution():
    assert (3, "LE CHIFFREMENT ES FACILE") in force_brute(MESSAGE)
    assert len(force_brute(MESSAGE)) == 26

def test_frequence():
    assert cle_par_frequence(MESSAGE) == 3


if __name__ == "__main__":
    tests = [f for n, f in sorted(globals().items()) if n.startswith("test_")]
    for t in tests:
        t()
        print("OK  ", t.__name__)
    print(f"\n{len(tests)} tests réussis.")
