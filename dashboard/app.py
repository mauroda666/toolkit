"""Gestor — dashboard Flask das ferramentas, agentes e skills do ecossistema.

Lê AO VIVO:
  - ferramentas  -> ./catalog.json (ou ../web/catalog.json)
  - agentes      -> ~/.claude/agents/*.md   (frontmatter YAML simples)
  - skills       -> ~/.claude/skills/*/SKILL.md

Rodar:  python app.py     (porta 8799; acessível no celular pela LAN)
"""
import json
import os
import re
from pathlib import Path

from flask import Flask, jsonify, render_template

APP_DIR = Path(__file__).resolve().parent
HOME = Path.home()
CLAUDE_AGENTS = HOME / ".claude" / "agents"
CLAUDE_SKILLS = HOME / ".claude" / "skills"

app = Flask(__name__)

DIVISIONS = [
    "project-management", "paid-media", "spatial-computing", "game-development",
    "academic", "design", "engineering", "finance", "gis", "healthcare",
    "marketing", "product", "sales", "security", "specialized", "support", "testing",
]


def load_tools():
    for p in (APP_DIR / "catalog.json", APP_DIR.parent / "web" / "catalog.json"):
        if p.exists():
            try:
                return json.loads(p.read_text(encoding="utf-8")).get("tools", [])
            except Exception:
                return []
    return []


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def division_of(stem):
    for d in sorted(DIVISIONS, key=len, reverse=True):
        if stem.startswith(d + "-"):
            return d
    return "outros"


def load_agents():
    out = []
    if CLAUDE_AGENTS.exists():
        for f in sorted(CLAUDE_AGENTS.glob("*.md")):
            fm = parse_frontmatter(f.read_text(encoding="utf-8", errors="ignore"))
            out.append({
                "id": f.stem,
                "name": fm.get("name", f.stem),
                "description": fm.get("description", ""),
                "division": division_of(f.stem),
                "emoji": fm.get("emoji", ""),
                "vibe": fm.get("vibe", ""),
            })
    return out


def load_skills():
    out = []
    if CLAUDE_SKILLS.exists():
        for sk in sorted(CLAUDE_SKILLS.glob("*/SKILL.md")):
            fm = parse_frontmatter(sk.read_text(encoding="utf-8", errors="ignore"))
            out.append({
                "id": sk.parent.name,
                "name": fm.get("name", sk.parent.name),
                "description": fm.get("description", ""),
            })
    return out


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/data")
def api_data():
    tools, agents, skills = load_tools(), load_agents(), load_skills()
    return jsonify({
        "tools": tools,
        "agents": agents,
        "skills": skills,
        "stats": {"tools": len(tools), "agents": len(agents), "skills": len(skills)},
    })


def _body_after_fm(text):
    m = re.match(r"^---\s*\n.*?\n---\s*\n?(.*)$", text, re.S)
    return (m.group(1) if m else text).strip()


@app.route("/api/agent/<path:agent_id>")
def api_agent(agent_id):
    f = (CLAUDE_AGENTS / (agent_id + ".md"))
    if not f.exists() or f.resolve().parent != CLAUDE_AGENTS.resolve():
        return jsonify({"error": "nao encontrado"}), 404
    text = f.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter(text)
    name = fm.get("name", agent_id)
    desc = fm.get("description", "")
    prompt = (f'Use o agente "{name}" (divisão {division_of(agent_id)}) para a tarefa a seguir.\n'
              f"Especialidade: {desc}\n\nTarefa: ")
    return jsonify({"id": agent_id, "name": name, "description": desc,
                    "division": division_of(agent_id), "source": text,
                    "body": _body_after_fm(text), "prompt": prompt})


@app.route("/api/skill/<path:skill_id>")
def api_skill(skill_id):
    f = (CLAUDE_SKILLS / skill_id / "SKILL.md")
    if not f.exists() or CLAUDE_SKILLS.resolve() not in f.resolve().parents:
        return jsonify({"error": "nao encontrado"}), 404
    text = f.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter(text)
    name = fm.get("name", skill_id)
    desc = fm.get("description", "")
    prompt = f'Ative a skill "{name}" ({desc}).\n\nTarefa: '
    return jsonify({"id": skill_id, "name": name, "description": desc,
                    "source": text, "body": _body_after_fm(text), "prompt": prompt})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8799"))
    print(f"Gestor em http://localhost:{port}  (celular: http://<IP-do-desktop>:{port})")
    app.run(host="0.0.0.0", port=port, debug=False)
