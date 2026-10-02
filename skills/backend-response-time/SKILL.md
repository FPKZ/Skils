---
name: backend-response-time
description: Analisa, audita e otimiza a latência e o tempo de resposta das rotas e serviços no backend. Focado em manter a execução abaixo de limites rígidos (sub-10ms em memória/cache, sub-50ms em I/O local), eliminar I/O bloqueante (Sync desnecessário), otimizar complexidade algorítmica (O(1) lookups vs O(N)), reduzir serializações redundantes e garantir máxima fluidez e reatividade para o frontend e mobile.
---

# Backend Response Time & Latency Optimization (Performance & Fluidez)

## 🎯 Visão Geral e Princípio Central
A fluidez e a percepção de velocidade de uma aplicação pelo usuário final dependem diretamente do tempo de resposta do backend.
Cada milissegundo adicional no servidor infla o TTFB (Time to First Byte), atrasa a montagem das telas no frontend/mobile e degrada a experiência do usuário.

```
MÁXIMA EFICIÊNCIA: NENHUMA ROTA CRÍTICA DEVE DESPERDIÇAR CICLOS DE CPU OU I/O
```

---

## ⏱️ Budgets de Latência (Metas Mandatórias)

| Tipo de Operação | Meta Ideal | Limite Máximo Tolerado | Ação se Ultrapassado |
| :--- | :--- | :--- | :--- |
| **Operação em Memória / Cache** | `< 2ms` | `5ms` | Otimizar estrutura de dados (usar Map/Set, evitar O(N²)) |
| **Leitura em Disco Local / JSON** | `< 10ms` | `25ms` | Implementar cache em memória ou debounce/leitura seletiva |
| **Escrita / Persistência Local** | `< 15ms` | `40ms` | Escrita atômica assíncrona, evitar serializações repetitivas |
| **Rotas de Listagem / Leitura (GET)** | `< 25ms` | `60ms` | Reduzir payloads, índices rápidos, eliminar joins/scans pesados |
| **Rotas de Mutação (POST, PUT, DELETE)** | `< 50ms` | `100ms` | Processamento assíncrono em background quando cabível |

---

## 🔍 Checklist de Auditoria de Desempenho (Sentinel & Forge)

### 1. Eliminação de Bloqueios no Event Loop (Node.js)
- [ ] Identificar e eliminar métodos síncronos repetitivos (`fs.*Sync`) em rotas de alto tráfego contínuo.
- [ ] Garantir que loops e transformações de dados não bloqueiem o loop por mais de 5ms.
- [ ] Utilizar fluxos assíncronos (`fs.promises`) ou workers dedicados para operações I/O intensivas.

### 2. Complexidade Algorítmica e Estruturas de Dados
- [ ] Substituir buscas sequenciais `Array.find()` ou `Array.filter()` repetidas em loop por mapas indexados `new Map()` ou `Set` (reduzindo de O(N²) para O(1)).
- [ ] Evitar iterações redundantes sobre coleções (aplicar transformações em uma única passagem ou em lazy evaluation).

### 3. I/O Mínimo e Inteligente (Disco e Rede)
- [ ] **Não reler o disco:** Se o dado já foi lido recentemente e não houve mutação externa, reaproveitar estado ou cache.
- [ ] **Não regravar o disco:** Se uma alteração não modificou o conteúdo real do documento, abortar a gravação física (dirty checking).
- [ ] **Leitura seletiva:** Ler apenas os metadados necessários (ex: `manifest.json`) em vez de carregar todos os arquivos individuais da pasta para uma simples listagem.

### 4. Serialização e Parsing (JSON Overhead)
- [ ] `JSON.stringify` e `JSON.parse` em objetos massivos consomem tempo considerável de CPU.
- [ ] Evitar serializar repetidamente o mesmo objeto no mesmo ciclo de requisição.

### 5. Medição Concreta e Benchmarking
- [ ] Instrumentar o tempo real de execução com `performance.now()` ou `console.time()` em testes e auditorias.
- [ ] Adicionar headers como `Server-Timing` quando útil para rastrear gargalos ponta-a-ponta.
- [ ] Toda auditoria do Sentinel deve comprovar a latência média das rotas ou serviços afetados.

---

## 🚫 Antipatterns Proibidos
1. **Varredura Completa de Diretório em Cada Listagem:** Nunca varrer todos os arquivos JSON de uma pasta se houver um arquivo de índice/manifest disponível.
2. **Escrita sem Verificação de Mudança:** Gravar em disco sem checar se os dados realmente foram alterados.
3. **Múltiplas Chamadas Externas Sequenciais (Waterfall):** Quando dados independentes forem necessários, executar via `Promise.all` em paralelo, nunca em `await` sequencial.
