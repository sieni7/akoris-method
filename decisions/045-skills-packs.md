# Décision 045 — Skills Packs

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

Les **Skills Packs** sont des ensembles de règles, outils et seuils spécifiques à un domaine, chargés en plus de la méthode générique.

## Règles

### Dimensions d'un Skill Pack

| Dimension | Contenu |
|-----------|---------|
| **Outils** | Linters, scanners, frameworks de test |
| **Seuils** | Couverture min, complexité max, taille max |
| **Règles** | Architecture, patterns, anti-patterns |
| **Preuves** | Sorties attendues, formats de log |

### Liste V2

| Skill Pack | Domaine | Outils principaux |
|------------|---------|-------------------|
| `web-frontend` | React, Vue, Svelte | Vitest, Playwright, ESLint, a11y |
| `web-backend` | Node, Python, Go | Jest/Pytest, semgrep, pip-audit/npm audit |
| `data-ml` | Python, pandas, PyTorch | Pytest, great-expectations, dvc |
| `mobile` | React Native, Flutter | Jest, Detox, mobsf |
| `embedded` | C, Rust | cppcheck, clang-tidy, MISRA |
| `security` | Tous | gitleaks, semgrep, trivy, osv-scanner |

### Mécanique

- Choix au bootstrap (`skills.yaml`) :
  ```yaml
  skills:
    - web-backend
    - security
  ```
- Chargés par l'Auditor/Builder, appliqués dans les verdicts.
- AKORIS sans Skill Pack fonctionne (générique).
- AKORIS avec est plus précis.

### Skills Packs comme produits dérivés

- Chaque pilote **crée** son Skill Pack.
- Les Skill Packs ne sont pas inventés à l'avance, ils sont **extraits** de l'expérience réelle.

## Justification

- **Précision** : AKORIS générique est vague ; les packs le rendent précis.
- **Réplicabilité** : un pack se copie sur un autre projet du même domaine.
- **Indépendance** : les packs sont optionnels, la méthode reste générique.

## Alternatives écartées

- **Pas de Skills Packs** : AKORIS reste vague.
- **Skills Packs obligatoires** : complexité inutile.
- **Skills Packs dans le core** : mélange générique et spécifique.
