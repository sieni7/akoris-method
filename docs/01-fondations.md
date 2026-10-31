# Chapitre 1 — Les Fondations d'AKORIS

## 1. Le Paradoxe du « Vibe Coding »

Le développement assisté par IA, souvent qualifié de « Vibe Coding », promet une vélocité inédite et une accessibilité démocratique de la production logicielle. Cependant, cette approche comporte un piège majeur : l'accumulation invisible de dette technique, la génération d'hallucinations non détectées et la production de code spaghetti.

La conséquence est systématique : des projets qui s'effondrent sous leur propre poids après une phase de démonstration rapide, rendant la maintenance impossible, la traçabilité nulle et la confiance des parties prenantes rompue.

## 2. La Réponse AKORIS : Une Méthode, pas un Outil

AKORIS (Adaptive Knowledge & Orchestrated Review for Iterative Systems) n'est ni un modèle d'IA, ni un éditeur de code, ni un simple ensemble de prompts. C'est une **méthode de gouvernance**, indépendante des modèles, des fournisseurs et des outils.

- **Principe directeur** : L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.
- **Positionnement** : AKORIS impose un cadre pour transformer la capacité des LLM en ingénierie logicielle fiable, mesurable et pérenne, en remplaçant l'improvisation par des processus vérifiables.

## 3. Les 3 Boussoles (Les « 3 Zéros »)

AKORIS vise trois objectifs qui orientent la qualité et la pérennité du logiciel. Ils doivent être mesurés et tracés; ce sont des boussoles, non des garanties absolues :

1. **Zéro hallucination** : Toute affirmation, règle métier ou génération de code doit être vérifiable, testable et tracée. Rien n'est supposé; les éléments importants sont étayés par des tests ou des références explicites.
2. **Zéro code spaghetti** : L'architecture doit rester modulaire et lisible. Le respect des conventions de nommage, des scopes d'écriture et des principes d'architecture est essentiel.
3. **Zéro dette non maîtrisée** : Toute compromission — technique, fonctionnelle ou de sécurité — doit être explicitement enregistrée dans le registre des dettes, priorisée et planifiée pour résorption. L'objectif est qu'aucune dette ne soit oubliée.

## 4. Les 5 Principes Fondateurs

Ces principes structurent chaque interaction entre les agents et le Validator :

- **Principe 1 : Séparation des pouvoirs.** Celui qui code n'audite pas, celui qui audite ne valide pas, celui qui valide ne code pas. Cette indépendance garantit l'objectivité du contrôle et empêche l'auto-validation.
- **Principe 2 : Gouvernance par l'écrit.** Tout état, décision (ADR) ou dette réside dans le répertoire `.akoris/`. La mémoire éphémère du chat ne constitue pas la source de vérité technique ou décisionnelle du projet.
- **Principe 3 : Suprématie du Validator.** L'humain (le Validator) conserve le pouvoir d'arbitrage, de déblocage et d'acceptation finale. L'IA ne prend jamais de décision métier à la place du Validator.
- **Principe 4 : Atomicité des actions.** Une tâche correspond à un critère d'acceptation et génère un ou plusieurs commits clairement tracés. Le découpage s'arrête au niveau tâche (pas de sous-tâches floues).
- **Principe 5 : Itération contrôlée.** Aucune avancée n'est permise sans le signal `GO` explicite du Validator à chaque étape du cycle de vie du sprint.

---

*Fin du chapitre 1.*
