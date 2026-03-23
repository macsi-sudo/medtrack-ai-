# medtrack-ai-
print("=== MedTrack AI ===")

# Entrée des données
name = input("Nom du patient : ")
mobility = int(input("Score de mobilité (0-10) : "))
memory = int(input("Score de mémoire (0-10) : "))
fatigue = int(input("Niveau de fatigue (0-10) : "))

# Analyse
score = (mobility + memory) - fatigue

# Résultat
print("\n--- Analyse ---")

if score > 10:
    print(f"{name} progresse très bien.")
elif score > 5:
    print(f"{name} montre une amélioration modérée.")
else:
    print(f"{name} nécessite un suivi renforcé.")
