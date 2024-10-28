
# Melhorias Estruturantes

Esta API permite realizar web scraping de informações de páginas web públicas e processar os dados de forma assíncrona utilizando filas de mensagens. A API é escalável e preparada para ser implantada em um ambiente Docker com RabbitMQ e Redis.

## Pré-Requisitos

Antes de começar, certifique-se de que você possui os seguintes itens instalados e funcionando em sua máquina:

- **Docker**: Certifique-se de que o Docker está instalado e operacional.
- **Redis**: Instale o Redis.
- **Another Redis Desktop Manager**: Utilize este aplicativo para visualizar os dados armazenados no Redis. Você pode baixá-lo [aqui](https://github.com/qishibo/AnotherRedisDesktopManager/releases).

## Como Utilizar

### 1. Copiar o Código para Seu Computador

- Acesse o [repositório no GitHub](https://github.com/GabrielMontesdiocaRodrigues/Melhorias-Estruturantes).
- Clique no botão verde (`<Code>`) e faça o download do projeto.
- Acesse a pasta onde o projeto foi alocado usando um prompt de comando.

### 2. Criando Containers e Acessando a API

No prompt de comando, dentro da pasta `Melhorias-Estruturantes-main`, execute o seguinte comando:

```bash
docker-compose up --build
```

### 3. Acessando o Redis via Another Redis Desktop Manager

- Crie uma nova conexão no aplicativo usando as portas padrão e a seguinte senha: `1q2w3e4r`.
- Assim, você poderá visualizar as informações salvas no Redis pela API.

### 4. Acessando a API e Enviando Dados

- Após a aplicação estar em execução, você pode acessar a [API](http://localhost:8000/docs).
- Para enviar um CNPJ, utilize o endpoint `POST /scrape` clicando no botão `<Try it out>`.
- Após enviar o CNPJ, anote o `task_id` retornado e utilize-o no endpoint `GET /results/{task_id}` clicando novamente no botão `<Try it out>`.
- Isso deverá retornar os dados do CNPJ em formato JSON.

## Conclusão

A API desenvolvida atende eficientemente à proposta inicial. Para verificar se a API está funcionando corretamente, você pode executar o programa `test.py`, que enviará CNPJs de forma assíncrona para a API.

### Pré-requisito para o Programa de Teste

Certifique-se de ter a biblioteca `aiohttp` instalada, pois ela não está incluída no arquivo `requirements.txt`. Para instalá-la, execute o seguinte comando em um prompt de comando:

```bash
pip install aiohttp
```
