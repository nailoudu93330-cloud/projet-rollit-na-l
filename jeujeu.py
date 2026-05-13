from fltk import *
import random

# ================== CONSTANTES =====================
H, L = 10, 8
TAILLE_CASE = 50
MARGE_X = 50
MARGE_Y = 60
TAILLE_RATELIER = 5
Couleurs = ["red", "green", "blue", "yellow", "orange", "magenta"]

# ================== VARIABLES =====================
cases_neutralisees = []
plateau = []
ratelier1, ratelier2 = [], []
score1, score2 = [0], [0]
joueur_actuel = 1
partie_finie = False
mode_de_jeu = 1 

# ================== LOGIQUE =====================
def creer_cases_neutralisees():
    cases=[]
    for y in range(H):
        ligne=[]
        nb = random.randint(1,2)
        while len(ligne)<nb:
            x=random.randint(0,L-1)
            if x not in ligne:
                ligne.append(x)
        cases.append(ligne)
    return cases

def creer_plateau():
    p = []
    for y in range(H):
        ligne = []
        for x in range(L):
            if x in cases_neutralisees[y]:
                ligne.append(None)
            else:
                ligne.append(random.choice(Couleurs))
        p.append(ligne)
    for x in range(L):
        if p[0][x] is not None:
            p[0][x] = p[0][x].upper()
    return p

def retourner(j):
    if j is None: return None
    return j.upper() if j.islower() else j

def retourner_voisins(plateau, y, x):
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < H and 0 <= nx < L:
            plateau[ny][nx] = retourner(plateau[ny][nx])

def score_ratelier(ratelier, couleur):
    points = 0
    if ratelier.count(couleur) >= 3:
        for _ in range(3):
            ratelier.remove(couleur)
        points = 2 if len(ratelier) >= TAILLE_RATELIER else 1
    return points

def capturer(plateau, y, x, ratelier, score_list):
    global partie_finie
    j = plateau[y][x]
    if j is None or j.islower() or len(ratelier) >= TAILLE_RATELIER or partie_finie:
        return False
    plateau[y][x] = None
    couleur = j.lower()
    ratelier.append(couleur)
    score_list[0] += score_ratelier(ratelier, couleur)
    retourner_voisins(plateau, y, x)
    if len(ratelier) >= TAILLE_RATELIER:
        partie_finie = True
    return True

# ================== DESSIN =====================
def dessiner():
    efface_tout()
    rectangle(-10, -10, 1010, 1010, remplissage="white")

    # Plateau
    for y in range(H):
        for x in range(L):
            x0, y0 = MARGE_X + x*TAILLE_CASE, MARGE_Y + y*TAILLE_CASE
            j = plateau[y][x]
            rectangle(x0, y0, x0+TAILLE_CASE, y0+TAILLE_CASE, remplissage="lightgrey")
            if j is not None:
                cx, cy, r = x0 + TAILLE_CASE//2, y0 + TAILLE_CASE//2, TAILLE_CASE//2 - 4
                if j.islower():
                    cercle(cx, cy, r, couleur="black", remplissage="lightgrey")
                    cercle(cx, cy, r // 2, couleur=j, remplissage=j)
                else:
                    cercle(cx, cy, r, couleur=j, remplissage=j)

    # Râtelier 1
    texte(MARGE_X, MARGE_Y + H*TAILLE_CASE + 10, "Râtelier J1 :", taille=12)
    for i in range(TAILLE_RATELIER):
        rx = MARGE_X + i*50
        ry = MARGE_Y + H*TAILLE_CASE + 30
        rectangle(rx, ry, rx+40, ry+40, remplissage="#E0E0E0")
        if i < len(ratelier1):
            cercle(rx+20, ry+20, 15, couleur=ratelier1[i], remplissage=ratelier1[i])

    # Râtelier 2 (affiché seulement en multi)
    if mode_de_jeu == 2:
        texte(MARGE_X, MARGE_Y + H*TAILLE_CASE + 80, "Râtelier J2 :", taille=12)
        for i in range(TAILLE_RATELIER):
            rx = MARGE_X + i*50
            ry = MARGE_Y + H*TAILLE_CASE + 100
            rectangle(rx, ry, rx+40, ry+40, remplissage="#E0E0E0")
            if i < len(ratelier2):
                cercle(rx+20, ry+20, 15, couleur=ratelier2[i], remplissage=ratelier2[i])

    # Infos
    texte(20, 10, f"Score J1: {score1[0]}", taille=14)
    if mode_de_jeu == 2:
        texte(150, 10, f"Score J2: {score2[0]}", taille=14)
        couleur_tour = "red" if joueur_actuel == 1 else "blue"
        texte(350, 10, f"Tour: Joueur {joueur_actuel}", couleur=couleur_tour, taille=14)
    
    if partie_finie:
        texte(200, 300, "PARTIE TERMINÉE", couleur="red", taille=30)
    
    mise_a_jour()

# ================== MAIN =====================
cases_neutralisees = creer_cases_neutralisees()
plateau = creer_plateau()

cree_fenetre(500, 800)

# Menu de démarrage
rectangle(0,0,500,800, remplissage="white")
texte(50, 350, "Appuyez sur 1 pour SOLO\nou 2 pour MULTI", taille=20)
mise_a_jour()

while True:
    ev = attend_ev()
    if type_ev(ev) == "Touche":
        t = touche(ev)
        if t == "1": mode_de_jeu = 1; break
        if t == "2": mode_de_jeu = 2; break
    if type_ev(ev) == "Quitte": ferme_fenetre(); exit()

# Boucle de jeu
while True:
    dessiner()
    ev = donne_ev()
    if ev is not None:
        if type_ev(ev) == "Quitte":
            break
        if type_ev(ev) == "ClicGauche":
            gx = (abscisse(ev) - MARGE_X) // TAILLE_CASE
            gy = (ordonnee(ev) - MARGE_Y) // TAILLE_CASE
            if 0 <= gx < L and 0 <= gy < H:
                if mode_de_jeu == 1:
                    capturer(plateau, gy, gx, ratelier1, score1)
                else:
                    target_rat = ratelier1 if joueur_actuel == 1 else ratelier2
                    target_score = score1 if joueur_actuel == 1 else score2
                    if capturer(plateau, gy, gx, target_rat, target_score):
                        joueur_actuel = 2 if joueur_actuel == 1 else 1
    attente(0.01)

ferme_fenetre()