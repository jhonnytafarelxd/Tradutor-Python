import json
import shutil
from deep_translator import GoogleTranslator

# Caminho do arquivo original
arquivo_json = "en.json"

# Backup do arquivo original
backup_json = arquivo_json.replace(".json", "_old.json")
shutil.copyfile(arquivo_json, backup_json)
print(f"[✔] Backup criado: {backup_json}")

# Ler conteúdo original
with open(arquivo_json, "r", encoding="utf-8") as file:
    dados = json.load(file)

# Função para traduzir texto
def traduzir(texto):
    if not texto or not isinstance(texto, str) or texto.strip() == "":
        return texto
    try:
        return GoogleTranslator(source="en", target="pt").translate(texto)
    except Exception as e:
        print(f"[!] Erro ao traduzir '{texto}': {e}")
        return texto

# Traduz todos os valores do dicionário
def traduzir_dict(dados):
    if isinstance(dados, dict):
        return {k: traduzir_dict(v) for k, v in dados.items()}
    elif isinstance(dados, list):
        return [traduzir_dict(v) for v in dados]
    elif isinstance(dados, str):
        return traduzir(dados)
    else:
        return dados

dados_traduzidos = traduzir_dict(dados)

# Salvar JSON traduzido sobrescrevendo o original
with open(arquivo_json, "w", encoding="utf-8") as file:
    json.dump(dados_traduzidos, file, indent=2, ensure_ascii=False)

print(f"[✔] Tradução concluída. Arquivo salvo: {arquivo_json}")
