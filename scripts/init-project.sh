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
#   ├── .akoris/                (copié depuis templates/.akoris/)
#   └── .git/                   (git init)
#
# Ne fait PAS :
#   - git commit initial (à toi de le faire)
#   - adapter contexte.md (à toi de le faire)
#   - lancer le bootstrap (à toi de le faire)

set -euo pipefail

# === Vérifications ===

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

TARGET_DIR="$PARENT_DIR/$PROJECT_NAME"

if [ -e "$TARGET_DIR" ]; then
    echo "ERREUR : $TARGET_DIR existe déjà." >&2
    exit 1
fi

# === Scaffold ===

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

echo "→ Création des placeholders README"
cat > "$TARGET_DIR/app/README.md" <<'EOF'
# app/ — Produit exécutable

Le code source du produit. Seul le Builder écrit ici.

- `src/` : code source
- `tests/` : tests (unit, integration, e2e, uat, fixtures)
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

echo "→ git init"
( cd "$TARGET_DIR" && git init -q )

# === Message final ===

echo ""
echo "✅ Projet '$PROJECT_NAME' créé dans $TARGET_DIR"
echo ""
echo "Prochaines étapes :"
echo "  1. cd $TARGET_DIR"
echo "  2. Adapter .akoris/contexte.md (stack, règles métier)"
echo "  3. git add . && git commit -m 'init: bootstrap AKORIS'"
echo "  4. Suivre .akoris/config/bootstrap.md dans l'onglet A"
echo ""
