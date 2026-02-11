#!/usr/bin/env python3
"""
Build Evaluator for CSOnline RC-1
Valida binários e metadados após build bem-sucedido.
"""

import os
import json
import sys

def validate_binaries_and_metadata():
    """
    Valida se os binários e metadados estão prontos para serem referenciados pela pasta /docs.
    """
    docs_path = "docs"
    if not os.path.exists(docs_path):
        print("Erro: Pasta /docs não encontrada.")
        return False

    # Verificar se index.html existe
    index_path = os.path.join(docs_path, "index.html")
    if not os.path.exists(index_path):
        print("Erro: index.html não encontrado em /docs.")
        return False

    # Verificar se download.html existe
    download_path = os.path.join(docs_path, "download.html")
    if not os.path.exists(download_path):
        print("Erro: download.html não encontrado em /docs.")
        return False

    # Verificar se manual existe
    manual_path = os.path.join(docs_path, "manual")
    if not os.path.exists(manual_path):
        print("Erro: Pasta /docs/manual não encontrada.")
        return False

    # Verificar se feedback existe
    feedback_path = os.path.join(docs_path, "feedback")
    if not os.path.exists(feedback_path):
        print("Erro: Pasta /docs/feedback não encontrada.")
        return False

    # Verificar metadados (exemplo: version.json ou similar)
    metadata_path = "version.json"  # Assumindo um arquivo de metadados
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
            print(f"Metadados válidos: Versão {metadata.get('version', 'desconhecida')}")
    else:
        print("Aviso: Arquivo de metadados version.json não encontrado.")

    print("Validação bem-sucedida: Binários e metadados prontos para /docs.")
    return True

if __name__ == "__main__":
    success = validate_binaries_and_metadata()
    sys.exit(0 if success else 1)