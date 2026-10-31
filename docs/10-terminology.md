# Terminologie AKORIS

> Ce document est le référentiel officiel du vocabulaire AKORIS v1.
> Il vise à éliminer les ambiguïtés entre le Validator (humain) et les agents (LLM).

## 1. Les Acteurs

| Terme | Définition |
| :--- | :--- |
| **Validator** | L'humain (toi). L'autorité souveraine. Il autorise, tranche et assume la responsabilité finale. |
| **Orchestrator** | L'agent IA (Onglet A). Il planifie, découpe et coordonne. Il ne code pas. |
| **Builder** | L'agent IA (Onglet B). Il exécute, code, commit et push. Il ne planifie pas. |
| **Auditor** | L'agent IA (Onglet C). Il contrôle, teste et rapporte. Il ne code pas. |

## 2. Les Signaux et Verdicts

| Terme | Définition |
| :--- | :--- |
| **GO** | Mot-clé de déclenchement. Le Validator tape `go` pour autoriser un agent à travailler. |
| **go with reserve** | Verdict de validation partielle. Le Validator accepte le travail mais ouvre une dette technique. |
| **no-go** | Verdict de refus. Le Validator rejette le travail, l'Orchestrator doit re-planifier. |
| **go force-unlock** | Commande d'urgence. Le Validator libère un verrou orphelin (`locked_by`). |

## 3. La Gouvernance et l'État

| Terme | Définition |
| :--- | :--- |
| **state.md** | Le bus de contrôle. Fichier unique qui contient l'état du projet, le verrou et les verdicts. |
| **locked_by** | Le verrou. Indique quel agent a la main (un seul à la fois). |
| **next_agent** | Le prochain agent à agir (défini par `state.md`). |
| **action** | L'action attendue (`go`, `idle`, `review`, `push`, etc.). |
| **phase** | L'étape du sprint (`plan`, `execution`, `audit`, `review`, `closed`). |
| **ADR** | Architecture Decision Record. Un document immuable qui trace une décision d'architecture. |
| **DT** | Dette Technique. Un compromis assumé, tracé et suivi. |
| **Bloc / Lot** | Une unité de travail pour corriger ou faire évoluer la méthode AKORIS elle-même. |

## 4. Les Standards et Prompts

| Terme | Définition |
| :--- | :--- |
| **SPA** | Standard de Prompt AKORIS. La norme (13 rubriques) qui régit tous les prompts. |
| **SPA-TEMPLATE** | Le moule vierge du SPA (avec les crochets `[À renseigner]`). |
| **SPA-INSTANCE** | Un prompt concret construit à partir du template (ex: Générateur de Contexte). |

## 5. La Qualité et les Tests

| Terme | Définition |
| :--- | :--- |
| **TNR** | Tests de Non-Régression. La base obligatoire de la qualité (unit + integration). |
| **UAT** | User Acceptance Test. Validation par le verdict du Validator. |
| **E2E** | End-to-End. Tests de parcours complet. |
| **SecOps** | Le checkpoint de sécurité (déclenché aux sprints marqués `🔒`). |
| **Quality Gate** | Un point de contrôle obligatoire (critères d'entrée, sortie, preuves). |
| **Playbook** | Une procédure standardisée (pré-conditions, rollback, etc.). |

## 6. Git et Processus

| Terme | Définition |
| :--- | :--- |
| **Conventional Commits** | Le format standard des messages de commit (`feat:`, `fix:`, etc.). |
| **DCO** | Developer Certificate of Origin. La signature (`Signed-off-by`) obligatoire. |
| **SemVer** | Le versionnage sémantique (`vMAJOR.MINOR.PATCH`). |

## 7. Skills Packs (Compétences)

- **Compétence (Skill)** : Savoir-faire métier (ex: QA-01 Code Reviewer) stocké dans `templates/skills/`. N'a pas de rôle de gouvernance.
- **Activation** : Instance SPA qui mobilise une compétence dans un rôle spécifique (ex: Auditor) pour une mission donnée. Stockée dans `.akoris/activations/`.

---
