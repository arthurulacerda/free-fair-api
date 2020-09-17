# Free Fair API

## Descrição

Simples exemplo de API utilizando Flask RESTful API. A API realiza CRUD de feiras.

## Instalação

Esta API foi desenvolvida utilizando  Python 3 e em ambiente Linux (Ubuntu)

Primeiramente, instale o `virtualenv`, ferramenta utilizada para criação de ambientes Python isolados.

```
pip install virtualenv
```

Instale as dependências abaixo para realizar a conexão com MySQL, caso esteja utilizando outro SO, consulte [aqui](https://github.com/PyMySQL/mysqlclient-python) as alternativas.

```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

Realize o clone do projeto para seu repositório local.

```
git clone https://github.com/arthurulacerda/free-fair-api.git
```

Acesse o diretório, crie um ambiente com `virtualenv` e ative-o.

```
python -m venv v-env
source v-env/bin/activate
```

Faça a instalação das dependências do projeto, que se encontram em *requirements.txt*.

```
pip install -r requirements.txt
```

Realize a [instalação de MySQL](https://docs.oracle.com/javacomponents/advanced-management-console-2/install-guide/mysql-database-installation-and-configuration-advanced-management-console.htm#JSAMI122), crie um database e um usuário e atualize as informações da sua conexão com o banco de dados no arquivo `config.py`

Após finalizar a configuração do banco de dados, inicie a aplicação com o comando:

```
python app.py
```

## Instalação

Para popular o banco de dados, basta deixar a aplicação executando, e em outro terminal, executar o script:

```
python import.py
```

O script fará a leitura do arquivo CSV no diretório *data* e realizará requisições POST para adicionar os registros no banco de dados.
