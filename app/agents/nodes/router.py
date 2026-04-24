from langchain_google_genai import ChatGoogleGenerativeAI
from ..state import AgentState
from ...core.config import settings

class InvestigatorRouter:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GOOGLE_API_KEY
        )

    async def __call__(self, state: AgentState):
        metadata = state["metadata"]
        prompt = (
            f"You are a Senior Lead Forensic Investigator. Analyze these file attributes: {metadata}. "
            "Decide if this file should be routed for 'memory_malware' analysis (YARA) or 'system_registry' analysis. "
            "Respond with ONLY the string 'memory_malware' or 'system_registry'."
        )
        
        response = await self.llm.ainvoke(prompt)
        route = response.content.strip().lower()
        
        # Fallback logic
        if "malware" in route or "memory" in route:
            route = "memory_malware"
        elif "registry" in route or "system" in route:
            route = "system_registry"
        else:
            route = "memory_malware" # Default
            
        return {"analysis_route": route}
