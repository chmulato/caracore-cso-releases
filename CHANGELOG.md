# Changelog - CaraCore CSO Loja

Este arquivo registra alterações relevantes da loja e da documentação de publicação.

## 2026-10-17 - Transportes com Virtual Tracker: alvo conjunto

### Relay sem dados de trajeto em Frotas

- Decisão confirmada: E2EE celular-desktop, com chave privada de descriptografia somente na instalação do cliente. Frotas conecta/encaminha, não lê ou armazena posições, rotas, informações de trânsito ou envelopes de telemetria.
- Home e tecnologia refletem a proposta de soberania. Critérios do plano incluem ausência de persistência em logs/APM/proxy/cache/filas e limites de memória/banda/conexões do relay. Capacidade ainda em planejamento, não implementada.

### Rastreabilidade do plano

- A oficina Transportes consolidou o backlog mestre integrado INT-01..21, em seis etapas E0–E5, com dependências, donos por oficina e aceites vinculados às promessas da home.
- As 10 sprints de evolução local não equivalem ao total do lançamento. Prova de viabilidade móvel e estimativa/capacidade antecedem o compromisso de execução; oferta/publicação dependem de homologação.
- Planejamento apenas: nenhuma tarefa de GPS/integração concluída e nenhuma nova promessa comercial adicionada.

### Clareza comercial e contato

- Benefício no título: organizar entregas e acompanhar deslocamentos pelo celular; explicação simples dos papéis de Frotas, Transportes e Virtual Tracker.
- CTA principal “Conversar sobre minha operação” abre WhatsApp com mensagem de interesse preenchida; CTA secundário explica o funcionamento. E-mail e Telegram permanecem como alternativas com links diretos na página de contato.
- Detalhes de arquitetura ficam na página de tecnologia. Data-alvo, estágio de desenvolvimento, limites de conexão/localização e ausência de contratação antecipada continuam explícitos.

1. Decisão explícita do responsável: lançamento-alvo conjunto de Gestão de Transportes e Virtual Tracker em **08/11/2028**, substituindo a previsão de VT após dezembro de 2028, sem janela confirmada. É mudança de planejamento, não entrega ou homologação.
2. Home reposicionada para o produto da oficina Transportes; Frotas Web aparece como aplicação complementar disponível. Removidos cards de preço Frotas para não sugerirem preço de Transportes/VT.
3. Virtual Tracker definido como capacidade de integração e localização, não terceiro produto. Interface/hop em Frotas e histórico/mapa em Transportes; localização online-only, sem fila no celular.
4. Download, tecnologia, feedback e rodapés alinhados ao mesmo alvo, com preço/pacotes indefinidos e sem oferta antecipada. Contador não anuncia disponibilidade automaticamente ao atingir a data.
5. Esta revisão não implementa GPS/integração nem publica instalador. Publicação da vitrine depende de commit/push e deploy separados.

## 2026-09-29 - Roadmap alinhado à fila empresarial

### Loja
1. As páginas de home, download, tecnologia e feedback informam a janela FRO de **08/abr–dez/2027** e o freeze do Momento 1 em **08/11/2026**.
2. A home esclarece que Frotas já está no ar, que o freeze não é um novo lançamento e que o escopo FRO ainda não está disponível. Momento 2/PWA fica para depois de dez/2028, sem janela confirmada.

## 2026-09-05 - Home de conversão (Frotas hoje)

### Loja
1. Home reescrita para vender o que existe agora: hero com um H1, dois CTAs e “já tem conta”.
2. Seções de valor, “para quem é” e planos em cards — stack e 2028 saíram do topo.
3. Sem depoimento inventado e sem percentual de economia. GPS e Transportes ficam no bloco “ainda não está no contrato”.
4. `AGENTS.md` e `.cursor/rules/project-memory.mdc` descrevem a home de conversão para outras IAs.

---

## 2026-09-05 - Loja única e CSO unificado em 2028

### Loja
1. Copy da home, download, tecnologia e feedback: esta Pages é a loja das **duas** frentes; em **08/11/2028** Frotas + Transportes passam a ser **um só CaraCore CSO**.
2. Rodapé único em todas as páginas: Frotas disponível · completar frota 1º trim. 2027 · CSO único 08/11/2028 · GPS fora do contrato de hoje.
3. Cards Equipe e Operação alinham o que a Frotas já entrega (troca de perfil pelo ADMIN; KM no abastecimento/viagem; veículo inativo).
4. Transportes continua em Garagem — sem instalador e sem novidade de download. Contratar a Frotas hoje não inclui o desktop.

---

## 2026-05-21 - Ciclo de qualidade e progresso da oficina

### Progresso da oficina
1. Suite de testes backend zerada: 331 / 331 testes, 0 falhas (era 190 / 200).
2. Plano de casos de uso concluído: UC-01 a UC-10 todos implementados.
3. ATO 1 do Protocolo Amarelinha (Geometria): sequência obrigatória de 5 checkpoints implementada e testada.
4. Testes frontend Vitest: 34 / 34 green.
5. Flyway expandido: V1-V13 (13 migrações ativas).

### Segurança
1. Validação CVE em 2026-05-21 sem ocorrências críticas.
2. Validação CVE em 2026-05-21 sem ocorrências de alta severidade.

### Documentação
1. CHANGELOG.md, README.md: atualizados.
2. Loja: evo-roadmap-footer atualizado com milestones de maio/2026.

---

## 2026-04-01 - Atualização de vitrine para publicação

### Inclusões
1. Banner de pré-lançamento com data oficial da versão 1.0.0 (08/11/2028) na página inicial.
2. Chamada para demonstração na matriz institucional.
3. Página de download com orientação de instalação e verificação de integridade SHA-256.
4. Canal de feedback com rotas para e-mail, WhatsApp e Telegram.
5. Publicação do manual em estrutura Docsify.

### Ajustes
1. Revisão da comunicação institucional sobre segurança de dados locais em SQLite.
2. Consolidação da relação entre loja e matriz para apresentação e consultoria.

### Segurança
1. Validação CVE em 2026-04-01 sem ocorrências críticas.
2. Validação CVE em 2026-04-01 sem ocorrências de alta severidade.
