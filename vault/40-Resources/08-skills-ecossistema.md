# 🧩 Skills fundamentais + o gerenciador de skills (npx skills)

Fontes: [vercel-labs/skills](https://github.com/vercel-labs/skills) (a CLI) e [mattpocock/skills](https://github.com/mattpocock/skills).

## O achado principal
`npx skills` é o **gerenciador de pacotes do ecossistema aberto de agent skills** (diretório em https://skills.sh). Instala/atualiza skills (SKILL.md) em dezenas de agentes — **e suporta o OpenClaw nativamente** (`~/.openclaw/skills/`). Ou seja: dá pra equipar o seu swarm (e o Claude Code) com skills testadas da comunidade **com um comando**, mantendo-as atualizáveis (`npx skills update`) em vez de copiar-forkar e apodrecer.

Comandos-chave: `npx skills find <q>` (busca), `npx skills add <owner/repo[@skill]>` (instala), `npx skills update`, `npx skills init` (cria a sua).

## Skills fundamentais para adotar (mapeadas ao ecossistema)
| Skill / fonte | O que faz | Onde encaixa |
|---|---|---|
| **find-skills** (vercel-labs/skills) | Meta-skill: descobre/instala skills sob demanda | Todo o swarm + Claude Code |
| **skill-creator / write-a-skill** (vercel-labs/agent-skills, mattpocock) | Cria novas SKILL.md com qualidade | Fabricar as skills do openclaw/enxame-studio |
| **web-design-guidelines / frontend-design** (vercel-labs/agent-skills, ~100K+ installs) | Padrões de UI/UX e design web | equita-webapp, landings, sites de cliente |
| **react-best-practices** (vercel-labs) | Performance React/Next | equita-webapp, reputa-zap, radar-marca-ia |
| **to-prd** (mattpocock) | Ideia → PRD estruturado | opportunity-scout, business-planner |
| **to-issues** (mattpocock) | Plano → issues no GitHub | orchestrator (fila de tarefas do swarm) |
| **grill-me / grill-with-docs** (mattpocock) | Entrevista implacável que afia um plano/design | orchestrator antes de construir; decisões de produto |
| **tdd** (mattpocock) | Test-driven development disciplinado | coder, qa-tester |
| **diagnose / triage** (mattpocock) | Diagnóstico e triagem de bugs | qa-tester, devops, incidentes |
| **improve-codebase-architecture / zoom-out** (mattpocock) | Refatoração e visão macro | coder, auditor |
| **handoff** (mattpocock) | Handoff de sessão/contexto | swarm-coordinator |
| **anthropics/skills** | Frontend design, processamento de documentos | Equita (documentos), UI |

## Como instalar (não-secreto → pode ir pro swarm)
No servidor onde vive o swarm (ou local), para o OpenClaw:
```bash
# meta-skill de descoberta (recomendado primeiro)
npx skills add vercel-labs/skills@find-skills -a openclaw -g -y
# pacote de design/dev da Vercel (escolha as skills)
npx skills add vercel-labs/agent-skills --skill frontend-design --skill web-design-guidelines -a openclaw -g -y
# workflow do Matt Pocock (PRD, issues, tdd, triage, grill)
npx skills add mattpocock/skills --skill to-prd --skill to-issues --skill tdd --skill grill-me -a openclaw -g -y
# para o Claude Code, troque -a openclaw por -a claude-code
```
> Skills são **não-secretas** → ok versionar/sincronizar. Como o `openclaw/` do repo é espelho sanitizado sincronizado à VM, o caminho limpo é instalar em `~/.openclaw/skills/` na VM (via deploy/console) OU commitar em `openclaw/agents/<agente>/agent/skills/`. Prefira **instalar pela CLI** para receber updates upstream; forke só quando for customizar.

## Por que é estratégico (e monetizável)
- **Velocidade de entrega:** o enxame-studio (white-label) passa a montar produtos com skills testadas (design, PRD, issues, TDD) — menos retrabalho, mais margem.
- **Qualidade de UI dos clientes:** web-design/frontend-design elevam o padrão de landings e webapps (Equita, sites de cliente).
- **Pipeline intake→entrega produtizado:** to-prd + to-issues + grill-me transformam "ideia do cliente" em PRD afiado → issues → execução pelo swarm. É o núcleo vendável do enxame-studio.
- **Fábrica de skills própria:** skill-creator/write-a-skill deixam você publicar as SUAS skills (mauroda666) no skills.sh — presença + distribuição.

## Próximo passo sugerido
PR no openclaw adicionando uma skill **skills-manager** (ensina o swarm a descobrir/instalar/atualizar skills via `npx skills`, com a lista curada acima) — a meta-capability que destrava todas as outras.
