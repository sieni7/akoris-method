# Décision 046 — Examples (3 cas d'usage)

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

`examples/` contient **3 cas d'usage réels**, du plus simple au plus complexe, un par profil.

## Règles

### Les 3 cas

| # | Cas | Complexité | Profil | Ce qu'il prouve |
|---|-----|------------|--------|-----------------|
| 01 | CLI tool | ★☆☆☆☆ | Lite | Squelette, state, sprint, dette |
| 02 | API REST | ★★★☆☆ | Standard | Auth, CI, tag v1.0.0, skill web-backend |
| 03 | SaaS | ★★★★★ | Strict | Profil Strict, sécu 🔒, multi-tenant, migration |

### Contenu de chaque exemple

```
examples/0N-<nom>/
├── README.md
├── app/                       ← code source complet
├── doc/                       ← doc technique + produit
├── .akoris/                   ← instance complète
├── METRICS.md                 ← durée, tokens, dettes, couverture
└── RETROSPECTIVE.md           ← ce qui a marché/cassé/surpris
```

### Timing

- V1.0 : `examples/` créé vide (README « à venir »).
- V1.1 : exemple 1 (pilote 1).
- V1.2 : exemple 2 (pilote 2).
- V1.3 : exemple 3 (pilote 3).
- V2.0 : synthèse + corrections.

## Justification

- **Preuve** : les exemples sont des projets réels, pas des tutoriels.
- **Progression** : simple → complexe, pédagogique.
- **Couverture** : les 3 profils sont testés.

## Alternatives écartées

- **Aucun exemple** : AKORIS n'est pas prouvé.
- **1 seul exemple** : pas de progression, pas de couverture des profils.
- **Exemples fictifs** : pas de preuve réelle.
