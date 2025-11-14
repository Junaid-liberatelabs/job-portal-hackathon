from langgraph.graph import StateGraph, START, END
from app.llm.workflow.skill_gap_analysis.state import SkillGapAnalysisState
from app.llm.workflow.skill_gap_analysis.agents.skill_gap_analysis import skill_gap_analysis
from app.core.logging_config import get_logger

class SkillGapAnalysisGraph(StateGraph):
    def __init__(self):
        super().__init__(SkillGapAnalysisState)

        self.logger = get_logger(__name__)

        self.add_node("skill_gap_analysis", skill_gap_analysis.analyze_skill_gap_node)
        self.add_edge(START, "skill_gap_analysis")
        self.add_edge("skill_gap_analysis", END)

skill_gap_analysis_graph = SkillGapAnalysisGraph()