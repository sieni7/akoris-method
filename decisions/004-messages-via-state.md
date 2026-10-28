# Décision 004 — Messages inter-onglets via state.md

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Les messages entre agents (et vers le Validator) passent par le champ `message` de `state.md`. Pas de communication LLM-directe.

## Règles

- Chaque agent écrit `message: "<texte>"` dans `state.md` en fin de tour.
- Le Validator lit ce message dans l'UI (ou dans le fichier).
- Pas de "chat" entre agents : tout passe par `state.md`.

## Justification

- Traçabilité complète (le message est dans un fichier versionné).
- Pas de communication non contrôlée entre LLM.
- Le Validator voit tout.

## Alternatives écartées

- **Chat inter-onglets** : non contrôlé, volatile.
- **API directe entre LLM** : complexe, risqué.
- **Copier-coller manuel** : casse le flux.
