from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from app.llm.prompts.load_prompt import load_yaml_prompt
from langchain_core.messages import SystemMessage, HumanMessage
from app.llm.workflow.agent_chat.state import AgentChatState
from app.llm.workflow.agent_chat.tools.mentor_tools import (
    user_career_roadmap_analysis,
    user_skill_gap_analysis_report,
    user_full_profile,
    user_applied_jobs,
    search_jobs,
    search_resources
)

class MentorAgent:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.llm = ChatOpenAI(model="gpt-4.1-mini", max_retries=3)
        self.gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", max_retries=3)
        self.fallback_llm = self.llm.with_fallbacks([self.gemini_llm])

        #bind tools to the llm
        self.tools = [
            user_career_roadmap_analysis,
            user_skill_gap_analysis_report,
            user_full_profile,
            user_applied_jobs,
            search_jobs,
            search_resources
        ]
        self.fallback_llm_with_tools = self.fallback_llm.bind_tools(self.tools)
        self.system_prompt = load_yaml_prompt(path="agent_chat/mentor", key="SYSTEM_PROMPT")

    def mentor_node(self, state: AgentChatState):
        messages = [SystemMessage(content=self.system_prompt)] + state["messages"]
        response = self.fallback_llm_with_tools.invoke(messages)
        return {"messages": [response]}

mentor_agent = MentorAgent()