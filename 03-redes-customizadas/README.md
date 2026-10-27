# Laboratório: Redes no Docker e Comunicação entre Contêineres

Demonstração prática dos drivers de rede do Docker, ciclo de vida da rede padrão (`bridge`), inspeção de endereçamento IP e a limitação de resolução de nomes (DNS interno).

---

## 🎯 Objetivos de Aprendizagem

1. **Exploração de Drivers de Rede:** Compreender as redes pré-configuradas do daemon (`bridge`, `host`, `none`) via `docker network ls`.
2. **Criação de Redes Bridge:** Provisionamento de redes customizadas com `docker network create`.
3. **Inspeção de Contêineres:** Extrair endereços IP privados atribuídos na interface bridge usando `docker container inspect`.
4. **Comunicação Inter-Contêiner:** Validar o tráfego de pacotes ICMP (`ping`) e requisições HTTP (`curl`) entre contêineres independentes.
5. **Limitação de DNS na Bridge Padrão:** Evidenciar que contêineres na rede padrão (`bridge`) comunicam-se apenas via endereço IP direto, sem suporte nativo a resolução por hostname/nome do contêiner.

---

## 🛠️ Tecnologias Utilizadas

- **Servidor Web:** Nginx 1.29
- **Diagnóstico de Rede:** `iputils-ping` & `curl`
- **Docker Networking:** Driver Bridge e Network Inspection

---

## 📂 Arquivos do Laboratório

```text
03-redes-customizadas/
├── Dockerfile         # Nginx com pacote iputils-ping instalado
├── index.html         # Página estática para validação de requisições
└── README.md          # Documentação do laboratório
```

---

## 🧪 Comandos e Roteiro de Testes

### 1. Inspeção e Criação de Redes
```bash
# Listar redes disponíveis
docker network ls

# Criar uma rede customizada baseada no driver bridge
docker network create minha-rede
```

### 2. Construção das Imagens
```bash
# Imagem contendo 'Olá do container 1'
docker build -t app:1.0 .

# Ajuste no index.html para 'Olá do container 2' e rebuild
docker build -t app:2.0 .
```

### 3. Execução dos Contêineres (Rede Bridge Padrão)
```bash
docker run --name container1 -d app:1.0
docker run --name container2 -d app:2.0
```

### 4. Teste de Comunicação e Resolução de Nomes
```bash
# Obter o endereço IP atribuído ao container2
docker container inspect container2

# Acessar a CLI do container1
docker exec -it container1 bash

# Teste 1: Ping direto via IP (Comunicação estabelecida com sucesso)
ping <IP_DO_CONTAINER_2>

# Teste 2: Requisição HTTP interna
curl <IP_DO_CONTAINER_2>

# Teste 3: Ping via nome do contêiner (Falha esperada na bridge default por falta de DNS interno)
ping container2
exit
```