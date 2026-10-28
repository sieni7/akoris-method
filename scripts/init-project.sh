#!/usr/bin/env bash
#
# init-project.sh — Scaffold un nouveau projet AKORIS.
#
# Usage :
#   ./init-project.sh <nom-du-projet> [<chemin-parent>]
#
# Crée :
#   <chemin-parent>/<nom-du-projet>/
#   ├── app/                    (exécutable vide)
#   ├── doc/                    (documentaire vide)
#   ├── checklists/             (copié depuis akoris-method/)
#   ├── .akoris/                (copié depuis templates/.akoris/)
#   └── .git/                   (git init -b main)

set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage : $0 <nom-du-projet> [<chemin-parent>]" >&2
    exit 1
fi

PROJECT_NAME="$1"
PARENT_DIR="${2:-.}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
METHOD_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATES_DIR="$METHOD_DIR/templates"

if [ ! -d "$TEMPLATES_DIR/.akoris" ]; then
    echo "ERREUR : templates/.akoris/ introuvable dans $METHOD_DIR" >&2
    exit 1
fi

if [ ! -d "$METHOD_DIR/checklists" ]; then
    echo "ERREUR : checklists/ introuvable dans $METHOD_DIR" >&2
    exit 1
fi

TARGET_DIR="$PARENT_DIR/$PROJECT_NAME"

if [ -e "$TARGET_DIR" ]; then
    echo "ERREUR : $TARGET_DIR existe déjà." >&2
    exit 1
fi

echo "→ Création de $TARGET_DIR"
mkdir -p "$TARGET_DIR"

echo "→ Création des piliers app/ et doc/"
mkdir -p "$TARGET_DIR/app/src"
mkdir -p "$TARGET_DIR/app/tests/unit"
mkdir -p "$TARGET_DIR/app/tests/integration"
mkdir -p "$TARGET_DIR/app/tests/e2e"
mkdir -p "$TARGET_DIR/app/tests/uat"
mkdir -p "$TARGET_DIR/app/tests/fixtures"
mkdir -p "$TARGET_DIR/doc/tech"
mkdir -p "$TARGET_DIR/doc/produit"
mkdir -p "$TARGET_DIR/doc/archive"

echo "→ Copie de .akoris/ depuis templates/"
cp -r "$TEMPLATES_DIR/.akoris" "$TARGET_DIR/.akoris"

echo "→ Copie de checklists/ depuis $METHOD_DIR/"
cp -r "$METHOD_DIR/checklists" "$TARGET_DIR/checklists"

echo "→ Création des dossiers manquants dans .akoris/"
mkdir -p "$TARGET_DIR/.akoris/debt"
mkdir -p "$TARGET_DIR/.akoris/sprints/archive"
mkdir -p "$TARGET_DIR/.akoris/audits/archive"
mkdir -p "$TARGET_DIR/.akoris/roadmap"
mkdir -p "$TARGET_DIR/.akoris/adr"

echo "→ Génération de debt/index.md via build-debt-index.py"
if command -v python3 >/dev/null 2>&1; then
    ( cd "$TARGET_DIR" && python3 .akoris/scripts/build-debt-index.py 2>/dev/null ) || {
        echo "⚠️  build-debt-index.py a échoué (pyyaml manquant ?)."
        echo "    Création d'un index.md minimal — lance le script plus tard."
        cat > "$TARGET_DIR/.akoris/debt/index.md" <<'EOF'
# INDEX DES DETTES — à régénérer

> Lance `python3 .akoris/scripts/build-debt-index.py` après avoir installé pyyaml.

| ID | Titre | Priorité | Statut | Sprint origine | Sprint résorption | ADR |
|----|-------|----------|--------|----------------|-------------------|-----|
EOF
    }
else
    echo "⚠️  python3 non trouvé. index.md minimal créé."
    cat > "$TARGET_DIR/.akoris/debt/index.md" <<'EOF'
# INDEX DES DETTES — à régénérer

| ID | Titre | Priorité | Statut | Sprint origine | Sprint résorption | ADR |
|----|-------|----------|--------|----------------|-------------------|-----|
EOF
fi

echo "→ Création de doc/tech/tests.md"
cat > "$TARGET_DIR/doc/tech/tests.md" <<'EOF'
# STRATÉGIE DE TESTS — <nom-du-projet>

## Familles actives (V0)
- TNR (unit + integration) : obligatoire, couverture ≥ 80%
- Sécu checkpoint : aux sprints 🔒
- UAT : implicite (verdict Validator)
- E2E : [1 si parcours critique / aucun]

## Où
- app/tests/unit/
- app/tests/integration/
- app/tests/e2e/ (si actif)

## Seuils
| Métrique | go | go with reserve | no-go |
|----------|-----|-----------------|-------|
| Couverture | ≥80% | 60-79% | <60% |
| Tests échoués | 0 | 0 (flaky doc.) | ≥1 |
| Findings critiques | 0 | 0 | ≥1 |
EOF

echo "→ Création de app/tests/README.md"
cat > "$TARGET_DIR/app/tests/README.md" <<'EOF'
# app/tests/ — Tests

- `unit/` : tests unitaires (TNR)
- `integration/` : tests d'intégration (TNR)
- `e2e/` : tests E2E
- `uat/` : scénarios UAT
- `fixtures/` : données partagées

Voir `doc/tech/tests.md` pour la stratégie.
EOF

echo "→ Création des placeholders README"
cat > "$TARGET_DIR/app/README.md" <<'EOF'
# app/ — Produit exécutable

Le code source du produit. Seul le Builder écrit ici.
EOF

cat > "$TARGET_DIR/doc/tech/README.md" <<'EOF'
# doc/tech/ — Documentation technique

Écrite par le Builder. Voir `tests.md` pour la stratégie de tests.
EOF

cat > "$TARGET_DIR/doc/produit/README.md" <<'EOF'
# doc/produit/ — Documentation produit

Écrite par l'Orchestrator. Voir `changelog.md` pour l'historique.
EOF

echo "→ Copie de .gitignore"
cat > "$TARGET_DIR/.gitignore" <<'EOF'
# Dépendances
node_modules/
venv/
.venv/

# Build
dist/
build/
*.egg-info/

# Secrets
.env
.env.local
*.key
*.pem

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# AKORIS
.akoris/doctor/
EOF

echo "→ git init -b main"
( cd "$TARGET_DIR" && git init -q -b main )

echo "→ Personnalisation de .akoris/projet.md"
if [ -f "$TARGET_DIR/.akoris/projet.md" ]; then
    # Remplacer <nom-du-projet> par le nom réel
    sed -i.bak "s/<nom-du-projet>/$PROJECT_NAME/g" "$TARGET_DIR/.akoris/projet.md"
    rm -f "$TARGET_DIR/.akoris/projet.md.bak"
fi

echo ""
echo "✅ Projet '$PROJECT_NAME' créé dans $TARGET_DIR"
echo ""
echo "Prochaines étapes :"
echo "  1. cd $TARGET_DIR"
echo "  2. Adapter .akoris/projet.md (stack, règles métier)"
echo "  3. git add . && git commit -m 'init: bootstrap AKORIS'"
echo "  4. Suivre .akoris/config/bootstrap.md dans l'onglet A"
echo ""
