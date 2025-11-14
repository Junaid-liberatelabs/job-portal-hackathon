from langgraph.graph import StateGraph, START, END
from app.llm.workflow.career_roadmap.state import CareerRoadmapState
from app.llm.workflow.career_roadmap.agents.career_roadmap import career_roadmap
from app.core.logging_config import get_logger

class CareerRoadmapGraph(StateGraph):
    def __init__(self):
        super().__init__(CareerRoadmapState)

        self.logger = get_logger(__name__)

        self.add_node("career_roadmap_report", career_roadmap.create_career_roadmap_report_node)
        self.add_node("career_roadmap_graph", career_roadmap.create_career_roadmap_graph_node)
        
        self.add_edge(START, "career_roadmap_report")
        self.add_edge("career_roadmap_report", "career_roadmap_graph")
        self.add_edge("career_roadmap_graph", END)

career_roadmap_graph = CareerRoadmapGraph()