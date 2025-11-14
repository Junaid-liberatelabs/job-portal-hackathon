from pydantic import BaseModel
from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from app.llm.prompts.load_prompt import load_yaml_prompt
from langchain_core.messages import SystemMessage, HumanMessage

from app.llm.workflow.skills_extraction.state import SkillsExtractionState, AnalysisOutput


class SkillExtractor:
    def __init__(self):
       self.logger = get_logger(__name__)
       self.llm = ChatGroq(model_name="openai/gpt-oss-20b")
       
       self.llm_gpt= ChatOpenAI(model_name="gpt-4.1-nano", max_retries=3)

       self.fallback_llm = self.llm.with_fallbacks([self.llm_gpt])

       self.system_prompt = load_yaml_prompt(path="skills_extractions/skill_extraction", key="SYSTEM_PROMPT")
       self.user_prompt = load_yaml_prompt(path="skills_extractions/skill_extraction", key="USER_PROMPT")
       

    def extract_skills_node(self, state: SkillsExtractionState):
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.user_prompt.format(text=f"{state.file_data} \n\n Here is the additional CV content: \n\n {state.additional_cv_content}"))
        ]
        try:
         response = self.fallback_llm.invoke.with_structured_output(AnalysisOutput)(messages)

         state.analysis_output = response
         return state
        except Exception as e:
            self.logger.error(f"Error extracting skills and tools: {e}")
            raise e


skill_extractor = SkillExtractor()