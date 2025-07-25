# 🧰 BD‑NoSql

> Projeto desenvolvido para a disciplina **Banco de Dados II**, do curso de **Análise e Desenvolvimento de Sistemas** — IFPE.

Este repositório demonstra o uso prático de bancos **NoSQL** em contextos de **cache** e **mensageria**, utilizando **MongoDB**, **Redis** e **RabbitMQ**. O sistema foi implementado com uma interface em linha de comando (CLI) e uma interface gráfica simples com Tkinter, abordando o ciclo completo de um pedido: criação, armazenamento, envio e notificação.

---

## 📁 Estrutura de arquivos

```
pedido-system/
│
├── main.py                # Menu principal (CLI)
├── interface.py           # Interface gráfica com Tkinter
├── pedido_service.py      # CRUD de pedidos + envio via RabbitMQ
├── notificacao_service.py # Consumidor da fila RabbitMQ
├── cache.py               # Operações com Redis
├── database.py            # Conexão com MongoDB
├── models.py              # Modelo de dados do pedido
└── requirements.txt       # Dependências do projeto
```

---

## 🚀 Tecnologias utilizadas

- **Python 3**  
- **MongoDB** – banco de dados NoSQL  
- **Redis** – sistema de cache  
- **RabbitMQ** – mensageria entre serviços  
- **Tkinter** – interface gráfica (GUI)

---

## ⚙️ Como executar

```bash
# Clone o repositório
git clone https://github.com/nos-4/BD-NoSql.git

# Acesse a pasta
cd BD-NoSql/pedido-system

# Crie e ative um ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Execução por CLI

```bash
python main.py
```

Siga o menu para criar, listar, atualizar ou remover pedidos.

### Execução da interface gráfica

```bash
python interface.py
```

Interface gráfica simples que permite criar e consultar pedidos.

---

## ✨ Funcionalidades principais

- [x] CRUD de pedidos (criação, listagem, atualização e remoção)  
- [x] Armazenamento em MongoDB  
- [x] Cache com Redis para otimizar leituras  
- [x] Envio de mensagens com RabbitMQ  
- [x] Interface em linha de comando (CLI)  
- [x] Interface gráfica com Tkinter  

---

## 🔁 Fluxo do sistema

1. O usuário interage com o sistema (via CLI ou GUI).
2. Dados dos pedidos são validados e armazenados no MongoDB.
3. Redis é utilizado como cache para consultas rápidas.
4. A cada novo pedido, uma mensagem é enviada à fila RabbitMQ.
5. O serviço consumidor (`notificacao_service.py`) processa a fila de pedidos para simular notificações.

---

## 📦 Componentes principais

- `main.py`: menu principal para uso via terminal.  
- `interface.py`: interface gráfica com suporte a criação e consulta de pedidos.  
- `pedido_service.py`: implementa o CRUD e lógica de envio ao RabbitMQ.  
- `notificacao_service.py`: serviço consumidor da fila de mensagens.  
- `cache.py`: interface com Redis (leitura e gravação em cache).  
- `database.py`: conexão e operações com MongoDB.  
- `models.py`: definição da estrutura do pedido.

---

## 🤝 Contribuições

Este projeto foi desenvolvido para fins acadêmicos, mas sinta-se à vontade para sugerir melhorias ou usar como base para estudos e aplicações semelhantes.

---

## 📄 Licença

Este projeto está sob a licença **MIT**.

---

## 👨‍💻 Autoria

Desenvolvido por estudantes do curso de **Análise e Desenvolvimento de Sistemas – IFPE**, para a disciplina de **Banco de Dados II**:

- [Adriel Rodrigues Gomes da Silva](https://github.com/Adriel-grs)  
- [Ana Clara Ferreira Monte](https://github.com/anacfmonte)  
- [Eveline Síntia Matos e Silva](https://github.com/EvelineSintia)  
- [Samara Araújo Almeida](https://github.com/s4mnara)
