from langgraph.graph import StateGraph, START, END
from app.llm.workflow.cv_generation.state import CVGenerationState
from app.llm.workflow.cv_generation.agents.cv_generator import cv_generator
from app.core.logging_config import get_logger


class CVGenerationGraph(StateGraph):
    def __init__(self):
        super().__init__(CVGenerationState)

        self.logger = get_logger(__name__)

        self.add_node("cv_generation", cv_generator.generate_cv_node)
        self.add_edge(START, "cv_generation")
        self.add_edge("cv_generation", END)


cv_generation_graph = CVGenerationGraph()
