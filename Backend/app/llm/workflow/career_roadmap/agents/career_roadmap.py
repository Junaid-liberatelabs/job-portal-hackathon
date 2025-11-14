import json
from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from app.llm.prompts.load_prompt import load_yaml_prompt
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from app.llm.workflow.career_roadmap.state import CareerRoadmapState
from app.api.schemas.career_roadmap import CareerRoadmapGraphData

class CareerRoadmap:
    def __init__(self):
        self.logger = get_logger(__name__)
        # self.llm = ChatGroq(model_name="openai/gpt-oss-20b")
        self.llm_gpt= ChatOpenAI(model="gpt-4.1", max_retries=3)
        self.llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash", max_retries=3)
        self.fallback_llm = self.llm_gpt.with_fallbacks([self.llm_gemini])
        self.system_prompt = load_yaml_prompt(path="career_roadmap/career_roadmap", key="SYSTEM_PROMPT")
        self.user_prompt = load_yaml_prompt(path="career_roadmap/career_roadmap", key="USER_PROMPT")
        self.graph_system_prompt = load_yaml_prompt(path="career_roadmap/career_roadmap", key="GRAPH_SYSTEM_PROMPT")
        self.graph_user_prompt = load_yaml_prompt(path="career_roadmap/career_roadmap", key="GRAPH_USER_PROMPT")

    def create_career_roadmap_report_node(self, state: CareerRoadmapState):
        user_data = state.user_profile_data
        user_applied_job_data = state.user_applied_job_data
        timeframe = state.timeframe
        available_learning_time = state.available_learning_time
        
        # Format user data as JSON for better LLM readability
        user_data_str = json.dumps(user_data, indent=2, default=str)
        user_applied_job_data_str = json.dumps(user_applied_job_data, indent=2, default=str)
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.user_prompt.format(
                user_profile_data=user_data_str,
                user_applied_job_data=user_applied_job_data_str,
                timeframe=timeframe,
                available_learning_time=available_learning_time
            ))
        ]
        response = self.fallback_llm.invoke(messages)
        state.career_roadmap_report = response.content
        return state

    def create_career_roadmap_graph_node(self, state: CareerRoadmapState):
        if not state.career_roadmap_report:
            self.logger.warning("No career roadmap report available for graph conversion")
            return state
        
        try:
            # Update prompt to explicitly request JSON format
            enhanced_user_prompt = self.graph_user_prompt.format(
                career_roadmap_report=state.career_roadmap_report
            ) + "\n\nIMPORTANT: Return ONLY valid JSON in the following format:\n{\n  \"nodes\": [...],\n  \"edges\": [...]\n}\nDo not include any markdown formatting, code blocks, or additional text. Return pure JSON only."
            
            messages = [
                SystemMessage(content=self.graph_system_prompt),
                HumanMessage(content=enhanced_user_prompt)
            ]
            
            # Try using GPT model directly for structured output (supports it)
            # Use function_calling method to handle dict types better
            try:
                response = self.llm_gpt.with_structured_output(
                    CareerRoadmapGraphData,
                    method="function_calling"
                ).invoke(messages)
                state.graph_data = response
                self.logger.info(f"Successfully generated graph data with {len(response.nodes)} nodes and {len(response.edges)} edges")
            except Exception as structured_error:
                self.logger.warning(f"Structured output failed, falling back to JSON parsing: {structured_error}")
                # Fallback: Get JSON response and parse it manually
                response = self.fallback_llm.invoke(messages)
                json_text = response.content.strip()
                
                # Remove markdown code blocks if present
                if json_text.startswith("```"):
                    json_text = json_text.split("```")[1]
                    if json_text.startswith("json"):
                        json_text = json_text[4:]
                    json_text = json_text.strip()
                elif json_text.startswith("```json"):
                    json_text = json_text[7:].strip()
                    if json_text.endswith("```"):
                        json_text = json_text[:-3].strip()
                
                # Parse and validate JSON
                json_data = json.loads(json_text)
                state.graph_data = CareerRoadmapGraphData.model_validate(json_data)
                self.logger.info(f"Successfully parsed graph data with {len(state.graph_data.nodes)} nodes and {len(state.graph_data.edges)} edges")
                
        except Exception as e:
            self.logger.error(f"Error converting roadmap to graph: {e}")
            raise e
        
        return state


career_roadmap = CareerRoadmap()