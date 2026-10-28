# Décision 009 — Rôles des 3 agents + Validator

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Trois agents IA (Orchestrator, Builder, Auditor) + un humain (Validator). Séparation stricte des pouvoirs.

## Règles

| Agent | Onglet | Rôle | Ne fait PAS |
|-------|--------|------|-------------|
| Orchestrator | A | Planifie, découpe, propose | Coder, auditer, valider |
| Builder | B | Exécute, code, commit, push | Planifier, auditer, valider |
| Auditor | C | QA + SecOps, rapporte | Coder, corriger, valider |
| Validator | humain | Autorise, tranche, assume | Coder, auditer |

## Justification

- Celui qui code n'audite pas.
- Celui qui audite ne valide pas.
- Celui qui valide ne code pas.
- **La** condition de la gouvernance.

## Alternatives écartées

- **1 seul agent** : auto-validation, dérive.
- **2 agents** : fusion production/vérification.
- **Pas d'humain** : perte de l'autorité finale.
