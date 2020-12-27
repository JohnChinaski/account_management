#### TESTE TÉCNICO PARA VAGA DE DESENVOLVEDOR PYTHON

Aplicação web desenvolvida para criação e gerenciamento de contas, proprietários e transações através de endpoints API Rest utilizando o framework FastAPI.

### REQUISITOS

Para o funcionamento correto desta aplicação web, necessário algumas configurações da máquina:

- Sistema operacional Linux (não obrigatório mas recomendado)
- Docker instalado (https://docs.docker.com/get-docker/)
- Docker Compose instalado (https://docs.docker.com/compose/install/)

### PREPARAÇÃO E SUBIDA DO AMBIENTE
Após a instalação do Docker e docker-compose:

1 - Clone o repositório este repositório (branch Master) no diretório de sua preferência;

2 - Na pasta raiz do repositório que clonou, execute o seguinte comando:
>docker-compose up --build

3 - Após isso, a aplicação deve estar a funcionar!

### DOCUMENTAÇÃO DOS ENDPOINTS
Após a aplicação estiver funcionando, podemos começar a consumir os endpoints.

[Documentação das rotas](http://localhost:8000/docs)

_obs: para ter acesso a Documentação das rodas, também é necessário que a aplicação esteja funcionando._ 

####_ALGUNS PONTOS IMPORTANTES PARA UTILIZAÇÃO_

- o prefixo para utilização de TODOS os endipoints é http://localhost:8000/
- todas as operações que forem necessárias informar uma data, deve obrgatóriamente ser uma string e estar no seguinte formato:
>DD-MM-AAA ---> dia 2 dígitos, mês 2 dígitos e ano 4 dígitos


