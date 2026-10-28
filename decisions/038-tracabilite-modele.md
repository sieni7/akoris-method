# Décision 038 — Traçabilité du modèle dans les rapports

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

Chaque rapport d'audit mentionne **le provider et le modèle** qui a produit le travail audité, et **le modèle** qui a audité.

## Règles

- `audit_report.md` contient un en-tête :
  ```yaml
  audited_by:
    provider: nvidia
    model: nemotron-3-super
  produced_by:
    provider: deepseek
    model: deepseek-v4-flash
  ```
- Idem pour `audit_report-secops.md`.
- Si Builder et Auditor sont sur le **même** provider/modèle → signaler comme **dette** dans le rapport (corrélation).

## Justification

- **Traçabilité** : on sait qui a produit, qui a audité.
- **Détection de corrélation** : si même modèle, l'audit est moins fiable.
- **Reproductibilité** : on peut rejouer avec les mêmes modèles.

## Alternatives écartées

- **Pas de traçabilité** : on ne sait pas qui a fait quoi.
- **Traçabilité dans un fichier séparé** : complexité inutile.
- **Traçabilité dans `state.md`** : mélange état et audit.
