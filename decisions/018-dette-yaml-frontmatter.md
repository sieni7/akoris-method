# Décision 018 — Format dette : YAML frontmatter

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 4 (gouvernance)

---

## Décision

Chaque dette utilise un **YAML frontmatter** (11 champs) + prose Markdown.

## Règles

- 11 champs obligatoires : `id`, `titre`, `priorite`, `statut`, `sprint_origine`, `decision_origine`, `adr_lie`, `risque`, `impact`, `sprint_resorption_prevu`, `cree_le`.
- Valeurs autorisées : `priorite ∈ {P0,P1,P2,P3}`, `statut ∈ {ouverte,en_cours,resorbee,acceptee_definitivement}`, `impact ∈ {faible,moyen,eleve,critique}`.
- Le script `build-debt-index.py` **rejette** une dette hors schéma.
- Sections : Contexte, Plan de résorption, Preuves, Historique.

## Justification

- **Parsable sans regex fragile** (pyyaml).
- **Validable** par un schéma.
- **Standard** (Jekyll, Hugo, Obsidian).

## Alternatives écartées

- **Markdown pur** : parsing fragile.
- **JSON** : moins lisible en Markdown.
- **Sans validation** : dette mal formée = index faux.
