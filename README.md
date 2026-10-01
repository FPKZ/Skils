# Hub Central de Skills & Orquestrador de Agentes (Agente 0)

Este repositório é o **controlador central** de habilidades (skills) e metodologia de desenvolvimento para o **Google Antigravity** e **Antigravity IDE**.

Ele atua como o cérebro metodológico global do seu ambiente de desenvolvimento:
1. **Disponibilidade Global:** Todas as skills deste repositório estão conectadas globalmente ao Antigravity (`~/.gemini/config/skills.json` e symlinks em `~/.gemini/skills/` / `~/.agents/skills/`). Isso significa que o Antigravity e a IDE têm acesso a elas **em qualquer projeto que você abrir**.
2. **Agente 0 (Orquestrador de Tokens):** Controla o fluxo de trabalho antes de gastar tokens, decidindo a rota mais eficiente (execução direta, TDD, planejamento arquitetural ou subagentes).
3. **Distribuidor Sob Demanda:** Mantém o catálogo indexado com mais de 2.500 skills especializadas. Quando você estiver trabalhando em um projeto específico (ex: React, Tailwind, Docker), o agente instala a skill diretamente no projeto alvo (`.agents/skills/`), mantendo este repositório limpo.
4. **Criação Sob Demanda:** Permite criar, evoluir e refatorar novas skills sob medida quando novos padrões surgirem.

---

## 📦 Skills Centrais Instaladas (24 Skills)

### 1. Metodologia & Orquestração
- **`ask-matt`**: Roteador inteligente para escolher o fluxo de trabalho ideal.
- **`using-superpowers`**: Meta-skill que garante que o agente verifique e use as skills certas antes de agir.
- **`brainstorming`**: Alinhamento de requisitos, intenção e escopo antes de qualquer código.
- **`grill-me` / `grilling`**: Entrevistas focadas para estressar ideias e encontrar falhas de design cedo.
- **`writing-plans`**: Criação de planos de implementação divididos em tarefas pequenas (2-5 min).
- **`executing-plans`**: Execução sequencial de planos na mesma sessão (modo econômico em tokens).
- **`subagent-driven-development`**: Execução autônoma despachando subagentes dedicados por tarefa.
- **`wayfinder`**: Planejamento de iniciativas grandes e incertas como mapas de decisões.

### 2. Testes & Qualidade de Código
- **`test-driven-development` (TDD)**: Ciclo estrito Red-Green-Refactor. Proíbe código antes de teste falhando.
- **`verification-before-completion`**: Proíbe afirmar que algo está pronto ou corrigido sem executar a validação real.

### 3. Depuração & Arquitetura
- **`systematic-debugging`**: Processo de 4 fases para investigar a causa-raiz de bugs antes de propor correções.
- **`codebase-design`**: Vocabulário e princípios para desenhar módulos profundos (*deep modules*).
- **`domain-modeling`**: Modelagem do vocabulário de domínio e registros de decisão (ADRs).
- **`improve-codebase-architecture`**: Varredura em busca de oportunidades de desacoplamento e melhoria arquitetural.
- **`prototype`**: Criação de protótipos descartáveis para responder dúvidas de design ou lógica.
- **`diagnosing-superpowers`**: Auditoria de sessões passadas para entender desvios ou gastos excessivos.

### 4. Git & Colaboração
- **`using-git-worktrees`**: Criação de ambientes isolados via Git Worktree para proteger branches principais.
- **`finishing-a-development-branch`**: Verificação final de testes, opções de merge/PR e limpeza de worktrees.
- **`requesting-code-review`**: Solicitação de revisão de código comparando diffs contra o plano.
- **`receiving-code-review`**: Avaliação técnica crítica de feedbacks de revisão sem concordância cega.
- **`dispatching-parallel-agents`**: Investigação de múltiplos problemas independentes em paralelo.
- **`wizard`**: Geração de scripts interativos para passos manuais (tokens, cloud, acessos).

### 5. Extensibilidade
- **`writing-skills`**: Criação e teste de novas skills usando TDD de documentação.

---

## 🛠️ Gerenciador de Skills (`skill-hub.py`)

Para buscar e instalar skills específicas de frameworks e bibliotecas nos seus projetos:

### 1. Pesquisar skills no catálogo (2.500+ opções):
```bash
./scripts/skill-hub.py search react
./scripts/skill-hub.py search docker
./scripts/skill-hub.py search tailwind
```

### 2. Ver detalhes de uma skill:
```bash
./scripts/skill-hub.py info react-best-practices
```

### 3. Instalar uma skill em outro projeto:
```bash
# Instala diretamente em /caminho/do/projeto/.agents/skills/react-best-practices
./scripts/skill-hub.py install react-best-practices /caminho/do/seu/projeto
```

---

## 🤖 Como Funciona no Dia a Dia com o Antigravity

1. **Em qualquer projeto:** O Antigravity já reconhece as 24 skills deste repositório como guia de conduta.
2. **Ao pedir uma nova tecnologia:** Diga ao agente *"Estamos criando uma tela em React"*. O Agente 0 verificará se o projeto precisa da skill `react-best-practices`, consultará o catálogo e perguntará:
   > *"Deseja que eu instale a skill 'react-best-practices' na pasta `.agents/skills` deste projeto?"*
3. **Após a sua confirmação:** Ele instala a skill localmente no projeto em questão, deixando seu código padronizado sem poluir este repositório central.
4. **Criando novos padrões:** Quando você e o agente resolverem um fluxo que queira padronizar para o futuro, o agente perguntará se deseja empacotar como uma nova skill.
