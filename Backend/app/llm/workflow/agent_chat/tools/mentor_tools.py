from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

@tool
def search_resources(query: str) -> str:
    """Search for learning resources based on the query."""
    pass

@tool       
def user_skill_gap_analysis_report(query: str) -> str:
    """Generate a skill gap analysis report for the user based on the query."""
    pass

@tool
def user_career_roadmap_analysis(query: str) -> str:
    """Analyze and generate a career roadmap for the user based on the query. The query should be a description of the user's career goals, experience, and skills."""
    pass

@tool
def search_jobs(query: str) -> str:
    """Search for job opportunities based on the query."""
    pass


mentor_tools_node = ToolNode(
    [user_career_roadmap_analysis,user_skill_gap_analysis_report,search_jobs,search_resources],
    name = 'mentor_tools'
)


