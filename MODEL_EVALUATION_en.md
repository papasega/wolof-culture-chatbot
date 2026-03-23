# 📊 Model Evaluation Results: Chatbot Wolof

This file documents the chatbot's training and testing results over time.
Every new `rasa train` + `rasa test` session should be recorded here.

---

## ✅ Evaluation 2026: Version 2.0 (Rasa 3.6.21+)

**Date:** March 23, 2026
**Data:** 632 NLU examples · 29 intents · 22 test stories

---

### 🧭 Conversation Level (Stories)

| Metric | Value |
| --- | --- |
| Correct stories | **20 / 22** |
| Accuracy | **0.909** |

---

### ⚙️ Action Level (Dialogue Management)

| Metric | Value |
| --- | --- |
| Correct actions | **62 / 64** |
| Accuracy | **0.979** |
| F1-Score | **0.971** |
| Precision | **0.965** |

> Near-perfect dialogue management: the bot chooses the correct action in 97.9% of cases.

---

### 🧠 NLU Classification: Intent Recognition

**Corpus:** 632 examples · 29 intents

The confusion matrix shows a near-perfect diagonal with an overall accuracy of **98.3%** (621/632 correct examples). Some minor attention points:

- **nlu_fallback**: 7 examples misclassified into `mood_great`, `ask_teranga`, and `bot_challenge`. This is expected as fallback testing can be tricky.
- **ask_education**: 1 confusion with `ask_religion`.
- **faq**: 1 confusion with `bot_challenge`.
- **ask_help**: 1 confusion with `faq`.

> **Recommended action:** Review the fallback thresholds and slightly diversify the examples for `ask_education` and `faq`.

---

### 💬 Response Selection (Chitchat / FAQ)

**Corpus:** 107 examples · 11 classes

| Class | Status |
| --- | --- |
| Classes 1 to 8 | ✅ Perfectly classified |
| Class 9 (9 examples) | ❌ All classified as class 0 |
| Class 10 (10 examples) | ❌ All classified as class 0 |

> **Recommended action:** Add more distinct examples for response selector classes 9 and 10 to avoid overlap.

---

### 📁 Generated Result Files

```text
results/
├── story_report.json              # Conversation report
├── TEDPolicy_report.json          # Entities report
├── intent_report.json             # NLU intents report
├── intent_errors.json             # Classification errors
├── response_selection_report.json # Chitchat/FAQ report
├── response_selection_errors.json # Response selection errors
├── failed_test_stories.yml        # Failed stories
└── stories_with_warnings.yml      # Stories with warnings
```

---

## 📜 Evaluation 2022: Version 1.0 (Rasa 3.x, Labs IAS)

**Date:** August 14, 2022
**Data:** 114 NLU examples · 5 folds cross-validation · 37 response selection examples

---

### 🧠 NLU Cross-Validation (5 folds)

| Metric | Train | Test |
| --- | --- | --- |
| Accuracy | **1.000** ± 0.000 | **0.868** ± 0.030 |
| F1-Score | **1.000** ± 0.000 | **0.861** ± 0.033 |
| Precision | **1.000** ± 0.000 | **0.886** ± 0.042 |

> The model was perfect on the training data. This indicates probable overfitting due to the low volume of data (only 114 examples).
> The test performance (F1 = 0.861) was satisfactory for a first prototype.

---

### 📈 Comparison 2022 vs 2026

| Metric | 2022 (v1.0) | 2026 (v2.0) | Evolution |
| --- | --- | --- | --- |
| NLU Examples | 114 | 632 | **+454%** ✅ |
| Intents | ~8 | 29 | **+262%** ✅ |
| Test Accuracy (intent) | 0.868 | 0.983 | **+11.5 pts** ✅ |
| Response selection | 37 ex. | 107 ex. | **+189%** ✅ |
| Tested stories | N/A | 22 | new ✅ |

---

**Author**: [Papa Sega WADE](https://papasegawade.com), Labs
