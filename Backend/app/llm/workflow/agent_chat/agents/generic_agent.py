from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from app.llm.prompts.load_prompt import load_yaml_prompt
from langchain_core.messages import SystemMessage, HumanMessage
from app.llm.workflow.agent_chat.state import AgentChatState

class GenericAgent:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.llm = ChatOpenAI(model="gpt-4.1-nano", max_retries=3)
        self.gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", max_retries=3)
        self.fallback_llm = self.llm.with_fallbacks([self.gemini_llm])

        self.system_prompt = load_yaml_prompt(path="agent_chat/generic", key="SYSTEM_PROMPT")


    def generic_agent_node(self, state: AgentChatState):
        messages = [SystemMessage(content=self.system_prompt)] + state["messages"]
        response = self.fallback_llm.invoke(messages)
        return {"messages": [response]}

generic_agent = GenericAgent()
