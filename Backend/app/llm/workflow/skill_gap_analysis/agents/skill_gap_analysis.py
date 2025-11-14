import json
from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from app.llm.prompts.load_prompt import load_yaml_prompt
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

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
        user_data = state.user_profile_data
        user_applied_job_data = state.user_applied_job_data
        resource_search_tool = state.resource_search_tool
        
        # Format data as JSON for better LLM readability
        user_data_str = json.dumps(user_data, indent=2, default=str)
        user_applied_job_data_str = json.dumps(user_applied_job_data, indent=2, default=str)
        
        # Bind tool to LLM if tool is provided
        llm_with_tools = self.fallback_llm
        if resource_search_tool:
            llm_with_tools = self.fallback_llm.bind_tools([resource_search_tool])
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.user_prompt.format(
                user_data=user_data_str,
                user_applied_job_data=user_applied_job_data_str
            ))
        ]
        
        # Invoke LLM with tools
        response = llm_with_tools.invoke(messages)
        
        # Handle tool calls if any
        final_messages = messages + [response]
        
        # Check if response contains tool calls
        # LangChain AIMessage has tool_calls as a list of dicts
        if hasattr(response, 'tool_calls') and response.tool_calls and len(response.tool_calls) > 0:
            for tool_call in response.tool_calls:
                tool_name = tool_call.get("name", "")
                tool_args = tool_call.get("args", {})
                tool_call_id = tool_call.get("id", "")
                
                if tool_name == "search_learning_resources" and resource_search_tool:
                    # Execute tool
                    tool_result = resource_search_tool.invoke(tool_args)
                    
                    # Add tool message to conversation
                    tool_message = ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call_id
                    )
                    final_messages.append(tool_message)
            
            # Get final response from LLM with tool results
            final_response = self.fallback_llm.invoke(final_messages)
            state.gap_analysis_report = final_response.content
        else:
            # No tool calls, use original response
            state.gap_analysis_report = response.content
        
        return state


skill_gap_analysis = SkillGapAnalysis()