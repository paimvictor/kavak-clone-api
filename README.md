# kavak-clone-api

## Rodar a API
```bash
python manage.py runserver
```

## Banco de Dados
Nesta api é usado o MySQL, para criar o banco de dados basta rodar:
```mysql
CREATE DATABASE kavak_api;
```
Então é necessário criar as tabelas utilizando o Django:
```bash
python manage.py migrate
```
**É necessario definir o usuario e senha em './kovak_api/settings.py' nas configurações `DATABASES`**

## Usando pre-commit para rodar linters automaticamente

Esta disponivel um hook pre-commit (.pre-commit.config.yaml), para instalar basta rodar:  
`pre-commit install --hook-type pre-commit --hook-type commit-msg`

Uma vez instalado, todos os comandos serao rodados automaticamente quando voce rodar `git commit` e sera impedido caso algum problema seja encontrado. (Voce tambem pode roda-los manualmente utilizando `pre-commit` sem argumentos.)