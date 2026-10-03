---
name: deep-technical-research
description: Metodologia de investigação técnica profunda, busca por soluções não documentadas, garimpo de discussões em fóruns (GitHub Issues, Reddit, StackOverflow, Hacker News), análise de CVEs/brechas conhecidas e validação de workarounds da comunidade.
---

# Metodologia de Investigação Técnica Profunda (Deep Technical Research)

Esta skill define o protocolo rigoroso de busca e extração de conhecimento técnico que **não se encontra na documentação oficial** ou que foi omitido pelos mantenedores de uma ferramenta/biblioteca.

---

## 🎯 Quando Ativar Esta Skill
- Um erro ou comportamento não está documentado na documentação oficial.
- Há suspeita de um bug crônico na biblioteca/serviço que ainda não foi corrigido.
- Necessidade de encontrar como outros desenvolvedores no mundo contornaram uma limitação arquitetural (*workarounds*).
- Investigação de brechas, vulnerabilidades (CVEs), vetores de ataque conhecidos ou bypasses relatados por pesquisadores de segurança.
- Identificação de flags ocultas, configurações não documentadas ou monkey patches estáveis.

---

## 🔍 Heurísticas e Dorks de Busca Avançada

Nunca faça buscas genéricas. Utilize operadores precisos:

### 1. Garimpo no GitHub (Issues, PRs, Discussões e Commits)
```text
site:github.com/<org>/<repo>/issues "<mensagem de erro exata>"
site:github.com/<org>/<repo>/issues "workaround" OR "temporary fix"
site:github.com inurl:pull "<termo>" "merged"
site:github.com inurl:commit "<termo>" "fix"
```

### 2. Garimpo em Comunidades & Fóruns de Engenharia
```text
site:reddit.com/r/<subreddits_relevantes> "<problema ou ferramenta>" "solved"
site:news.ycombinator.com "<ferramenta>" "exploit" OR "vulnerability" OR "show hn"
site:stackoverflow.com "<erro exato>" -"marked as duplicate"
site:lobste.rs "<ferramenta>"
```

### 3. Caça a Vulnerabilidades, CVEs e Advisories
```text
site:cve.org OR site:nvd.nist.gov "<nome da biblioteca>" "<versão>"
site:github.com/advisories "<nome da biblioteca>"
site:snyk.io/vuln "<nome da biblioteca>"
site:packetstormsecurity.com OR site:exploit-db.com "<ferramenta>"
```

---

## 🛡️ Protocolo de Validação e Filtragem de Risco

Soluções encontradas em fóruns carregam riscos severos. Toda descoberta DEVE ser auditada contra as seguintes 4 regras:

1. **Checagem de Cavalo de Troia / Pacotes Maliciosos:**
   - O comentário do fórum sugere instalar uma dependência desconhecida de terceiro?
   - Checar se o pacote tem atividade real, histórico de manutenção ou se é um vetor de typosquatting / supply-chain attack.
2. **Checagem de Degradação de Segurança:**
   - O workaround desabilita flags de segurança críticas (ex: `rejectUnauthorized: false`, CORS `*`, desativação de sandbox ou permissões root)?
   - Se sim, classifique expressamente como **ALTO RISCO** e busque alternativas seguras antes de recomendar.
3. **Checagem de Fuga de Memória / Concorrência:**
   - Monkey patches que interceptam métodos globais podem vazar referências ou quebrar o garbage collection sob alta concorrência.
4. **Verificação de Versão / Temporalidade:**
   - A solução de 2019 ainda é aplicável na versão moderna da biblioteca? Analisar se APIs internas chamadas pelo hack não foram depreciadas ou removidas.

---

## 📋 Formato do Dossiê Investigativo (Handoff Padronizado)

Toda entrega de investigação deve seguir rigorosamente este template:

```markdown
### 🕵️ Dossiê Investigativo: [Título do Problema]

- **Status da Documentação Oficial:** [Omitido / Considerado "By Design" / Bug Aberto]
- **Causa Raiz Identificada:** [Explicação técnica do porquê o comportamento ocorre]

#### 🌐 Fontes e Evidências Comunitárias
1. **[GitHub Issue #X | Autor | Data]:** [Link e citação do trecho chave]
2. **[Discussão Reddit / Artigo / CVE]:** [Link e síntese da descoberta]

#### 🛠️ Soluções Encontradas
- **Solução Recomendada / Workaround Seguro:**
  [Código ou configuração exata com passo a passo]
- **Soluções Alternativas (Se houver):**
  [Outros métodos tentados por usuários]

#### ⚠️ Avaliação de Impacto e Riscos
- **Segurança:** [Baixo / Médio / Alto] - [Explicação]
- **Manutenibilidade:** [Como isso se comportará em futuras atualizações]
- **Performance:** [Impacto no tempo de resposta ou I/O]
```
