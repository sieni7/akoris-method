# Décision 043 — CLI — Commandes

- **Statut :** V2 / non implémentée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

Le CLI expose **4 familles de commandes** : lifecycle, workflow, gouvernance, qualité.

## Règles

### Famille 1 — Lifecycle

| Commande | Effet |
|----------|-------|
| `akoris init` | Scaffold un nouveau projet |
| `akoris upgrade` | Migre vers une nouvelle version de méthode |
| `akoris resume` | Reprend une session (recharge le contexte) |

### Famille 2 — Workflow

| Commande | Équivalent V1 |
|----------|---------------|
| `akoris go A` / `B` / `C` | taper `go` dans l'onglet |
| `akoris verdict go` | taper `go` (verdict) |
| `akoris verdict reserve "..."` | taper `go with reserve: ...` |
| `akoris verdict no-go "..."` | taper `no-go: ...` |
| `akoris state` | (nouveau) affiche l'état |
| `akoris doctor` | taper `doctor` |

### Famille 3 — Gouvernance

| Commande | Effet |
|----------|-------|
| `akoris debt` | Liste, ouvre, résout une dette |
| `akoris adr` | Liste, crée un ADR |
| `akoris sprint` | Status, close un sprint |
| `akoris roadmap` | Affiche la roadmap |

### Famille 4 — Qualité

| Commande | Effet |
|----------|-------|
| `akoris validate` | Vérifie la cohérence globale |
| `akoris validate-method` | Vérifie la cohérence des règles |
| `akoris attach-evidence` | Attache les preuves machine |
| `akoris measure-spaghetti` | Mesure complexité/couplage |

### Compatibilité V1

- V1 : les commandes restent dans le chat (`go`, `doctor`).
- V2 : le CLI ajoute le préfixe `akoris`.
- **V1 reste toujours possible** (taper dans le chat).

## Justification

- **Cohérence** : 4 familles, pas de commande orpheline.
- **Compatibilité** : V1 et V2 coexistent.
- **Traçabilité** : le CLI log les commandes dans `.akoris/logs/commands.log`.

## Alternatives écartées

- **Commandes en vrac** : pas de structure.
- **CLI qui remplace V1** : perte de la flexibilité du chat.
- **Pas de log** : pas de traçabilité.
