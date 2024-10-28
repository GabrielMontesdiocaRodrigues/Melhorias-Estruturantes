# Melhorias Estruturantes

Criada uma API que permite realizar web scraping de informações de uma página web pública e processar os dados de forma assíncrona utilizando filas de mensagens. A API é escalável e preparada para ser implantada em um ambiente Docker com RabbitMQ e Redis.

## Pré-Requisitos

* Possui Docker instalado e operacional em sua máquina
* Possuir o aplicativo desktop Another Redis Desktop Manager para visualização das armazenadas nos Redis

## Como Utilizar 

1. Copiar o código para seu computador

   * Acessar o repositório do GitHub : ``https://github.com/GabrielMontesdiocaRodrigues/Melhorias-Estruturantes``
   * Clicar no botão verde(`<Code>`) e fazer download do projeto
   * Acessar a pasta onde o projeto está alocado com um prompt de comando
2. Criando containers e  acessando a API

   * No prompt de comando dentro da para  `` ./Melhorias-Estruturantes-main`` digitar a seguinte linah de código :

     ```bash
     docker-compose up --build
     ```
   * Após a aplicação no ar poderá acessar o seguinte link : ``http://localhost:8000/docs``
3. Acessando o Redis via Another Redis Desktop Manager
