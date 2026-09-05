# AGENTS.md — Loja CaraCore CSO

Clone local **canónico** (único): `D:\onedrive\dev\caracore-cso-releases`  
Remoto: https://github.com/chmulato/caracore-cso-releases  
Público: https://cso-transp.caracore.com.br/

Esta pasta é a **loja única** das duas frentes do CaraCore CSO:

| Frente | Oficina (não editar vitrine lá) | Status |
|--------|--------------------------------|--------|
| Gestão de Frotas (Web) | `D:\onedrive\dev\caracore-cso-quarkus` | Em produção em cso.caracore.com.br |
| Gestão de Transportes (Desktop) | `D:\onedrive\dev\caracore-cso-transportes` | Garagem · GA 08/11/2028 · **oficina sem informação de loja** |

Em **08/11/2028** as duas frentes viram **um só produto**. Até lá: quem contrata Frotas não leva desktop nem GPS. A loja **não** substitui a aplicação.

## Estado (05/09/2026)

- Home = **página de conversão** da Frotas (o que existe hoje), não wiki técnico.
- Hero: “Gestão de frotas simples, rápida e sem planilhas.” CTAs → `https://cso.caracore.com.br/cadastro` e `#planos`.
- 2028, desktop, stack e GPS ficam **abaixo** (bloco “ainda não está no contrato”). Stack detalhado só em `tecnologia.html`.
- Sem depoimento inventado, sem % de economia, sem botão de `.exe` ativo.
- Aplicação Frotas (landing SEO, JSON-LD, cache 5 min, LCP WebP) vive na oficina Quarkus — **não** duplicar HTML de produto aqui.

## Regras

1. Toda copy/HTML/CSS da vitrine CSO mora **aqui**. A oficina Transportes (`caracore-cso-transportes`) não leva URL, clone nem copy de loja.
2. CTAs de uso → `https://cso.caracore.com.br/` (cadastro / login / checkout). Sem `/delivery/`. Sem instalador público até o GA.
3. Wiki de alinhamento: `D:\onedrive\dev\caracore-wiki` (`wiki.caracore.com.br/projeto-cso.html`).
4. Publicação: GitHub Pages a partir de `docs/`.
5. Norte do ecossistema: `D:\onedrive\dev\AGENTS.md`.
