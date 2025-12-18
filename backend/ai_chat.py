import aiohttp
import json
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class APEXAIChat:
    """Classe central inteligente para gerenciar chat com Perplexity AI"""
    
    def __init__(self):
        self.api_key = os.getenv("PERPLEXITY_API_KEY")
        self.base_url = "https://api.perplexity.ai"
        self.model = "llama-3.1-sonar-large-128k-online"
        self.conversation_memory = {}
        self.max_memory = 20
        self.analysis_cache = {}
        
    async def chat(self, user_id: str, message: str, context: Optional[Dict] = None) -> Dict:
        """Processa mensagem com contexto inteligente"""
        try:
            history = self._get_history(user_id)
            system_prompt = self._build_system_prompt(history)
            full_prompt = f"{message}"
            if context:
                full_prompt += f"\n\nContexto: {json.dumps(context, ensure_ascii=False)}"
            
            response = await self._call_perplexity(system_prompt, full_prompt)
            self._save_to_memory(user_id, message, response)
            recommendations = self._extract_recommendations(response)
            
            return {
                "response": response,
                "recommendations": recommendations,
                "conversation_turns": len(history),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Erro no chat: {str(e)}")
            raise
    
    async def analyze_game(self, game_data: Dict) -> Dict:
        """Analisa dados de um jogo para apostas"""
        cache_key = f"{game_data.get('league')}_{game_data.get('teams', [])}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        prompt = f"""Analise este jogo para apostas esportivas:
Campeonato: {game_data.get('league')}
Times: {game_data.get('teams')}
Odds: {game_data.get('odds')}

Forneca:
1. Predicao de resultado
2. Probabilidades estimadas
3. Aposta recomendada
4. Nivel de confianca
5. Fatores de risco"""
        
        response = await self._call_perplexity(
            "Voce eh um especialista em apostas esportivas.",
            prompt
        )
        
        analysis = {
            "game": game_data,
            "analysis": response,
            "timestamp": datetime.now().isoformat()
        }
        
        self.analysis_cache[cache_key] = analysis
        return analysis
    
    def get_user_history(self, user_id: str) -> List[Dict]:
        """Retorna historico do usuario"""
        return self.conversation_memory.get(user_id, [])
    
    def clear_history(self, user_id: str):
        """Limpa historico"""
        if user_id in self.conversation_memory:
            del self.conversation_memory[user_id]
    
    def get_stats(self) -> Dict:
        """Retorna estatisticas"""
        return {
            "active_users": len(self.conversation_memory),
            "total_turns": sum(len(m) for m in self.conversation_memory.values()),
            "cached": len(self.analysis_cache),
            "timestamp": datetime.now().isoformat()
        }
    
    def _build_system_prompt(self, history: List[Dict]) -> str:
        """Constroi prompt com historico"""
        prompt = "Voce eh o APEX AI, especialista em apostas esportivas. Forneca analises inteligentes."
        return prompt
    
    async def _call_perplexity(self, system: str, user_msg: str) -> str:
        """Chama Perplexity API"""
        async with aiohttp.ClientSession() as session:
            headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
            payload = {"model": self.model, "messages": [{"role": "system", "content": system}, {"role": "user", "content": user_msg}], "max_tokens": 1000}
            async with session.post(f"{self.base_url}/chat/completions", headers=headers, json=payload) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data["choices"][0]["message"]["content"]
                raise Exception(f"API error: {resp.status}")
    
    def _extract_recommendations(self, response: str) -> List[str]:
        """Extrai recomendacoes"""
        recommendations = []
        for line in response.split('\n'):
            if any(kw in line.lower() for kw in ['recomendo', 'sugiro', 'aposte']):
                if len(line.strip()) > 15:
                    recommendations.append(line.strip())
        return recommendations[:5]
    
    def _save_to_memory(self, user_id: str, message: str, response: str):
        """Salva no historico"""
        if user_id not in self.conversation_memory:
            self.conversation_memory[user_id] = []
        self.conversation_memory[user_id].append({"role": "user", "content": message, "timestamp": datetime.now().isoformat()})
        self.conversation_memory[user_id].append({"role": "assistant", "content": response, "timestamp": datetime.now().isoformat()})
        if len(self.conversation_memory[user_id]) > self.max_memory:
            self.conversation_memory[user_id] = self.conversation_memory[user_id][-self.max_memory:]
    
    def _get_history(self, user_id: str) -> List[Dict]:
        """Recupera historico"""
        return self.conversation_memory.get(user_id, [])

# Instancia global
apex_ai = APEXAIChat()
