# Laboratório: Redes Customizadas e Mapeamento de Portas no Docker

Guia prático e aprofundado sobre o gerenciamento de redes virtuais (`bridge`), conexão dinâmica de contêineres e estratégias de publicação de portas (`Port Binding`) no Docker.

---

## 🎯 Conceitos Chave

### 1. Ciclo de Vida de Redes Customizadas
- **Isolamento e Segurança:** Redes personalizadas isolam contêineres da rede padrão (`bridge`), impedindo tráfego não autorizado.
- **Drivers Suportados:** `bridge` (padrão local), `host` (usa a stack de rede direta da máquina física) e `none` (totalmente isolado sem interface de rede).
- **Conexão Dinâmica:** O comando `docker network connect` anexa contêineres em execução a redes existentes sem necessidade de reinicialização.

### 2. Mapeamento de Portas (`Publishing` vs `Expose`)
- **`EXPOSE` (Dockerfile):** Funciona como metadado/documentação indicando em qual porta a aplicação escuta, mas não abre acesso externo automaticamente.
- **`-p <host>:<container>`:** Cria regras no subsistema de rede do daemon para rotear o tráfego do host para a porta do contêiner.
- **Binding por Interface de Rede:**
  - `0.0.0.0:8080:80` (padrão): Expõe em todas as interfaces físicas e locais do host.
  - `127.0.0.1:8080:80`: Restringe o acesso exclusivamente à interface de loopback (`localhost`), garantindo que dispositivos externos na rede local não acessem o serviço.
- **`-P` (Publish All):** Mapeia automaticamente todas as portas declaradas no `EXPOSE` para portas dinâmicas e aleatórias (High Ports) no host.

---

## 🛠️ Comandos de Referência

### Gerenciamento de Redes Customizadas
```bash
# Listar redes e seus drivers
docker network ls

# Criar rede bridge personalizada
docker network create --driver bridge minha-primeira-rede

# Inspecionar detalhes de IP, Subnet e Gateway
docker network inspect minha-primeira-rede

# Iniciar contêiner já anexado à rede
docker run -d --name app --network minha-primeira-rede nginx

# Conectar contêiner existente a uma rede em tempo de execução
docker network connect minha-primeira-rede app2

# Remover rede após remoção dos contêineres conectados
docker network rm minha-primeira-rede
```

### Técnicas de Mapeamento de Portas
```bash
# 1. Publicação padrão (todas as interfaces)
docker run --name app -d -p 8080:80 nginx

# 2. Binding seguro restrito a loopback (apenas localhost)
docker run --name app -d -p 127.0.0.1:8080:80 nginx

# 3. Mapeamento de múltiplas portas
docker run --name app -d -p 8080:80 -p 443:80 nginx

# 4. Publicação em intervalo contíguo de portas
docker run --name app2 -d -p 3000-3002:3000-3002 nginx

# 5. Publicação automática de portas dinâmicas (High Ports)
docker run --name app-nginx -d -P nginx
```