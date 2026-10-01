# Hub Central de Skills & Diretrizes do Agente 0

Este repositório (`/home/felipe/Documentos/skils`) é o **Controlador Central de Habilidades e Metodologias** para o Google Antigravity e Antigravity IDE.

## Papel do Repositório
1. **Hospedar Skills Centrais de Processo:** TDD, Debugging, Arquitetura, Planejamento, Execução e Verificação (instaladas em `./skills`).
2. **Índice Global de Tecnologias:** Catálogo com mais de 2.500 skills especializadas em `./catalog/skills_index.json`.
3. **Distribuidor de Skills:** Fornecer o utilitário CLI `./scripts/skill-hub.py` para buscar e instalar skills específicas diretamente nos repositórios dos projetos em que você estiver trabalhando.

## Diretrizes do Agente 0
- **Economia de Tokens:** Sempre avalie se a tarefa é Simples, Média ou Complexa antes de acionar skills pesadas.
- **Isolamento de Tecnologias:** Nunca instale skills de frameworks ou bibliotecas específicas (ex: React, Vue, Django) aqui neste repositório central. Elas devem ser instaladas no repositório de cada projeto (`.agents/skills/<skill-name>`).
- **Criação sob Demanda:** Se um novo padrão de desenvolvimento for criado ou refinado durante o uso, peça autorização para salvar como uma nova skill via `writing-skills`.
