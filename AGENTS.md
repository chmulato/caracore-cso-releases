# AGENTS.md — Loja CaraCore CSO

Clone local **canónico** (único): `D:\onedrive\dev\caracore-cso-releases`  
Remoto: https://github.com/chmulato/caracore-cso-releases  
Público: https://cso-transp.caracore.com.br/

Esta pasta é a **loja única** das duas frentes do CaraCore CSO:

| Frente | Oficina (não editar vitrine lá) | Status |
|--------|--------------------------------|--------|
| Gestão de Frotas (Web) | `D:\onedrive\dev\caracore-cso-quarkus` | Em produção em cso.caracore.com.br |
| Gestão de Transportes (Desktop) | `D:\onedrive\dev\caracore-cso-transportes` | Garagem · GA 08/11/2028 · **oficina sem informação de loja** |

**Decisão 17/10/2026:** esta loja apresenta comercialmente o produto construído
na oficina Transportes. Gestão de Transportes e Virtual Tracker têm
**lançamento-alvo conjunto em 08/11/2028**, sujeito à validação e homologação.
Virtual Tracker é a capacidade de integração e localização entre Transportes e
Frotas, não terceiro produto. Preço/pacotes não definidos; sem oferta antecipada.
Frotas é a aplicação complementar já disponível, cuja contratação atual não
inclui desktop ou GPS. Localização somente online, sem fila offline no celular.

## Estado (17/10/2026)

- Home = proposta comercial de **Transportes com Virtual Tracker em desenvolvimento**, não conversão dos planos Frotas.
- Hero destaca o lançamento-alvo conjunto e CTAs de proposta/contato, sem comprar ou baixar produto ainda não publicado.
- Frotas disponível aparece como complemento, com link para seus preços na aplicação; não apresentar seus planos como preço de Transportes/VT.
- Stack detalhado em `tecnologia.html`. Confirmar publicação e homologação antes de anunciar disponibilidade, mesmo após a data-alvo.
- Sem depoimento inventado, sem % de economia, sem botão de `.exe` ativo.
- Aplicação Frotas (landing SEO, JSON-LD, cache 5 min, LCP WebP) vive na oficina Quarkus — **não** duplicar HTML de produto aqui.

## Regras

1. Toda copy/HTML/CSS da vitrine CSO mora **aqui**. A oficina Transportes (`caracore-cso-transportes`) não leva URL, clone nem copy de loja.
2. CTAs de uso → `https://cso.caracore.com.br/` (cadastro / login / checkout). Sem `/delivery/`. Sem instalador público até o GA.
3. Wiki de alinhamento: `D:\onedrive\dev\caracore-wiki` (`wiki.caracore.com.br/projeto-cso.html`).
4. Publicação: GitHub Pages a partir de `docs/`.
5. Norte do ecossistema: `D:\onedrive\dev\AGENTS.md`.
