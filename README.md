# APEX SPORTS ANALYTICS - Sistema de Analise de Apostas Esportivas

## Visao Geral

APEX eh um sistema de IA especializado em analise de apostas esportivas, focado em escanteios com dados reais.

## Stack Tecnologico

- Backend: FastAPI (Python)
- Database: PostgreSQL
- Cache: Redis
- IA: Perplexity API
- Frontend: iOS (Swift)

## Estrutura

```
Gemini-APEX/
|-- backend/           # API FastAPI
|-- data/              # Scripts de coleta
|-- models/            # Logica APEX-ML
|-- config/            # Configuracoes
|-- tests/             # Testes
|-- docker-compose.yml
|-- requirements.txt
```

## Comecando

1. Clone o repositorio
2. Configure .env com suas credenciais
3. Execute `docker-compose up -d`
4. Inicialize o banco de dados
