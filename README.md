# AKORIS

**Adaptive Knowledge & Orchestrated Review for Iterative Systems**

> L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.

AKORIS est une méthode de gouvernance du développement logiciel assisté par
intelligence artificielle. Elle vise trois zéros : zéro hallucination, zéro code
spaghetti, zéro dette technique non maîtrisée — **visés, mesurés, tracés**.

---

## Les 3 noms d'AKORIS

| Nom | Quoi | Où |
|-----|------|-----|
| **akoris-method** | Le référentiel de la méthode (générique) | Ce repo |
| **.akoris/** | L'instance de la méthode dans un projet (spécifique) | Dans chaque projet |
| **akoris CLI** | L'outil (V1, npm, `npx akoris`) | Package npm |

```
akoris-method/  (référentiel — générique)
        │
        │  scripts/init-project.sh
        ▼
   .akoris/  (instance — spécifique au projet)
        │
        │  outil
        ▼
   akoris CLI  (V1)
```

**Règle :** `akoris-method/` est **le modèle**. `.akoris/` est **l'instance**.
Le projet n'a **pas besoin** de `akoris-method/` pour fonctionner — il a seulement
`.akoris/`, copié depuis `templates/`.

---

## Démarrage rapide

1. Cloner ce repo (ou le garder à côté)
2. Lancer `scripts/init-project.sh <nom-du-projet>`
3. Adapter `.akoris/projet.md` (stack, règles métier)
4. Suivre `checklists/phase-0.md`
5. Lancer le bootstrap : `.akoris/config/bootstrap.md`

---

## Documentation

- **Le livre :** `docs/` (9 parties, 34 chapitres)
- **Les décisions :** `decisions/` (48 décisions figées)
- **Les templates :** `templates/.akoris/` (à copier)
- **Les checklists :** `checklists/` (phase 0, bootstrap, sprint, verdict, clôture)
- **Les scripts :** `scripts/` (init, build-debt-index, validate)
- **Les exemples :** `examples/` (MVP, SaaS)

---

## Structure du repo

```
akoris-method/
├── README.md
├── METHOD.md
├── CHANGELOG.md
├── docs/                  ← le livre
├── templates/.akoris/     ← à copier dans un projet
├── checklists/            ← à suivre
├── decisions/             ← les décisions figées
├── scripts/               ← init, build-debt-index, validate
└── examples/              ← exemples fictifs
```

---

## Principes fondateurs

1. Séparation des pouvoirs (produire / vérifier / décider)
2. Une seule source de vérité
3. Un agent à la fois
4. Traçabilité par défaut
5. Réplicabilité

---

## Positionnement

AKORIS n'est :
- ni un modèle d'intelligence artificielle ;
- ni un éditeur de code ;
- ni un framework de programmation ;
- ni un simple ensemble de prompts.

C'est une méthode de gouvernance, indépendante des modèles, des fournisseurs et
des outils de développement utilisés.

---

## Licence

- Code : MIT
- Livre : CC-BY-4.0
- Méthode : Apache-2.0

Voir le fichier LICENSE.
