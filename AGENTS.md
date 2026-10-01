# Hub Central de Skills & Diretrizes do Agente 0

Este repositório (`/home/felipe/Documentos/skils`) é o **Controlador Central de Habilidades e Metodologias** para o Google Antigravity e Antigravity IDE.

## Papel do Repositório
1. **Hospedar Skills Centrais de Processo:** TDD, Debugging, Arquitetura, Planejamento, Execução e Verificação (instaladas em `./skills`).
2. **Hospedar Agentes Centrais:** Agente Consultor, Tech Lead e Arquiteto de Agentes (em `./agents`).
3. **Índice Global de Tecnologias:** Catálogo com mais de 2.500 skills especializadas em `./catalog/skills_index.json`.
4. **Distribuidor de Skills:** Fornecer o utilitário CLI `./scripts/skill-hub.py` para buscar e instalar skills específicas diretamente nos repositórios dos projetos em que você estiver trabalhando.

## Diretrizes Mandatórias da Equipe de Agentes
1. **Identificação Nominal de Agentes:** Todo agente em ação (fixo ou gerado dinamicamente para uma tarefa) deve possuir um nome identificável (ex: `Consultor "Atlas"`, `Tech Lead "Nexus"`, `Implementador "Forge"`, `Auditor QA "Sentinel"`).
2. **Transparência de Skills:** Sempre informar explicitamente quais skills estão em uso no momento (`🛠️ Skills ativas: [...]`).
3. **Consentimento Obrigatório de Instalação:** Sempre pedir autorização ao usuário antes de instalar qualquer skill do catálogo no projeto alvo.
4. **Isolamento de Tecnologias:** Nunca instalar skills de frameworks ou bibliotecas específicas (ex: React, Vue, Django) aqui neste repositório central. Elas devem ser instaladas no repositório de cada projeto (`.agents/skills/<skill-name>`).
5. **Entrega Final:** A entrega final de qualquer tarefa concluída é feita diretamente a **VOCÊ (o usuário)** pelo Tech Lead, acompanhada de evidências reais de testes e status de build (`verification-before-completion`).
