from itertools import product

def pgcd(x, y):
    """Calcule le PGCD de x et y avec pgcd(0,0) = 0"""
    while y != 0:
        x, y = y, x % y
    return abs(x) if x != 0 else 0

def est_endomorphisme(f, M):
    """Vérifie si f préserve l'opération PGCD"""
    return all(f[pgcd(x, y)] == pgcd(f[x], f[y]) for x, y in product(M, repeat=2))

def est_idempotent(f, M):
    """Vérifie si f ∘ f = f"""
    return all(f[f[x]] == f[x] for x in M)

def image_propre(f, M):
    """Calcule l'image directe de f"""
    return {f[x] for x in M}

def image_etendue(f, M):
    """Calcule l'image fermée par PGCD"""
    im_f = image_propre(f, M)
    return {y for y in M if any(pgcd(y, f[x]) in im_f for x in M)}

def generer_fonctions_valides(M):
    """Génère toutes les fonctions endomorphismes valides"""
    fonctions = []
    for f_vals in product(M, repeat=len(M)):
        f = dict(enumerate(f_vals))
        if f[0] == 0 and est_endomorphisme(f, M):
            fonctions.append(f)
    return fonctions

def analyser_fonctions(M):
    """Affiche l'analyse complète"""
    print("\nFonction".ljust(15), "Idempotent".ljust(12), "Image".ljust(15), "Image étendue".ljust(18), "i-régulier")
    print("-" * 65)
    
    for f in generer_fonctions_valides(M):
        f_tuple = tuple(f[i] for i in sorted(M))
        im = image_propre(f, M)
        im_et = image_etendue(f, M)
        
        ligne = f"{str(f_tuple).ljust(15)} | "
        ligne += f"{'Oui' if est_idempotent(f, M) else 'Non'.ljust(10)} | "
        ligne += f"{str(im).ljust(13)} | "
        ligne += f"{str(im_et).ljust(16)} | "
        ligne += "Oui" if im != im_et else "Non"
        
        print(ligne)

# Définir n directement ici (pas de input())
n = 2  # Changer cette valeur selon le besoin
M = list(range(n + 1))
analyser_fonctions(M)