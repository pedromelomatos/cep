## Consulta de Endereço via CEP (Django + ViaCEP)

Este é um projeto simples feito com Django que permite ao usuário digitar um CEP e obter o endereço correspondente utilizando a API pública do [ViaCEP](https://viacep.com.br/).

### 📷 Demonstração

![Demonstração do projeto](static/imagens/print-do-projeto.png)
*Interface da aplicação ao buscar um CEP.*


### 🚀 Funcionalidades

* Interface web amigável para buscar endereços.
* Integração com API ViaCEP usando a biblioteca `requests`.
* Projeto estruturado seguindo o padrão de apps Django.

### 📂 Estrutura do Projeto

```
cep/
├── cep/            # Configurações do projeto Django
├── cepapp/         # App principal que trata a lógica da busca de CEP
├── static/         # Arquivos estáticos (CSS, imagens, prints)
├── templates/      # Templates HTML (home.html)
├── db.sqlite3      # Banco de dados SQLite
└── manage.py
```

### ▶️ Como rodar o projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/pedromelomatos/cep.git
   cd cep
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

4. Acesse em: `http://127.0.0.1:8000/`
