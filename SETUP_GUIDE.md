# APEX Sports Analytics - Guia de Configuracao

## Status do Projeto

Repositorio GitHub organizado com estrutura base para aplicacao APEX integrada ao Gemini.

## Arquivos Criados

1. **README.md** - Visao geral do projeto
2. **.env.example** - Variaveis de ambiente template
3. **requirements.txt** - Dependencias Python
4. **docker-compose.yml** - Orquestracao Docker (PostgreSQL, Redis, Backend)
5. **backend/main.py** - API FastAPI inicial

## Requisitos Imediatos

### 1. Configurar Chaves de API

O aplicativo Gemini APEX ja esta configurado com:
- Perplexity API Key: CONFIGURADA
- SportMonks/FlashScore API: CONFIGURADA (placeholder)
- GitHub Sync: CONECTADO ao newjsouza/Gemini-APEX.git

### 2. Obter Chaves Reais

Para dados reais e atualizados, configure:

**SportMonks API** (Recomendado para dados esportivos)
- URL: https://www.sportmonks.com/
- Dados: Confrontos, Escalacoes, Estatisticas em tempo real
- Inclui: xG, Passes, Chutes, etc.

**Alternativa: FlashScore (Web Scraping)**
- Gratuito mas exige web scraping
- Suporta: Escalacoes AO VIVO, H2H, Ratings de jogadores

### 3. Configurar Variaveis de Ambiente

```bash
cp .env.example .env
# Editar .env com suas credenciais:
# PERPLEXITY_API_KEY=sua_chave_aqui
# SPORTMONKS_API_KEY=sua_chave_aqui
```

## Proximos Passos

### Curto Prazo (Esta Semana)
1. Implementar Efeito Vina (logica de escanteios)
2. Integrar Kelly Criterion Adaptado
3. Criar modelos do banco de dados (SQLAlchemy)
4. Testar endpoints da API

### Medio Prazo (2-4 Semanas)
1. Implementar integracao com SportMonks
2. Cache inteligente com Redis
3. Sistema de notificacoes
4. Interface de chat com Perplexity

### Longo Prazo (1-3 Meses)
1. Aplicativo iOS (Swift + SwiftUI)
2. Automacao de apostas
3. Dashboard de performance
4. Analise de vide EM TEMPO REAL

## Como Iniciar Localmente

```bash
# 1. Clone o repositorio
git clone https://github.com/newjsouza/Gemini-APEX.git
cd Gemini-APEX

# 2. Configure o ambiente
cp .env.example .env
# Edite .env com suas chaves

# 3. Inicie os servicos
docker-compose up -d

# 4. Acesse a API
# Health Check: http://localhost:8000/health
# Docs: http://localhost:8000/docs
```

## Arquitetura

```
APEX SPORTS ANALYTICS
|
+-- Frontend (Gemini Web App React)
|   |-- Dashboard
|   |-- Chat AI
|   |-- Configuracoes & API
|
+-- Backend (FastAPI Python)
|   |-- API REST
|   |-- Logica de Negocio (Kelly, Vina)
|   |-- Integracao com dados esportivos
|
+-- Banco de Dados
|   |-- PostgreSQL (dados persistentes)
|   |-- Redis (cache inteligente)
|
+-- Integracao Externa
    |-- Perplexity API (IA conversacional)
    |-- SportMonks API (dados em tempo real)
```

## Repositorio GitHub

Todos os arquivos estao sincronizados em: https://github.com/newjsouza/Gemini-APEX

Estrutura:
```
Gemini-APEX/
|- backend/
|  |- main.py (API FastAPI)
|- .env.example
|- requirements.txt
|- docker-compose.yml
|- README.md
|- SETUP_GUIDE.md
```
