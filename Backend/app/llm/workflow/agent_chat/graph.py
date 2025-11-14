from langgraph.graph import StateGraph, START, END
from app.llm.workflow.agent_chat.state import AgentChatState
from app.llm.workflow.agent_chat.agents.router import router_agent
from app.llm.workflow.agent_chat.agents.mentor import mentor_agent
from app.llm.workflow.agent_chat.agents.generic_agent import generic_agent
from app.core.logging_config import get_logger
from app.llm.workflow.agent_chat.tools.mentor_tools import mentor_tools_node


class AgentChatGraph(StateGraph):
    def __init__(self):
        super().__init__(AgentChatState)

        self.logger = get_logger(__name__)

        self.add_node("router", router_agent.router_node)
        self.add_node("mentor", mentor_agent.mentor_node)
        self.add_node("generic", generic_agent.generic_agent_node)
        self.add_node('mentor_tools', mentor_tools_node)

        self.add_edge(START, "router")
        self.add_conditional_edges(
                "router",
                agent_router
        )

        self.add_conditional_edges(
            'mentor',
            mentor_tool_router
        )

        self.add_edge("mentor_tools", "mentor")
        self.add_edge("mentor", END)
        self.add_edge("generic", END)


from typing import Literal
def agent_router(state: AgentChatState) -> Literal["mentor", "generic"]:
    decided_node = state["decided_node"]
    if decided_node == "mentor":
        return "mentor"
    else:
        return "generic"


def mentor_tool_router(state: AgentChatState)-> Literal["mentor_tools","__end__"]:
    last_message = state['messages'][-1]
    if (hasattr(last_message, 'tool_calls') and len(last_message.tool_calls) > 0):
        return "mentor_tools"
    else : 
        return END


agent_chat_graph = AgentChatGraph()