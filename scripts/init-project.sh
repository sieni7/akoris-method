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
echo "→ Copie de doc/ depuis templates/"
cp -r "$TEMPLATES_DIR/doc/." "$TARGET_DIR/doc/"

echo "→ Copie de checklists/ depuis $METHOD_DIR/"
cp -r "$METHOD_DIR/checklists" "$TARGET_DIR/checklists"

echo "→ Création des dossiers manquants dans .akoris/"
mkdir -p "$TARGET_DIR/.akoris/debt"
mkdir -p "$TARGET_DIR/.akoris/sprints/archive"
mkdir -p "$TARGET_DIR/.akoris/audits/archive"
mkdir -p "$TARGET_DIR/.akoris/roadmap"
mkdir -p "$TARGET_DIR/.akoris/adr"

echo "→ Génération de debt/index.md via build-debt-index.py"
if command -v python3 >/dev/null 2>&1 && python3 -c 'import yaml' >/dev/null 2>&1; then
    ( cd "$TARGET_DIR" && python3 .akoris/scripts/build-debt-index.py )
else
    echo "⚠️ PyYAML non détecté. L'index des dettes est copié depuis le template."
    echo "Installe PyYAML avant d'ajouter des dettes : pip install pyyaml"
fi

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

echo "→ Personnalisation des fichiers Markdown de .akoris/"
find "$TARGET_DIR/.akoris" -name "*.md" -exec sed -i.bak "s/<nom-du-projet>/$PROJECT_NAME/g" {} +
find "$TARGET_DIR/.akoris" -name "*.md.bak" -delete

echo ""
echo "✅ Projet '$PROJECT_NAME' créé dans $TARGET_DIR"
echo ""
echo "Prochaines étapes :"
echo "  1. cd $TARGET_DIR"
echo "  2. Adapter .akoris/projet.md (stack, règles métier)"
echo "  3. git add . && git commit -m 'init: bootstrap AKORIS'"
echo "  4. Suivre .akoris/config/bootstrap.md dans l'onglet A"
echo ""
