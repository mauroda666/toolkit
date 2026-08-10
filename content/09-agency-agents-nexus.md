# 🤝 Agency Agents (NEXUS) — como usar os 270 agentes

Instalados no Claude Code (`~/.claude/agents/`, 270 personas do catálogo MIT
`msitarzewski/agency-agents`) e, no swarm, via ORDEM #413 (`~/.openclaw/agency-agents/`).
Os **Runbooks/Playbooks NEXUS** dizem *quais* agentes acionar por cenário — vivem no vault em
`Toolkit/20-Skills/agency-nexus/`.

## Runbooks (times prontos) → onde encaixam
| Runbook | Time | Encaixe no seu ecossistema |
|---|---|---|
| **Startup MVP** | discovery → build enxuto | enxame-studio (produto novo white-label), MEI Fácil, Sabidinho |
| **Enterprise Feature** | arquitetura + hardening | Equita (webapp/bridge), Quiksilver Hub |
| **Incident Response** | diagnose/triage/SRE | infra/ops (casa com o ops-runner + ops-endpoint #411) |
| **Marketing Campaign** | growth + conteúdo | conteudo-factory, Faceless (@minarquismo), radar-marca-ia |

## Playbooks (ciclo fase 0→6)
Discovery → Strategy → Foundation → Build → Hardening → Launch → Operate. É o **pipeline do
enxame-studio** ponta a ponta: intake do cliente → PRD → build → operação. Combina com as skills
`to-prd`/`to-issues`/`tdd` (PR #410) e o `grill-me` (#408) para afiar o plano antes de construir.

## Como acionar no Claude Code
Os agentes aparecem como subagentes após reiniciar o Claude Code. Invoque pelo papel
("use o backend-architect", "chame o code-reviewer") ou deixe o orchestrator montar o time do
runbook. Prompts de ativação em `agency-nexus/coordination/agent-activation-prompts.md`.

## Divisões (18) do catálogo
academic · design · engineering · finance · game-development · gis · healthcare · marketing ·
paid-media · product · project-management · sales · security · spatial-computing · specialized ·
support · testing (+ `strategy/` = runbooks/playbooks).

> Curadoria: 270 é bastante. Se quiser enxugar o Claude Code, dá pra manter só as divisões
> relevantes (engineering, product, project-management, marketing, sales, finance, security).
