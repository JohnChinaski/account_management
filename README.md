#### TESTE TÉCNICO PARA VAGA DE DESENVOLVEDOR PYTHON

Aplicação web desenvolvida para criação e gerenciamento de contas, proprietários e transações através de endpoints API Rest utilizando o framework FastAPI.

### REQUISITOS

Para o funcionamento correto desta aplicação web, é necessário algumas configurações da máquina:

- Sistema operacional Linux (não obrigatório, mas recomendado)
- Docker instalado (https://docs.docker.com/get-docker/)
- Docker Compose instalado (https://docs.docker.com/compose/install/)

### PREPARAÇÃO DO AMBIENTE E EXECUÇÃO DA APLICAÇÃO
Após a instalação do Docker e docker-compose:

1 - Clone este repositório (branch master) no diretório de sua preferência;

2 - Na pasta raiz do repositório que clonou, execute o seguinte comando:
>docker-compose up --build

3 - Após isso, a aplicação deve estar em execução!

- Para encerrar a aplicação, basta abrir o terminal onde a aplicação esta em execução e pressionar as teclas CTRL + C.

### DOCUMENTAÇÃO DOS ENDPOINTS
Após o funcionamento da aplicação, podemos começar a consumir os endpoints.

[Documentação das rotas](http://localhost:8000/docs)

_Obs: para ter acesso à Documentação das rodas, também é necessário que a aplicação esteja em execução._ 

####_ALGUNS PONTOS IMPORTANTES PARA UTILIZAÇÃO_

- o prefixo para utilização de TODOS os endpoints é http://localhost:8000/
- todas as operações que sejam necessárias informar uma data deve, obrigatóriamente, ser uma string e estar no seguinte formato:
>"DD-MM-AAAA" ---> dia (2 dígitos), mês (2 dígitos) e ano (4 dígitos).


