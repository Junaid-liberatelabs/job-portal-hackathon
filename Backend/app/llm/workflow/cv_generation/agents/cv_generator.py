import json
from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from app.llm.prompts.load_prompt import load_yaml_prompt
from langchain_core.messages import SystemMessage, HumanMessage

from app.llm.workflow.cv_generation.state import CVGenerationState


class CVGenerator:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.llm = ChatGroq(model_name="llama-3.3-70b-versatile")
        self.llm_gpt = ChatOpenAI(model_name="gpt-4o-mini", max_retries=3)
        self.fallback_llm = self.llm.with_fallbacks([self.llm_gpt])
        self.system_prompt = load_yaml_prompt(path="cv_generation/cv_generation", key="SYSTEM_PROMPT")
        self.user_prompt = load_yaml_prompt(path="cv_generation/cv_generation", key="USER_PROMPT")

    def generate_cv_node(self, state: CVGenerationState):
        """
        Generate HTML CV using LLM.
        
        Args:
            state: CVGenerationState containing user profile and job application data
            
        Returns:
            Updated state with generated HTML CV
        """
        user_data = state.user_profile_data
        user_applied_job_data = state.user_applied_job_data
        
        # Format data as JSON for better LLM readability
        user_data_str = json.dumps(user_data, indent=2, default=str)
        user_applied_job_data_str = json.dumps(user_applied_job_data, indent=2, default=str)
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.user_prompt.format(
                user_data=user_data_str,
                user_applied_job_data=user_applied_job_data_str
            ))
        ]
        
        # Invoke LLM to generate HTML CV
        response = self.fallback_llm.invoke(messages)
        
        # Extract HTML content from response
        html_content = response.content.strip()
        
        # Clean up markdown code blocks if LLM wrapped the HTML
        if html_content.startswith("```html"):
            html_content = html_content[7:]  # Remove ```html
        elif html_content.startswith("```"):
            html_content = html_content[3:]  # Remove ```
        
        if html_content.endswith("```"):
            html_content = html_content[:-3]  # Remove trailing ```
        
        html_content = html_content.strip()
        
        # Update state with generated HTML
        state.html_cv = html_content
        
        self.logger.info("Successfully generated HTML CV")
        
        return state


cv_generator = CVGenerator()
