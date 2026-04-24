from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes.router import InvestigatorRouter
from .nodes.tools_node import ToolsNode
from .nodes.synthesis import SynthesizerNode

def create_forensic_graph():
    # Initialize nodes
    investigator = InvestigatorRouter()
    tools = ToolsNode()
    synthesizer = SynthesizerNode()
    
    workflow = StateGraph(AgentState)

    # Add Nodes
    workflow.add_node("investigator", investigator)
    workflow.add_node("yara_scan", tools.yara_scan)
    workflow.add_node("registry_parse", tools.registry_parse)
    workflow.add_node("synthesizer", synthesizer)

    # Define Edges
    workflow.set_entry_point("investigator")
    
    workflow.add_conditional_edges(
        "investigator",
        lambda x: x["analysis_route"],
        {
            "memory_malware": "yara_scan",
            "system_registry": "registry_parse"
        }
    )
    
    workflow.add_edge("yara_scan", "synthesizer")
    workflow.add_edge("registry_parse", "synthesizer")
    workflow.add_edge("synthesizer", END)

    return workflow.compile()
