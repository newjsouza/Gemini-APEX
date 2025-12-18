# APEX AI Chat - Melhorias de Inteligencia Artificial

## Resumo das Melhorias (v2.0.0)

O APEX AI Chat agora possui inteligencia artificial avancada para analise de apostas esportivas, com capacidades de aprendizado contextual e recomendacoes inteligentes.

## Arquitetura Melhorada

### Componentes Principais

1. **APEXAIChat Class** (ai_chat.py)
   - Gerenciamento centralizado de chat com IA
   - Integracao com Perplexity AI (llama-3.1-sonar)
   - Memoria conversacional persistente
   - Cache inteligente de analises

2. **FastAPI Backend** (main.py)
   - 5 novos endpoints REST para chat inteligente
   - Suporte a contexto de apostas em tempo real
   - Historico completo de conversas por usuario
   - Estatisticas do sistema

## Funcionalidades Principais

### 1. Chat Inteligente com Memoria
```python
POST /api/v1/chat
{
  "user_id": "user_123",
  "message": "Analise o jogo Barcelona vs Real Madrid",
  "context": { /* contexto adicional */ },
  "game_data": { /* dados do jogo */ }
}
```

**Features:**
- Mantém historico de ate 20 turnos por usuario
- Sistema de prompts dinamicos baseado em historico
- Extracacao automatica de recomendacoes
- Respostas contextualizadas

### 2. Analise Inteligente de Jogos
```python
POST /api/v1/analyze-game
{
  "sport": "football",
  "league": "Premier League",
  "teams": ["Manchester City", "West Ham"],
  "odds": { "home": 1.5, "away": 6.0, "draw": 4.2 },
  "recent_data": { /* dados recentes */ }
}
```

**Analisa:**
- Form atual dos times
- Historico de encontros
- Lesoes e suspensoes
- Condicoes climaticas
- Padroes estatisticos

### 3. Gerenciamento de Historico
```python
GET /api/v1/chat/history/{user_id}
DELETE /api/v1/chat/history/{user_id}
```

- Recupera conversas anteriores
- Limpa historico quando necessario
- Persistencia de dados com timestamps

### 4. Estatisticas do Sistema
```python
GET /api/v1/stats
```

Retorna:
- Usuarios ativos
- Total de turnos de conversa
- Analises em cache
- Status do modelo IA

## Tecnologias Utilizadas

- **Framework**: FastAPI (Python)
- **IA**: Perplexity AI API (llama-3.1-sonar-128k-online)
- **Async**: aiohttp para requisicoes HTTP asincronas
- **Validacao**: Pydantic BaseModel

## Melhorias Técnicas

### 1. Inteligencia Conversacional
- Prompts dinamicos que variam baseado no historico
- Extracao automatica de recomendacoes via keywords
- Contexto multi-turno para analises coerentes

### 2. Otimizacoes de Performance
- Cache de analises para evitar requisicoes duplicadas
- Limite de historico para gerenciar memoria
- Requisicoes asincronas sem bloqueio

### 3. Tratamento Robusto de Erros
- Validacao de entrada com Pydantic
- Tratamento de excecos em todos endpoints
- Logging detalhado para debugging

## Como Usar

### 1. Chat Basico
```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user_001",
    "message": "Qual time tem maior chance no proximo jogo?",
    "context": {"tournament": "Campeonato Brasileiro"}
  }'
```

### 2. Analise de Jogo
```bash
curl -X POST http://localhost:8000/api/v1/analyze-game \
  -H "Content-Type: application/json" \
  -d '{
    "sport": "football",
    "league": "Premier League",
    "teams": ["Manchester City", "Liverpool"],
    "odds": {"home": 1.8, "away": 4.0, "draw": 3.5}
  }'
```

### 3. Recuperar Historico
```bash
curl http://localhost:8000/api/v1/chat/history/user_001
```

## Variaveis de Ambiente Necessarias

```bash
PERPLEXITY_API_KEY=sk_live_xxxxxxxxxxxx
APP_HOST=0.0.0.0
APP_PORT=8000
APP_ENV=production
```

## Proximas Melhorias Planejadas

- [ ] Integracao com banco de dados PostgreSQL para persistencia
- [ ] Redis para cache distribuido
- [ ] WebSocket para chat em tempo real
- [ ] Analise de padroes com machine learning
- [ ] Dashboard de metricas em tempo real
- [ ] Multi-idioma suporte
- [ ] Rate limiting e autenticacao JWT

## Commits Recentes

1. **Add APEXAIChat class**: Implementacao da classe central de IA
2. **Implement chat and game analysis endpoints**: Adicao dos endpoints REST

## Status

✅ Versao 2.0.0 em producao
✅ Perplexity AI integrado
✅ Chat com memoria persistente
✅ Analise de jogos implementada
✅ API REST completa

---

**Desenvolvedor**: newjsouza
**Data**: Dezembro 18, 2025
**Versao**: 2.0.0
