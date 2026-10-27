# Docker Fundamentals 🐳

Repositório dedicado ao estudo prático e aprofundado dos fundamentos de Docker, abordando desde comandos essenciais, ciclo de vida de contêineres e armazenamento persistente até redes e empacotamento de aplicações reais.

---

## 📚 Laboratórios Práticos

| # | Laboratório | Tecnologias | Descrição |
|---|---|---|---|
| **01** | [Persistência de Dados com Volumes](./01-persistencia-volumes/) | Nginx, Docker Volumes | Demonstração prática da camada efêmera e montagem de volumes gerenciados. |
| **02** | [Persistência com SQLite e Flask](./02-volume-python-flask/) | Python 3.11, Flask, SQLite | Persistência de banco de dados relacional e compartilhamento de volumes via `--volumes-from`. |
| **03** | [Comunicação e Redes Customizadas](./03-redes-customizadas/) | Nginx, Docker Network, Ping | Comunicação entre contêineres via bridge, inspeção de IP e testes de resolução DNS. |
| **04** | [Redes Customizadas e Port Binding](./04-redes-e-portas/) | Nginx, Bridge Driver, Port Mapping | Gerenciamento de sub-redes, anexo dinâmico de contêineres e publicação de portas (`-p`, `-P` e restrição de loopback). |

---

## 🛠️ Tecnologias Utilizadas
- **Docker & Docker Desktop**
- **Python 3.11 (Slim)**
- **SQLite3 & Flask**
- **Nginx & Redes Bridge**
- **Bash & PowerShell**