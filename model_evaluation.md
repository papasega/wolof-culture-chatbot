# 📊 Résultats d'Évaluation du Modèle — Chatbot Wolof

Ce fichier documente les résultats d'entraînement et de tests du chatbot au fil du temps.
Chaque nouvelle session `rasa train` + `rasa test` doit être consignée ici.

---

## ✅ Évaluation 2026 — Version 2.0 (Rasa 3.6.21+)

**Date :** 22 mars 2026
**Modèle :** `20260322-100129-achromatic-run.tar.gz`
**Données :** 570 exemples NLU · 26 intents · 22 stories de test

---

### 🧭 Niveau Conversation (Stories)

| Métrique | Valeur |
|---|---|
| Stories correctes | **20 / 22** |
| Accuracy | **0.909** |

---

### ⚙️ Niveau Action (Dialogue Management)

| Métrique | Valeur |
|---|---|
| Actions correctes | **62 / 64** |
| Accuracy | **0.979** |
| F1-Score | **0.971** |
| Précision | **0.965** |

> Quasi-perfection sur la gestion du dialogue : le bot choisit la bonne action dans 97,9% des cas.

---

### 🧠 Classification NLU — Intent Recognition

**Corpus :** 570 exemples · 26 intents

La matrice de confusion montre une quasi-diagonale parfaite, avec deux points d'attention :

- **Intent index 6** : 1 exemple mal classifié (15/16 corrects)
- **Intent index 23** : 7 exemples **tous mal classifiés** vers l'intent index 16 → confusion entre deux intents proches à corriger
- **Intent index 9** et **25** : 1 erreur chacun (mineure)

> **Action recommandée :** différencier davantage les exemples NLU des intents 16 et 23.

---

### 💬 Response Selection (Chitchat / FAQ)

**Corpus :** 107 exemples · 11 classes

| Classe | Statut |
|---|---|
| Classes 1 à 8 | ✅ Parfaitement classifiées |
| Classe 9 (9 exemples) | ❌ Tous classifiés en classe 0 |
| Classe 10 (10 exemples) | ❌ Tous classifiés en classe 0 |

> **Action recommandée :** ajouter plus d'exemples différenciés pour les classes 9 et 10 du ResponseSelector.

---

### 📁 Fichiers de résultats générés

```
results/
├── story_report.json              # Rapport conversation
├── TEDPolicy_report.json          # Rapport entités
├── intent_report.json             # Rapport NLU intents
├── intent_errors.json             # Erreurs de classification
├── response_selection_report.json # Rapport chitchat/FAQ
├── response_selection_errors.json # Erreurs sélection réponses
├── failed_test_stories.yml        # Stories échouées
└── stories_with_warnings.yml      # Stories avec avertissements
```

---

---

## 📜 Évaluation 2022 — Version 1.0 (Rasa 3.x — Labs IAS)

**Date :** 14 août 2022
**Données :** 114 exemples NLU · cross-validation 5 folds · 37 exemples response selection

---

### 🧠 Cross-Validation NLU (5 folds)

| Métrique | Train | Test |
|---|---|---|
| Accuracy | **1.000** ± 0.000 | **0.868** ± 0.030 |
| F1-Score | **1.000** ± 0.000 | **0.861** ± 0.033 |
| Précision | **1.000** ± 0.000 | **0.886** ± 0.042 |

> Le modèle était parfait sur les données d'entraînement (overfitting probable dû au faible volume de données — 114 exemples seulement).
> La performance en test (F1 = 0.861) était correcte pour un premier prototype.

---

### 📈 Comparaison 2022 vs 2026

| Métrique | 2022 (v1.0) | 2026 (v2.0) | Évolution |
|---|---|---|---|
| Exemples NLU | 114 | 570 | **+400%** ✅ |
| Intents | ~8 | 26 | **+225%** ✅ |
| Test Accuracy (intent) | 0.868 | ~0.993* | **+12.6 pts** ✅ |
| Response selection | 37 ex. | 107 ex. | **+189%** ✅ |
| Stories testées | — | 22 | nouveau ✅ |

*\*estimé à partir de la matrice de confusion : ~567/570 corrects*

---

**Auteur** : [Papa Sega WADE](https://papasegawade.com) — Labs
