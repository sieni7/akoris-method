# Décision 007 — Pas de no-go formel en A

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

`no-go` formel **uniquement dans C**. En A et B : `go` ou rien.

## Règles

- Onglet A : `go` ou ne rien taper.
- Onglet B : `go` ou ne rien taper.
- Si le Validator refuse un plan en A, il **ne tape rien** (blocage implicite).
- `no-go` est réservé au verdict post-audit (C).

## Justification

- `no-go` est un **jugement** : il n'a de sens qu'après l'audit.
- En A/B, il n'y a **rien à juger** : juste à autoriser.
- Évite la confusion "autorisation vs jugement".

## Alternatives écartées

- **no-go partout** : mélange autorisation et jugement.
- **no-go en A uniquement** : asymétrie inutile.
- **Pas de no-go du tout** : perte de l'outil de refus.
