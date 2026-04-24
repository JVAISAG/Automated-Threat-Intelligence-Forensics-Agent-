from langchain_google_genai import ChatGoogleGenerativeAI
from ..state import AgentState
from ...core.config import settings

class SynthesizerNode:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GOOGLE_API_KEY
        )

    async def __call__(self, state: AgentState):
        artifacts = state["raw_artifacts"]
        metadata = state["metadata"]
        
        prompt = (
            "You are a Senior Threat Intelligence Analyst. Synthesize the following forensic artifacts "
            f"and file metadata ({metadata}) into a professional Threat Intelligence Report.\n\n"
            f"Artifacts: {artifacts}\n\n"
            "The report should include:\n"
            "1. Executive Summary\n"
            "2. Technical Findings\n"
            "3. Risk Assessment\n"
            "4. Recommendations"
        )
        
        response = await self.llm.ainvoke(prompt)
        return {"final_report": response.content}
