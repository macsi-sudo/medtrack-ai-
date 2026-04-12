"""
====================================================
  MedTrack AI — Suivi Intelligent du Patient
  Auteure : Macouta Sissoko
  Formation : Bachelor Informatique & Santé — ISEP Paris
  GitHub : github.com/macsi-sudo/medtrack-ai-
====================================================
"""
 
 
SCORE_MIN = 0
SCORE_MAX = 10
 
def afficher_banniere():
    print("=" * 45)
    print("         MedTrack AI  ")
    print("   Suivi Intelligent du Patient")
    print("=" * 45)
    print()
 
 
def saisir_score(message):
    """Demande un score entre 0 et 10 et valide la saisie."""
    while True:
        try:
            valeur = int(input(f"  {message} (0-10) : "))
            if SCORE_MIN <= valeur <= SCORE_MAX:
                return valeur
            else:
                print("  Veuillez entrer une valeur entre 0 et 10.\n")
        except ValueError:
            print("   Valeur invalide. Entrez un nombre entier.\n")
 
 
def calculer_score(mobilite, memoire, fatigue):
    """Calcule le score global de progression du patient."""
    return (mobilite + memoire) - fatigue
 
 
def interpreter_score(score, nom):
    """Interprète le score et retourne une recommandation médicale."""
    print()
    print("-" * 45)
    print(f"   Analyse de {nom}")
    print("-" * 45)
    print(f"  Score global : {score}/20")
    print()
 
    if score > 10:
        print(f"   {nom} progresse très bien.")
        print("  → Continuer le suivi habituel.")
    elif score > 5:
        print(f"   {nom} montre une amélioration modérée.")
        print("  → Renforcer les exercices de rééducation.")
    else:
        print(f"   {nom} nécessite un suivi renforcé.")
        print("  → Consulter l'équipe médicale rapidement.")
 
    print("-" * 45)
 
 
def afficher_detail(mobilite, memoire, fatigue):
    """Affiche le détail des indicateurs saisis."""
    print()
    print("   Détail des indicateurs :")
    print(f"     • Mobilité  : {mobilite}/10")
    print(f"     • Mémoire   : {memoire}/10")
    print(f"     • Fatigue   : {fatigue}/10  (indicateur inversé)")
 
 
def continuer():
    """Demande si l'utilisateur veut analyser un autre patient."""
    print()
    reponse = input("  Analyser un autre patient ? (o/n) : ").strip().lower()
    return reponse == "o"
 
 
# ─────────────────────────────────────────────────
# PROGRAMME PRINCIPAL
# ─────────────────────────────────────────────────
 
def main():
    afficher_banniere()
 
    while True:
        # Saisie du nom du patient
        print("  Informations patient")
        nom = input("  Nom du patient : ").strip()
 
        if not nom:
            nom = "Patient inconnu"
 
        print()
        print("  Évaluation clinique")
 
        # Saisie des indicateurs
        mobilite = saisir_score("Score de mobilité")
        memoire  = saisir_score("Score de mémoire ")
        fatigue  = saisir_score("Niveau de fatigue")
 
        # Affichage du détail
        afficher_detail(mobilite, memoire, fatigue)
 
        # Calcul et interprétation
        score = calculer_score(mobilite, memoire, fatigue)
        interpreter_score(score, nom)
 
        # Continuer ou quitter
        if not continuer():
            print()
            print("  Merci d'avoir utilisé MedTrack AI. 🏥")
            print("=" * 45)
            break
 
        print()
 
 
if __name__ == "__main__":
    main()
 
