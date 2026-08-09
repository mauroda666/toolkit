@echo off
git init -b main
git add .
git commit -m "Ecossistema Toolkit: 70 ferramentas, dashboard, guias, vault Obsidian"
git remote remove origin 2>nul
git remote add origin https://github.com/mauroda666/toolkit.git
git push -u origin main
echo Pronto! Veja em https://github.com/mauroda666/toolkit
pause
