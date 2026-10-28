# Décision 026 — Auditor SecOps checkpoint

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

L'Auditor exerce un mandat **SecOps** aux sprints marqués **`🔒`** dans la roadmap (checkpoints sécurité).

## Règles

- Déclenché uniquement aux sprints `🔒`.
- Vérifie : secrets, injections, CVE, auth, surface d'attaque.
- Il écrit `audit_report-secops.md`.
- Deux tours distincts (QA puis SecOps) aux sprints `🔒`.
- **Preuve attendue (V1)** : le rapport cite les scanners exécutés (gitleaks, semgrep, pip-audit, npm audit) et leurs sorties (texte).
- **Preuve attendue (V2)** : le rapport attache les sorties verbatim et les IDs de run CI.

## Justification

- La sécurité n'est pas un audit continu : c'est un **checkpoint**.
- Aux moments structurants (avant prod, avant auth, avant API publique).
- Cadré par la roadmap (prévisible, pas improvisé).

## Alternatives écartées

- **SecOps permanent** : surcharge, findings superficiels.
- **Jamais de SecOps** : vulnérabilités non détectées.
- **SecOps par le Builder** : conflit d'intérêt.
- **SecOps déclaratif sans scanner** : contredit « zéro hallucination ».
