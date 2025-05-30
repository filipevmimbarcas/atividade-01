# Aplicação Flask: Contador de Visitas com PostgreSQL
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python)
![Flask](https://img.shields.io/badge/Flask-^2.0-lightgrey.svg?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1.svg?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Conteinerização-blue.svg?logo=docker)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-Orquestração_Local-informational.svg?logo=docker)
![Status](https://img.shields.io/badge/Status-Concluído-green.svg) 

 Uma aplicação web simples desenvolvida em **Flask** que registra e exibe o número total de visitas a uma rota específica. Os dados são persistidos em um banco de dados **PostgreSQL**. Todo o ambiente da aplicação (servidor web e banco de dados) é conteinerizado com **Docker** e orquestrado localmente via **Docker Compose**, o que facilita a configuração, o desenvolvimento e a execução.


---

## Estrutura do Projeto

├── app.py                  <br>
├── requirements.txt        <br>
├── Dockerfile              <br>
└── docker-compose.yml      <br>

---

## Como Executar a Aplicação

Siga os passos abaixo para colocar a aplicação em funcionamento em sua máquina local.

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu sistema:

* **Docker Engine:** [Instruções de Instalação](https://docs.docker.com/engine/install/)
* **Docker Compose:** [Instruções de Instalação](https://docs.docker.com/compose/install/) 

### 1. Clonar o Repositório

Primeiro, clone o repositório para sua máquina local e navegue até o diretório do projeto:

```bash
git clone https://github.com/filipevmimbarcas/atividade-01.git
cd atividade-01

```

### 2. Iniciar os Containers com Docker Compose
No terminal, dentro do diretório raiz do projeto (onde o docker-compose.yml está), execute o seguinte comando:

```bash
docker-compose up --build -d 
```

- docker compose up: Inicia os serviços definidos no docker-compose.yml.
- build: Garante que a imagem da aplicação Flask seja construída (ou reconstruída) a partir do Dockerfile antes de iniciar o container.
- d: Inicia os containers em modo "detached" (em segundo plano).

### 3.Verificar status dos containers
Para confirmar que todos os containers estão rodando corretamente, execute:

```bash
docker-compose ps
```

### 4. Acessar a aplicação
```bash
http://localhost:5000/visitantes
```

Você deverá ver uma resposta JSON indicando o número total de visitas, por exemplo: {"total_visitas":1}. Cada vez que você atualizar a página, o contador de visitas no banco de dados aumentará.


![app-flask](https://github.com/user-attachments/assets/6e53e01b-b83e-4436-bae1-7d711616bf51)
