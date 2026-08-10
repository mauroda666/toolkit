# Gestor (Flask) — Ferramentas · Agentes · Skills

Dashboard único e responsivo (desktop + celular) que agrega, **ao vivo**:
- **Ferramentas** — o catálogo (`catalog.json`, 87 itens) com valor/categoria/links.
- **Agentes** — o que estiver em `~/.claude/agents/*.md` (hoje 218, curados).
- **Skills** — o que estiver em `~/.claude/skills/*/SKILL.md`.

Busca unificada + filtro por categoria (ferramentas) / divisão (agentes). Reflete
mudanças automaticamente: instalou/removeu um agente ou skill, recarregue a página.

## Rodar (Windows)
Requer **Python 3** instalado (se não tiver: `winget install Python.Python.3.12`).
```
duplo-clique em run.bat
```
Ou no terminal:
```
cd dashboard
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Abre em **http://localhost:8799**.

## Acessar no celular (mesma Wi-Fi)
1. No desktop, descubra o IP local: `ipconfig` → "Endereço IPv4" (ex.: 192.168.0.15).
2. No celular, abra `http://192.168.0.15:8799`.
3. Se não abrir, libere a porta no Firewall do Windows (perfil Privado) para o Python,
   ou: `netsh advfirewall firewall add rule name="Gestor 8799" dir=in action=allow protocol=TCP localport=8799`.

O app já escuta em `0.0.0.0`, então basta o desktop e o celular na mesma rede.

## Notas
- Porta configurável: `set PORT=9000 && python app.py`.
- Só leitura; não altera seus arquivos. Sem dependências além do Flask.
- Para deixar sempre ligado, dá pra criar um atalho do `run.bat` na inicialização.
