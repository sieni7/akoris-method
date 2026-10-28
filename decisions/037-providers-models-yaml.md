# Décision 037 — Configuration des providers (models.yaml)

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

La configuration des providers/modèles par onglet est centralisée dans `.akoris/config/models.yaml`, versionné et reproductible.

## Règles

### Format

```yaml
orchestrator:
  provider: glm
  model: glm-5.3-flash
  fallback: [deepseek-v4-flash]
builder:
  provider: deepseek
  model: deepseek-v4-flash
  fallback: [big-pickle]
auditor:
  provider: nvidia
  model: nemotron-3-super
  fallback: [glm-5.3-flash]
```

### Diversité recommandée

- **Builder ≠ Auditor** (providers ou modèles différents).
- Recommandé par défaut, vérifié par `akoris doctor` (V2).
- Si mono-provider (contrainte matérielle), documenter comme dette (DT-XXX).

### Fallback

- Chaque onglet a une liste de fallback ordonnée.
- Si le provider principal est down, l'adapter bascule automatiquement (V2).

### V1 vs V2

- V1 : config manuelle dans chaque onglet (permis, non tracé).
- V2 : `models.yaml` versionné, tracé, vérifié.

## Justification

- **Reproductibilité** : la config est versionnée, un nouveau projet la copie.
- **Traçabilité** : on sait quel modèle a produit quoi.
- **Diversité** : évite la corrélation des erreurs (reviewer).
- **Fallback** : résilience si un provider tombe.

## Alternatives écartées

- **Config manuelle par onglet** : pas de trace, pas de reproductibilité.
- **Mono-provider imposé** : perte de la diversité, biais partagé.
- **Config dans `contexte.md`** : mélange gouvernance et config.
