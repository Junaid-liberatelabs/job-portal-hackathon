from typing import List
from langchain_core.tools import tool as langchain_tool
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from app.db.model.resources import Resource
from app.services.embedding_service import embedding_service


class ResourceSearchInput(BaseModel):
    """Input schema for resource search tool"""
    skills: List[str] = Field(description="List of skills to search for resources. The tool will perform semantic search to find resources that match these skills.")


def create_resource_search_tool(db: Session):
    """
    Create a tool that searches for learning resources by skills using semantic search.
    The tool uses embeddings to find semantically similar resources.
    """
    import json
    
    def search_learning_resources(skills: List[str]) -> str:
        """
        Search for learning resources in the database that semantically match the given skills.
        Uses vector embeddings for semantic similarity search.
        
        Args:
            skills: A list of skills to search for. The tool will find resources that are semantically similar to these skills.
        
        Returns:
            A JSON string containing a list of resources with their details (name, description, url, platform, duration, pricing, similarity_score).
            Each resource includes: id, name, description, url, tags, platform, duration, pricing, similarity_score.
            Results are ordered by similarity score (highest first).
        
        Example:
            search_learning_resources(["Python", "Django"]) will return resources semantically similar to Python and Django.
        """
        try:
            # Combine skills into a single text for embedding
            skills_text = " ".join(skills)
            
            # Generate embedding for the skills text
            skills_embedding = embedding_service.generate_embedding(skills_text)
            
            # Perform semantic search using cosine similarity
            results = (
                db.query(
                    Resource,
                    (1 - Resource.embedding.cosine_distance(skills_embedding)).label("similarity")
                )
                .filter(Resource.embedding.isnot(None))
                .order_by((1 - Resource.embedding.cosine_distance(skills_embedding)).desc())
                .limit(20)
                .all()
            )
            
            # Convert to response format
            resource_list = []
            for resource, similarity in results:
                resource_dict = {
                    "id": resource.id,
                    "name": resource.name,
                    "description": resource.description,
                    "url": str(resource.url),
                    "tags": resource.tags or [],
                    "platform": resource.platform,
                    "duration": resource.duration,
                    "pricing": resource.pricing or "Free",
                    "similarity_score": round(float(similarity), 4)
                }
                resource_list.append(resource_dict)
            
            # Return as JSON string for LLM to parse
            return json.dumps(resource_list, indent=2, default=str)
        except Exception as e:
            return f"Error searching resources: {str(e)}"
    
    # Create tool with proper schema
    resource_tool = langchain_tool(
        "search_learning_resources",
        args_schema=ResourceSearchInput
    )(search_learning_resources)
    
    return resource_tool

