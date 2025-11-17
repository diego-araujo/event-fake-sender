# Gerador de Notificações

Aplicação web para facilitar o envio de requisições JSON para um backend, utilizando Flask, Nginx e Docker Compose.

## Estrutura do Projeto

```
demo-evento/
├── app/
│   ├── app.py              # Aplicação Flask
│   └── templates/
│       └── index.html      # Interface web com Material Design
├── json_files/             # Arquivos JSON de notificações
│   ├── transito.json
│   ├── video.json
│   └── acidente.json
├── nginx/
│   └── nginx.conf          # Configuração do Nginx
├── Dockerfile.flask        # Dockerfile para Flask
├── Dockerfile.nginx        # Dockerfile para Nginx
├── docker-compose.yml      # Orquestração dos containers
└── requirements.txt        # Dependências Python
```

## Funcionalidades

A aplicação permite enviar três tipos de notificações:

1. **Notificação de Trânsito** - Lê `transito.json` e envia para o backend
2. **Notificação de Vídeo** - Lê `video.json` e envia para o backend
3. **Notificação de Acidente** - Lê `acidente.json` e envia para o backend

## Como Usar

### Pré-requisitos

- Docker
- Docker Compose

### Executar a Aplicação

1. Clone ou navegue até o diretório do projeto:
```bash
cd demo-evento
```

2. Execute o Docker Compose:
```bash
docker-compose up --build
```

3. Acesse a aplicação no navegador:
```
http://localhost
```

### Parar a Aplicação

```bash
docker-compose down
```

## Personalização

### Modificar Arquivos JSON

Os arquivos JSON estão localizados em `json_files/`. Você pode editá-los conforme necessário:

- `json_files/transito.json` - Dados de notificação de trânsito
- `json_files/video.json` - Dados de notificação de vídeo
- `json_files/acidente.json` - Dados de notificação de acidente

### Integrar com Backend

Para integrar com seu backend real, edite o arquivo `app/app.py` e modifique a função `send_notification()` para fazer uma requisição HTTP para seu backend:

```python
import requests

# Dentro da função send_notification()
response = requests.post('https://seu-backend.com/api/notificacoes', json=json_data)
```

## Tecnologias Utilizadas

- **Flask** - Framework web Python
- **Nginx** - Servidor web e proxy reverso
- **Docker** - Containerização
- **Material Design** - Framework de UI
- **Material Icons** - Ícones

## Portas

- **80** - Nginx (acesso público)
- **5000** - Flask (interno, acessível apenas via Nginx)

