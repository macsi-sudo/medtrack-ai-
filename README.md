# 🏥 MedTrack AI — Suivi Intelligent du Patient

> Projet personnel réalisé dans le cadre du Bachelor Informatique & Santé à l'ISEP Paris
> **Macouta Sissoko** · [linkedin.com/in/macoutasissoko](https://linkedin.com/in/macoutasissoko) · [github.com/macsi-sudo/medtrack-ai-](https://github.com/macsi-sudo/medtrack-ai-)


##  Description du projet

**MedTrack AI** est un programme Python de suivi médical intelligent qui analyse l'état de santé d'un patient à partir de trois indicateurs cliniques clés : la **mobilité**, la **mémoire** et la **fatigue**.

L'objectif est d'aider les soignants à identifier rapidement les patients qui nécessitent un suivi renforcé, grâce à un algorithme de scoring automatique simple et efficace.


## Objectifs

- Évaluer l'état de santé d'un patient en temps réel via une saisie interactive
- Calculer un score global de progression basé sur des indicateurs médicaux
- Générer une recommandation automatique de prise en charge
- Démontrer l'application concrète du Python dans le domaine de la santé numérique



## Fonctionnement

Le programme demande à l'utilisateur de saisir :

| Indicateur         |  Échelle       |    Description |
| Score de mobilité | 0 à 10 | Capacité physique du patient |
| Score de mémoire | 0 à 10 | Fonctions cognitives |
| Niveau de fatigue | 0 à 10 | Fatigue ressentie (inversé dans le score) |

**Formule de calcul :
Score global = (mobilité + mémoire) - fatigue

**Interprétation du score :**
- Score > 10 →  Le patient progresse très bien
- Score > 5  →  Amélioration modérée, à surveiller
- Score ≤ 5  →  Suivi renforcé nécessaire

## Lancer le programme

### Prérequis
Python 3.x installé sur votre machine

### Installation & exécution
git clone https://github.com/macsi-sudo/medtrack-ai-.git
cd medtrack-ai-
python medtrack_ai.py

### Exemple d'utilisation
=== MedTrack AI ===
Nom du patient : Marie Dupont
Score de mobilité (0-10) : 8
Score de mémoire (0-10) : 7
Niveau de fatigue (0-10) : 3

 
 Analyse 
Marie Dupont progresse très bien.
Score global : 12/20


## Compétences mobilisées

- **Python** : saisie utilisateur, conditions, logique algorithmique
- **Santé numérique** : compréhension des indicateurs médicaux
- **Documentation technique** : rédaction de README professionnel
- **GitHub** : versioning et mise en ligne autonome

## Auteure

**Macouta Sissoko**
Étudiante en Bachelor Informatique & Santé — ISEP Paris
Recherche une alternance à partir de septembre 2026 en santé numérique

[![LinkedIn](https://img.shields.io/badge/LinkedIn-macoutasissoko-blue?logo=linkedin)](https://linkedin.com/in/macoutasissoko)
[![GitHub](https://img.shields.io/badge/GitHub-macsi--sudo-black?logo=github)](https://github.com/macsi-sudo)


## Licence

Projet open source — libre d'utilisation à des fins éducatives.
```
