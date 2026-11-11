# CHIFFREMENT-PAR-DECALAGE-INF-381
Il s'agit d'un TP expérimental sur les méthodes de chiffrement et déchiffrement et nous sommes axés sur le chiffrement par décalage ou Cesar 

# Chiffrement par décalage (César) en Python

TP de cryptographie : chiffrement, déchiffrement et cryptanalyse du chiffrement par décalage.

## Principe
- Chiffrer : `C = (P + k) mod 26`
- Déchiffrer : `P = (C - k) mod 26`
- 26 clés possibles (25 utiles).

## Fichiers
- `cesar.py` : fonctions `chiffrer`, `dechiffrer`, `force_brute`, `cle_par_frequence` et menu interactif
- `test_cesar.py` : tests

## Utilisation
```bash
python cesar.py          # menu interactif
python test_cesar.py     # lance les tests
```