# AUDIT REPORT (SECOPS) — Sprint <NN> 🔒

> Rapport d'audit SecOps. Écrit par l'Auditor (onglet C), UNIQUEMENT aux sprints 🔒.
> Ne mélange JAMAIS QA et SecOps.

---

## Métadonnées

- **Sprint :** <NN> 🔒
- **Date :** <YYYY-MM-DD>
- **Auditeur :** Auditor SecOps
- **Branche :** sprint-<NN>
- **Commit audité :** <hash>

## Surface d'attaque

- **Endpoints exposés :** <N>
- **Auth :** <mécanisme>
- **Secrets :** <N> (aucun ne doit être en clair)

## Audit sécurité

| # | Catégorie | Sévérité | Localisation | Description | Suggestion |
|---|-----------|----------|--------------|-------------|------------|
| S1 | secrets | critique | <fichier:ligne> | <desc> | <suggestion> |
| S2 | injection | élevé | <fichier:ligne> | <desc> | <suggestion> |
| S3 | CVE | moyen | <dep> | <desc> | <suggestion> |
| S4 | auth | faible | <fichier:ligne> | <desc> | <suggestion> |

**Sévérités :** `critique` | `élevé` | `moyen` | `faible`

## Audit dépendances (CVE)

| Package | Version | CVE | Sévérité | Correctif |
|---------|---------|-----|----------|-----------|
| <pkg>   | <ver>   | CVE-XXXX-YYYY | élevé | <version> |

## Audit secrets

- **Secrets en clair :** <N> (0 attendu)
- **Fichiers .env :** <gitignore OK | ⚠️ exposé>
- **Clés API :** <OK | ⚠️>

## Audit auth

- **Mécanisme :** <description>
- **Failles :** <N>
- **Recommandations :** <…>

## Findings

| # | Sévérité | Description | Suggestion |
|---|----------|-------------|------------|
| S1 | critique | <desc> | <suggestion> |
| S2 | élevé | <desc> | <suggestion> |

**Règle :** 0 finding critique = `go` | 1+ critique = `no-go` (sécu bloquante)

## Recommandation de push

- **Verdict SecOps :** `go` | `go with reserve` | `no-go`
- **Justification :** <raison>
- **Dettes à ouvrir :** DT-NNN, DT-NNN
- **Recommandation push :** `push` | `push avec réserves` | `ne pas push`

## Message pour le Validator

<message synthétique>
