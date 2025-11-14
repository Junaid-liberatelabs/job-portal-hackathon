from langgraph.graph import StateGraph, START, END
# from app.llm.workflow.skills_extraction.agents.skill_extractor import SkillExtractor
from app.llm.workflow.skills_extraction.state import SkillsExtractionState
from app.core.logging_config import get_logger
from app.llm.workflow.skills_extraction.agents.skill_extractor import skill_extractor

class SkillsExtractionGraph(StateGraph):
    """
    This graph is used to extract the skills and tools from the given text.
    """
    def __init__(self):
        super().__init__(SkillsExtractionState)

        self.logger = get_logger(__name__)

        self.add_node("skill_extractor", skill_extractor.extract_skills_node)
        self.add_edge(START, "skill_extractor")
        self.add_edge("skill_extractor", END)


skill_extraction_graph = SkillsExtractionGraph()