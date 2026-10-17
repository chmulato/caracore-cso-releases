# CaraCore CSO — Loja e Releases

Vitrine comercial da **Gestão de Transportes CSO**, construída na oficina
`caracore-cso-transportes`, com **Virtual Tracker™ como capacidade de integração
e localização**, não terceiro produto. Decisão de 17/10/2026:
**lançamento-alvo conjunto em 08/11/2028**, sujeito à validação e homologação.
Frotas Web é a aplicação complementar já disponível.

**Clone local (único):** `D:\onedrive\dev\caracore-cso-releases`  
**URL da loja:** https://cso-transp.caracore.com.br/  
**Aplicação Frotas (não é esta vitrine):** https://cso.caracore.com.br/  
**Wiki:** https://wiki.caracore.com.br/projeto-cso.html

## O que esta loja apresenta

| Frente | Status | Onde |
|---|---|---|
| **Gestão de Frotas (Web)** | Em produção | [cso.caracore.com.br](https://cso.caracore.com.br/) — oficina `caracore-cso-quarkus` |
| **Gestão de Transportes (Desktop)** | Em desenvolvimento; alvo **08/11/2028** | Oficina `caracore-cso-transportes` — instalador ainda não publicado |
| **Virtual Tracker** | Capacidade futura; alvo conjunto **08/11/2028** | Interface/hop em Frotas; recebimento, histórico/mapa em Transportes |

Quem contrata a Frotas **hoje** compra gestão no navegador — **não** o desktop e **não** rastreador GPS. Virtual Tracker™ (GPS/mapa) fica fora desse contrato atual.

A localização exige conexão com Frotas e a base Transportes, sem fila offline
no celular. Preços, pacotes e condições comerciais de Transportes/VT ainda
não estão definidos; não há contratação antecipada. A data não confirma
disponibilidade nem ativa download automaticamente.

## Rastreabilidade da proposta

O plano mestre fica na oficina `caracore-cso-transportes`, em
`docs/plano_organizado_execucao_cso.md`, seção 7: cada promessa desta loja
corresponde a tarefas INT-01 a INT-21, com donos, dependências e critérios de
aceite. As 10 sprints locais não são o plano completo do lançamento.
INT-02 valida o celular e INT-03 estima capacidade/calendário; INT-20/21
condicionam oferta e publicação a evidências de homologação. Nenhuma tarefa
integrada foi concluída nesta revisão documental. A data continua um alvo.

A loja **não** substitui a aplicação. CTAs de uso apontam para `cso.caracore.com.br`. Esta Pages serve vitrine das duas frentes, status de download e canal de feedback.

## Páginas

- [index.html](docs/index.html) — proposta de Transportes com Virtual Tracker; Frotas como complemento disponível
- [download.html](docs/download.html) — sem instalador público; lançamento-alvo conjunto em 08/11/2028
- [tecnologia.html](docs/tecnologia.html) — stacks das duas oficinas
- [canal-feedback.html](docs/canal-feedback.html) — e-mail, WhatsApp, Telegram
- `docs/wiki/` — redireciona para o portal wiki

## Publicação

GitHub Pages a partir de `docs/` · custom domain `cso-transp.caracore.com.br` (ficheiro `docs/CNAME`). DNS no Registro.br: CNAME → `chmulato.github.io`.

O hostname legado `*.up.railway.app` **não** é URL pública da Frotas.

## Canais de suporte

1. E-mail: suporte@caracore.com.br
2. WhatsApp: +55 41 9 9909-7797
3. Telegram: @chmulato

## Licença

Licenciamento proprietário institucional da Cara Core Informática. Consulte [LICENSE](LICENSE).
