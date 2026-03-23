# 🇸🇳 Chatbot Wolof : Bot bu Wolof 2020-2023

🇬🇧 [Read this in English](./README_en.md)

Un chatbot conversationnel en **wolof** (avec support du code-switching wolof-français) construit avec [Rasa 3.x](https://rasa.com/).

Ce bot est conçu pour interagir en wolof sur des sujets liés à la **culture sénégalaise** : teranga, proverbes, cuisine, musique, sport, santé, éducation, religion, géographie, et plus encore.

![Chatbot Wolof](./assets/chatbo_wolof_psw.png)

## Qu'est-ce que Rasa ?

[Rasa](https://rasa.com/) est un framework open-source de construction de chatbots conversationnels. Il repose sur deux composants principaux :

- **Rasa NLU** *(Natural Language Understanding)* : comprend ce que dit l'utilisateur, il classifie l'**intention** (intent) et extrait les **entités** (mots clés importants).
- **Rasa Core** : gère le **dialogue**. Il décide quelle action ou réponse donner en fonction de l'historique de la conversation, via des stories, des règles et des policies.

Contrairement à un chatbot à règles pures (if/else), Rasa utilise du **machine learning supervisé** : il apprend à partir d'exemples annotés pour généraliser à de nouvelles formulations.

---

## Pourquoi ce chatbot est différent d'un LLM et pourquoi il est plus fiable

Un **LLM (Large Language Model)** comme GPT-4 ou Claude est un modèle **probabiliste** : il génère la réponse la plus probable selon son entraînement sur des milliards de textes. Cela le rend très fluide… mais aussi **imprévisible** :

- Il peut **halluciner** : inventer des faits culturels wolof qui n'existent pas
- Il peut **dériver** du sujet ou répondre hors contexte
- Il est **non déterministe** : deux appels identiques peuvent donner deux réponses différentes
- Il est difficile à **contrôler** et à **auditer** dans un cadre précis

Ce chatbot Rasa adopte une approche **déterministe et bornée** :

| Critère | Chatbot Rasa (ce projet) | LLM (GPT, Claude…) |
| --- | --- | --- |
| **Réponses** | Définies et validées manuellement | Générées probabilistiquement |
| **Fiabilité culturelle** | ✅ Chaque réponse est vérifiée | ⚠️ Risque d'hallucination |
| **Contrôle du dialogue** | ✅ Stories + règles explicites | ❌ Difficile à contraindre |
| **Déterminisme** | ✅ Comportement prévisible | ❌ Non-déterministe |
| **Coût d'inférence** | ✅ Léger, local, gratuit | ❌ API payante, latence |
| **Langue rare (wolof)** | ✅ Entraîné sur des données ciblées | ⚠️ Peu de données wolof dans l'entraînement |

> **Pour un domaine culturel spécifique comme le wolof**, il est préférable d'avoir un bot qui répond *juste mais limité* plutôt qu'un LLM qui répond *fluide mais potentiellement faux*.

---

## Fonctionnalités

- **30+ intents** couvrant la culture wolof, la vie quotidienne et les FAQ
- **Code-switching wolof-français** (ex: "bonjour na nga def", "c'est quoi le thiéboudiène ?")
- **Proverbes wolof** (lëbb) avec significations, générés aléatoirement
- **Fallback intelligent** quand le bot ne comprend pas
- **Réponses multiples** pour chaque intent (variété naturelle)
- **Thèmes culturels** : teranga, cosaan, njaboot, mbalax, ceebu jën, làmb...

## Intents principaux

| Intent | Description | Exemple |
| -------- | ------------- | --------- |
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

```text
wolof-culture-chatbot/
├── config.yml              # Pipeline NLU + policies (Rasa 3.x)
├── domain.yml              # Intents, entities, slots, responses, actions
├── data/
│   ├── nlu.yml             # Données d'entraînement NLU (wolof + code-switching)
│   ├── stories.yml         # Parcours conversationnels
│   └── rules.yml           # Règles de conversation
├── actions/
│   └── actions.py          # Custom actions (proverbes, fallback)
├── tests/
│   └── test_stories.yml    # Tests end-to-end en wolof
├── results/                # Rapports JSON générés par rasa test (non versionné)
├── model_evaluation.md     # Historique des résultats d'entraînement et de tests
├── endpoints.yml           # Configuration des endpoints
└── credentials.yml         # Canaux de communication
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

## Résultats d'évaluation

Les résultats complets d'entraînement et de tests (2022 → 2026) sont documentés dans [`model_evaluation.md`](./model_evaluation.md).

**Résumé des performances (mars 2026) :**

| Niveau | Métrique | Score |
| --- | --- | --- |
| Conversation (stories) | Accuracy | **90.9%**, 20/22 |
| Dialogue (actions) | Accuracy | **97.9%**, 62/64 |
| Dialogue (actions) | F1-Score | **0.971** |
| NLU Intent | ~Accuracy | **~99.3%**, 567/570 |

## Pipeline NLU

- `WhitespaceTokenizer` : Tokenisation par espaces (adapté au wolof)
- `RegexFeaturizer` : Features basées sur des regex
- `LexicalSyntacticFeaturizer` : Features lexicales et syntaxiques
- `CountVectorsFeaturizer` (word + char n-grams) : Robuste pour le wolof
- `DIETClassifier` : Classification d'intents et extraction d'entités
- `ResponseSelector` : Sélection de réponses FAQ et chitchat
- `FallbackClassifier` : Gestion des cas hors sujet

## Contribuer

Les contributions sont les bienvenues ! Vous pouvez :

- Ajouter plus d'exemples NLU en wolof
- Ajouter de nouveaux intents et thèmes
- Enrichir les proverbes dans `actions.py`
- Améliorer les réponses dans `domain.yml`
- Ajouter des exemples de code-switching

## Limitations du chatbot classique

Ce chatbot, comme tout système basé sur Rasa, présente des **limites inhérentes à l'approche supervisée classique** qu'il est important de connaître.

### 1. Dépendance totale aux données d'entraînement

Chaque intent, chaque cas d'usage, chaque formulation doit être **écrit manuellement** avec des exemples annotés. Si un utilisateur pose une question qui n'a pas été anticipée, le bot tombe en fallback. Il ne peut pas improviser ni généraliser hors de ce qui a été prévu.

> Plus le bot couvre de sujets, plus il faut de données. C'est un travail continu et coûteux.

### 2. Fragilité face aux nouvelles formulations

Le modèle apprend à reconnaître des patterns à partir des exemples fournis. Une formulation légèrement différente de ce qui a été vu à l'entraînement peut ne pas être reconnue, surtout dans une langue comme le wolof qui est **agglutinante** et peu normalisée à l'écrit.

### 3. Réponses statiques

Toutes les réponses sont définies dans `domain.yml`. Le bot ne peut pas **adapter son discours** au contexte réel de la conversation. Il sélectionne une réponse parmi celles prévues, sans les reformuler ni les enrichir dynamiquement.

### 4. Maintenance manuelle obligatoire

Chaque évolution du bot (nouveau sujet, nouvelle formulation, correction d'une réponse) nécessite une mise à jour des données, un **ré-entraînement complet** du modèle et des tests de non-régression. Il n'y a pas d'apprentissage automatique en production.

### 5. Pas de compréhension profonde du wolof

Le pipeline utilise `WhitespaceTokenizer`, un simple découpage par espaces. Il n'existe pas encore de **modèle de langue pré-entraîné en wolof** (comme BERT pour l'anglais ou CamemBERT pour le français), ce qui limite la compréhension sémantique fine de la langue.

---

## Pistes d'amélioration

Ces limitations ouvrent des axes de recherche concrets pour faire évoluer le projet :

### Axe 1 : Enrichissement des données

- Collecter et annoter un **corpus wolof** plus large et diversifié
- Couvrir davantage de dialectes et variantes régionales du wolof
- Intégrer plus d'exemples de code-switching wolof-français-anglais

### Axe 2 : Représentation linguistique (Recherche)

- Entraîner des **word embeddings wolof** (FastText) sur un grand corpus de textes wolof
- **Fine-tuner un modèle multilingue** (XLM-R, mBERT) sur des données wolof annotées pour une meilleure compréhension sémantique
- **Construire un corpus wolof annoté** (tâche NER, POS tagging) pour outiller la communauté NLP africaine

> Ces axes s'inscrivent dans la dynamique des initiatives comme [Masakhane](https://www.masakhane.io/) et [AfroNLP](https://afronlp.github.io/), qui travaillent à outiller les langues africaines en ressources NLP.

---

**Auteur** : [Papa Sega WADE](https://papasegawade.com), Labs
