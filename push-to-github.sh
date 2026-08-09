#!/usr/bin/env bash
# Envia todo o toolkit para o repositorio mauroda666/toolkit
set -e
git init -b main 2>/dev/null || git init
git add .
git commit -m "Ecossistema Toolkit: 70 ferramentas, dashboard, guias, vault Obsidian" || true
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/mauroda666/toolkit.git
git push -u origin main
echo "Pronto! Veja em https://github.com/mauroda666/toolkit"
