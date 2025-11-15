from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from app.llm.prompts.load_prompt import load_yaml_prompt
from app.llm.workflow.agent_chat.state import AgentChatState

from langchain_core.messages import SystemMessage
from app.api.schemas.agent_chat import routerSchema

class AgentRouter:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.llm = ChatOpenAI(model="gpt-4.1-nano", max_retries=3)
        self.gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", max_retries=3)
        self.fallback_llm = self.llm.with_fallbacks([self.gemini_llm])

        self.system_prompt = load_yaml_prompt(path="agent_chat/router", key="SYSTEM_PROMPT")

    def router_node(self, state: AgentChatState):
        messages = [SystemMessage(content=self.system_prompt)] + state["messages"]
        response = self.fallback_llm.with_structured_output(routerSchema).invoke(messages)
        
        
        return {"decided_node": response.decided_node}


router_agent = AgentRouter()