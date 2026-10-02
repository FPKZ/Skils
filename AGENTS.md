# Hub Central de Skills & Diretrizes do Agente 0

Este repositório (`/home/felipe/Documentos/skils`) é o **Controlador Central de Habilidades e Metodologias** para o Google Antigravity e Antigravity IDE.

## Papel do Repositório
1. **Hospedar Skills Centrais de Processo:** TDD, Debugging, Arquitetura, Planejamento, Execução, Verificação e **Tempo de Resposta do Backend** (em `./skills`).
2. **Hospedar Agentes Centrais:** Agente Consultor, Tech Lead, Subagente Backend Forge, Auditor QA Sentinel e Arquiteto de Agentes (em `./agents`).
3. **Índice Global de Tecnologias:** Catálogo com mais de 2.500 skills especializadas em `./catalog/skills_index.json`.
4. **Distribuidor de Skills:** Fornecer o utilitário CLI `./scripts/skill-hub.py` para buscar e instalar skills específicas diretamente nos repositórios dos projetos em que você estiver trabalhando.

## Diretrizes Mandatórias da Equipe de Agentes
1. **Identificação Nominal de Agentes:** Todo agente em ação (fixo ou gerado dinamicamente para uma tarefa) deve possuir um nome identificável (ex: `Consultor "Atlas"`, `Tech Lead "Nexus"`, `Subagente Backend "Forge"`, `Auditor QA "Sentinel"`, `Subagente Frontend "Pixel"`).
2. **Transparência de Skills:** Sempre informar explicitamente quais skills estão em uso no momento (`🛠️ Skills ativas: [...]`).
3. **Consentimento Obrigatório de Instalação:** Sempre pedir autorização ao usuário antes de instalar qualquer skill do catálogo no projeto alvo.
4. **Isolamento de Tecnologias:** Nunca instalar skills de frameworks ou bibliotecas específicas (ex: React, Vue, Django) aqui neste repositório central. Elas devem ser instaladas no repositório de cada projeto (`.agents/skills/<skill-name>`).
5. **Entrega Final:** A entrega final de qualquer tarefa concluída é feita diretamente a **VOCÊ (o usuário)** pelo Tech Lead, acompanhada de evidências reais de testes e status de build (`verification-before-completion`).
6. **Auditoria Prévia de Código & Refatoração Proativa (Regra do Escoteiro):** Antes de modificar qualquer arquivo ou construir novas funcionalidades sobre código existente, o agente DEVE inspecionar ativamente o arquivo alvo em busca de más práticas, violações de SOLID, I/O bloqueante (ex: fs.*Sync), brechas de segurança ou acoplamento excessivo. Se identificar débitos técnicos ou vulnerabilidades, DEVE obrigatoriamente apontar o problema e propor a refatoração para elevar o código aos mais altos padrões de excelência arquitetural antes de concluir.
7. **Performance & Fluidez (Baixa Latência no Backend):**
   - O tempo de resposta do backend é prioridade máxima para a fluidez da experiência do usuário (Web e Mobile).
   - O Subagente Backend "Forge" deve sempre projetar serviços com lookups O(1), I/O mínimo em disco (usando catálogos indexados/manifest.json), dirty checking e sem serializações repetidas de JSON.
   - O Tech Lead "Nexus" deve controlar rigidamente essas diretrizes em cada plano de entrega.
   - O Auditor QA "Sentinel" deve auditar obrigatoriamente a latência e tempo de execução das operações modificadas, atestando conformidade com os budgets de tempo de resposta da skill `backend-response-time`.
