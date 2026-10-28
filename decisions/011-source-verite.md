# Décision 011 — Source de vérité unique

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Les fichiers du dossier `.akoris/` sont **la** source de vérité, pas le chat.

## Règles

- Toute décision, tout état, toute dette, tout ADR est dans `.akoris/`.
- Le chat (LLM) est volatile : il n'est **pas** une source de vérité.
- Si divergence entre chat et fichiers → **les fichiers gagnent**.

## Justification

- Le chat se ferme, les fichiers restent.
- Traçabilité par défaut.
- Réplicabilité (les fichiers se copient).

## Alternatives écartées

- **Chat comme source** : volatile, non réplicable.
- **Base de données** : complexité inutile.
- **Mémoire de l'agent** : non fiable.
