# Checklist de Publicacao - CaraCore CSO Loja

## 1) Confirmar estado local
- Verificar branch e staging:
  git -C D:/dev/caracore-cso-releases status --short --branch

## 2) Commit
Mensagem sugerida:
chore(store): versiona novidades da loja CSO para publicacao

Comando:
git -C D:/dev/caracore-cso-releases commit -m "chore(store): versiona novidades da loja CSO para publicacao"

## 3) Tag de release
Tag sugerida:
store-cso-2026-04-01

Comando:
git -C D:/dev/caracore-cso-releases tag -a store-cso-2026-04-01 -m "Publicacao da vitrine da loja CSO em 2026-04-01"

## 4) Configurar remoto (se necessario)
git -C D:/dev/caracore-cso-releases remote -v

Se nao houver origin:
git -C D:/dev/caracore-cso-releases remote add origin https://github.com/chmulato/caracore-cso-releases.git

## 5) Push
Branch:
git -C D:/dev/caracore-cso-releases push -u origin main

Tag:
git -C D:/dev/caracore-cso-releases push origin store-cso-2026-04-01

## 6) Publicar release no GitHub
- Abrir: https://github.com/chmulato/caracore-cso-releases/releases/new
- Selecionar tag: store-cso-2026-04-01
- Titulo sugerido: CaraCore CSO Loja - Preparacao de Publicacao 2026-04-01
- Corpo: colar conteudo de RELEASE_NOTES_2026-04-01.md
