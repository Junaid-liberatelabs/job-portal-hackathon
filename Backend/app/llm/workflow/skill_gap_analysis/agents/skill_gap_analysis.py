from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from app.llm.prompts.load_prompt import load_yaml_prompt
from langchain_core.messages import SystemMessage, HumanMessage

from app.llm.workflow.skill_gap_analysis.state import SkillGapAnalysisState

class SkillGapAnalysis:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.llm = ChatGroq(model_name="openai/gpt-oss-20b")
        self.llm_gpt= ChatOpenAI(model_name="gpt-4.1-nano", max_retries=3)
        self.fallback_llm = self.llm.with_fallbacks([self.llm_gpt])
        self.system_prompt = load_yaml_prompt(path="skill_gap_analysis/skill_gap_analysis", key="SYSTEM_PROMPT")
        self.user_prompt = load_yaml_prompt(path="skill_gap_analysis/skill_gap_analysis", key="USER_PROMPT")

    def analyze_skill_gap_node(self, state: SkillGapAnalysisState):
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.user_prompt.format(user_skills=state.user_profile_data.skills, job_description=state.user_applied_job_data))
        ]
        response = self.fallback_llm.invoke(messages)
        state.gap_analysis_report = response.content
        return state


skill_gap_analysis = SkillGapAnalysis()