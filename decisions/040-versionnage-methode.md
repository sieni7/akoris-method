# Décision 040 — Versionnage de la méthode dans l'instance

- **Statut :** V2 / non implémentée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

Chaque instance `.akoris/` note la **version de la méthode** dont elle est issue dans `.akoris/method-version.md`.

## Règles

### Format

```yaml
method:
  version: 0.1.1
  commit: <hash-du-repo-akoris-method>
  installed_at: <YYYY-MM-DD>
  profile: standard
```

### Migration

- `akoris upgrade` (V2) migre d'une version à l'autre.
- `akoris-method/CHANGELOG.md` liste les breaking changes et migrations.
- ADR obligatoire pour tout MAJOR de la méthode.

### Vérification

- `akoris doctor` (V2) signale si la version de l'instance est obsolète.
- Pas de blocage automatique (le Validator décide).

## Justification

- **Reproductibilité** : on sait de quelle version vient l'instance.
- **Migration** : on peut migrer proprement.
- **Traçabilité** : l'historique de la méthode est préservé.

## Alternatives écartées

- **Pas de version** : on ne sait pas d'où vient l'instance.
- **Version dans `contexte.md`** : mélange gouvernance et version.
- **Version dans le nom du dossier** : fragile, non standard.
