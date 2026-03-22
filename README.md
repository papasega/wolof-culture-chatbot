# 🇸🇳 Chatbot Wolof — Bot bu Wolof

Un chatbot conversationnel en **wolof** (avec support du code-switching wolof-français) construit avec [Rasa 3.x](https://rasa.com/).

Ce bot est conçu pour interagir en wolof sur des sujets liés à la **culture sénégalaise** : teranga, proverbes, cuisine, musique, sport, santé, éducation, religion, géographie, et plus encore.

## Fonctionnalités

- **30+ intents** couvrant la culture wolof, la vie quotidienne et les FAQ
- **Code-switching wolof-français** (ex: "bonjour na nga def", "c'est quoi le thiéboudiène ?")
- **Proverbes wolof** (lëbb) avec significations, générés aléatoirement
- **Fallback intelligent** quand le bot ne comprend pas
- **Réponses multiples** pour chaque intent (variété naturelle)
- **Thèmes culturels** : teranga, cosaan, njaboot, mbalax, ceebu jën, làmb...

## Intents principaux

| Intent | Description | Exemple |
|--------|-------------|---------|
| `greet` | Salutations | "na nga def", "salamlekum" |
| `ask_teranga` | Hospitalité wolof | "lan moy teranga ?" |
| `ask_proverb` | Proverbes wolof | "jox ma ab lëbb" |
| `ask_food` | Cuisine sénégalaise | "naka lañuy togg ceebu jën ?" |
| `ask_music` | Musique (mbalax) | "wax ma ci mbalax" |
| `ask_sport` | Sport (lutte, foot) | "wax ma ci làmb" |
| `ask_senegal` | Géographie Sénégal | "wax ma ci senegaal" |
| `ask_health` | Santé | "naka lañuy wara fey seen yaram ?" |
| `ask_education` | Éducation | "naka la jàngu yi di dem ?" |
| `ask_religion` | Religion | "wax ma ci diine ci senegaal" |
| `chitchat/*` | Conversation libre | "naka ngay jëm ?", "wax ma ab rëy" |

## Prérequis

- Python 3.8 - 3.10
- Rasa 3.x (`pip install rasa==3.6.20`)
- Rasa SDK (`pip install rasa-sdk`)

## Installation

```bash
# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# Installer les dépendances
pip install rasa==3.6.20 rasa-sdk

# Entraîner le modèle
rasa train

# Lancer le serveur d'actions (dans un terminal séparé)
rasa run actions

# Tester le bot en ligne de commande
rasa shell

# Ou tester via l'API REST
rasa run --enable-api --cors "*"
```

## Structure du projet

```
Chatbot_Wolof/
├── config.yml          # Pipeline NLU + policies (Rasa 3.x)
├── domain.yml          # Intents, entities, slots, responses, actions
├── data/
│   ├── nlu.yml         # Données d'entraînement NLU (wolof + code-switching)
│   ├── stories.yml     # Parcours conversationnels
│   └── rules.yml       # Règles de conversation
├── actions/
│   └── actions.py      # Custom actions (proverbes, fallback)
├── tests/
│   └── test_stories.yml # Tests end-to-end en wolof
├── endpoints.yml       # Configuration des endpoints
└── credentials.yml     # Canaux de communication
```

## Tester le bot

```bash
# Tests end-to-end
rasa test

# Évaluation NLU avec cross-validation
rasa test nlu --cross-validation

# Test interactif
rasa interactive
```

## Pipeline NLU

- `WhitespaceTokenizer` — Tokenisation par espaces (adapté au wolof)
- `RegexFeaturizer` — Features basées sur des regex
- `LexicalSyntacticFeaturizer` — Features lexicales et syntaxiques
- `CountVectorsFeaturizer` (word + char n-grams) — Robuste pour le wolof
- `DIETClassifier` — Classification d'intents et extraction d'entités
- `ResponseSelector` — Sélection de réponses FAQ et chitchat
- `FallbackClassifier` — Gestion des cas hors sujet

## Contribuer

Les contributions sont les bienvenues ! Vous pouvez :
- Ajouter plus d'exemples NLU en wolof
- Ajouter de nouveaux intents et thèmes
- Enrichir les proverbes dans `actions.py`
- Améliorer les réponses dans `domain.yml`
- Ajouter des exemples de code-switching

---

**Auteur** : [Papa Sega WADE](https://papasegawade.com) — IAS
