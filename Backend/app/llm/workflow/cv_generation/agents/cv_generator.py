import json
from app.core.logging_config import get_logger
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from app.llm.prompts.load_prompt import load_yaml_prompt
from langchain_core.messages import SystemMessage, HumanMessage

from app.llm.workflow.cv_generation.state import CVGenerationState


class CVGenerator:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.llm =  ChatOpenAI(model_name="gpt-4.1", max_retries=3)
        self.llm_gpt =ChatGoogleGenerativeAI(model="gemini-2.5-flash", max_retries=3)
        self.fallback_llm = self.llm.with_fallbacks([self.llm_gpt])
        self.system_prompt = load_yaml_prompt(path="cv_generation/cv_generation", key="SYSTEM_PROMPT")
        self.user_prompt = load_yaml_prompt(path="cv_generation/cv_generation", key="USER_PROMPT")

    def generate_cv_node(self, state: CVGenerationState):
        """
        Generate LaTeX CV using LLM.
        
        Args:
            state: CVGenerationState containing user profile and job application data
            
        Returns:
            Updated state with generated LaTeX CV
        """
        try:
            user_data = state.user_profile_data
            user_applied_job_data = state.user_applied_job_data
            
            # Format data as JSON for better LLM readability
            user_data_str = json.dumps(user_data, indent=2, default=str)
            user_applied_job_data_str = json.dumps(user_applied_job_data, indent=2, default=str)
            
            # Format the user prompt with proper error handling
            try:
                formatted_user_prompt = self.user_prompt.format(
                    user_data=user_data_str,
                    user_applied_job_data=user_applied_job_data_str
                )
            except KeyError as e:
                self.logger.error(f"Error formatting prompt - missing key: {e}")
                raise ValueError(f"Prompt formatting error: missing key {e}")
            except Exception as e:
                self.logger.error(f"Error formatting prompt: {e}")
                raise ValueError(f"Prompt formatting error: {str(e)}")
            
            messages = [
                SystemMessage(content=self.system_prompt),
                HumanMessage(content=formatted_user_prompt)
            ]
            
            # Invoke LLM to generate LaTeX CV
            response = self.fallback_llm.invoke(messages)
            
            # Extract LaTeX content from response
            latex_content = response.content.strip()
            
            # Clean up markdown code blocks if LLM wrapped the LaTeX
            if latex_content.startswith("```latex"):
                latex_content = latex_content[8:]  # Remove ```latex
            elif latex_content.startswith("```"):
                latex_content = latex_content[3:]  # Remove ```
            
            if latex_content.endswith("```"):
                latex_content = latex_content[:-3]  # Remove trailing ```
            
            latex_content = latex_content.strip()
            
            # Validate that we got LaTeX content
            if not latex_content:
                raise ValueError("LLM returned empty LaTeX content")
            
            if not latex_content.startswith("\\documentclass"):
                self.logger.warning("Generated content may not be valid LaTeX - missing \\documentclass")
            
            # Update state with generated LaTeX
            state.latex_cv = latex_content
            
            self.logger.info("Successfully generated LaTeX CV")
            
            return state
            
        except Exception as e:
            self.logger.error(f"Error generating LaTeX CV: {e}", exc_info=True)
            raise


cv_generator = CVGenerator()
