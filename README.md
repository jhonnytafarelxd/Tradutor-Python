<!-- Banner -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-Stable-success" alt="Status">
</p>

<h1 align="center">🌐 Auto Translator for PHP & JSON Files</h1>

<p align="center">
  Scripts simples e poderosos em <b>Python</b> para traduzir automaticamente arquivos de idioma 
  (<code>lang.php</code> e <code>en.json</code>) do <b>inglês → português 🇧🇷</b>, usando o 
  <a href="https://pypi.org/project/deep-translator/">deep_translator</a> com o Google Translator.
</p>

---

## ✨ Principais recursos

- 🔁 Tradução automática e rápida (EN → PT)
- 🧩 Suporte a dois formatos:
  - `traduz_php.py` → traduz arquivos PHP no formato `'chave' => 'valor'`
  - `traduz_json.py` → traduz arquivos JSON mantendo a estrutura original
- 💾 Cria **backup automático** antes de modificar o original
- 🧠 Mantém a estrutura e a codificação UTF-8 intactas
- ⚙️ Fácil de usar — basta um comando no terminal

---

## ⚙️ Como usar

1. **Instale o deep_translator**  
   ```bash
   pip install deep-translator
   ```

2. **Coloque o arquivo a ser traduzido** (`lang.php` ou `en.json`) na mesma pasta do script.

3. **Execute o script desejado:**
   ```bash
   python traduz_php.py
   # ou
   python traduz_json.py
   ```

4. O script criará um backup (`_old`) e substituirá o arquivo original pela versão traduzida.

---

## 🧾 Exemplo

**Antes (`lang.php`):**
```php
'welcome' => 'Welcome to our website',
```

**Depois:**
```php
'welcome' => 'Bem-vindo ao nosso site',
```

---

## 💡 Dica rápida

Quer traduzir para outro idioma?  
Basta mudar o idioma de destino no código:

```python
GoogleTranslator(source='en', target='es')  # Traduz para espanhol
GoogleTranslator(source='en', target='fr')  # Traduz para francês
```

---

## 📁 Estrutura do projeto

```
.
├── traduz_php.py      # Traduz arquivos PHP ('chave' => 'valor')
├── traduz_json.py     # Traduz arquivos JSON mantendo a estrutura
└── README.md          # Este arquivo ❤️
```

---

## ⚠️ Observações

- É necessário ter **conexão com a internet** (Google Translator online).  
- Sempre é criado um **backup automático** antes da tradução.  
- As traduções são automáticas — revise o resultado final antes de uso em produção.

---

## 👨‍💻 Autor

**Jhonny Tafarel Bonifacio de Oliveira**  
---

## 🪪 Licença

Distribuído sob a **MIT License**.  
Sinta-se livre para usar, modificar e compartilhar. 💙

<p align="center">Feito com 💻, ☕ e um toque de 🇧🇷</p>
