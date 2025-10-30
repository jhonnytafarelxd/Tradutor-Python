import re
import shutil
from deep_translator import GoogleTranslator

# Caminho do arquivo original
arquivo_php = "lang.php"

# Backup do arquivo original
backup_php = arquivo_php.replace(".php", "_old.php")
shutil.copyfile(arquivo_php, backup_php)
print(f"[✔] Backup criado: {backup_php}")

# Ler conteúdo original
with open(arquivo_php, "r", encoding="utf-8") as file:
    conteudo = file.read()

# Expressão regular para localizar as strings: 'chave' => 'valor'
padrao = r"'(.*?)'\s*=>\s*'(.*?)'"

# Função para traduzir os valores
def traduzir(valor):
    if not valor or valor.strip() == '':
        return valor
    try:
        return GoogleTranslator(source='en', target='pt').translate(valor)
    except Exception as e:
        print(f"[!] Erro ao traduzir '{valor}': {e}")
        return valor

# Substituir os valores traduzidos
def traduzir_array(match):
    chave = match.group(1)
    valor = match.group(2)
    valor_traduzido = traduzir(valor)
    return f"'{chave}' => '{valor_traduzido}'"

conteudo_traduzido = re.sub(padrao, traduzir_array, conteudo)

# Salvar conteúdo traduzido sobrescrevendo o original
with open(arquivo_php, "w", encoding="utf-8") as file:
    file.write(conteudo_traduzido)

print(f"[✔] Tradução concluída. Arquivo salvo: {arquivo_php}")
