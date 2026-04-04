# Checklist de Publicação - CaraCore CSO Loja

## 1. Verificar estado local

Executar:

```bash
git -C D:/dev/caracore-cso-releases status --short --branch
```

Critério de aceite:
1. Branch correta.
2. Arquivos esperados em staging.

## 2. Criar commit

Mensagem sugerida:

```text
chore(store): versiona novidades da loja CSO para publicacao
```

Comando:

```bash
git -C D:/dev/caracore-cso-releases commit -m "chore(store): versiona novidades da loja CSO para publicacao"
```

## 3. Criar tag de release

Tag sugerida:

```text
store-cso-2026-04-01
```

Comando:

```bash
git -C D:/dev/caracore-cso-releases tag -a store-cso-2026-04-01 -m "Publicacao da vitrine da loja CSO em 2026-04-01"
```

## 4. Confirmar remoto

Executar:

```bash
git -C D:/dev/caracore-cso-releases remote -v
```

Se não houver `origin`, configurar:

```bash
git -C D:/dev/caracore-cso-releases remote add origin https://github.com/chmulato/caracore-cso-releases.git
```

## 5. Enviar branch e tag

Branch:

```bash
git -C D:/dev/caracore-cso-releases push -u origin main
```

Tag:

```bash
git -C D:/dev/caracore-cso-releases push origin store-cso-2026-04-01
```

## 6. Publicar release no GitHub

Passos:
1. Abrir https://github.com/chmulato/caracore-cso-releases/releases/new.
2. Selecionar a tag `store-cso-2026-04-01`.
3. Título sugerido: `CaraCore CSO Loja - Preparacao de Publicacao 2026-04-01`.
4. Colar o conteúdo de [RELEASE_NOTES_2026-04-01.md](RELEASE_NOTES_2026-04-01.md) no corpo da release.
