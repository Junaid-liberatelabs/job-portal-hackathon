import json
import contextvars
from typing import List
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from sqlalchemy.orm import Session
from app.db.model.job import Job
from app.db.model.resources import Resource
from app.db.session import SessionLocal
from app.services.embedding_service import embedding_service
from app.db.crud.analysis_report import (
    get_skill_gap_analysis_report,
    get_most_recent_career_roadmap_report
)
from app.db.crud.user import get_user_by_id
from app.db.crud.application import get_applications_by_user
from app.db.crud.job import get_job_by_id

# Context variable to store user_id for tools
user_id_context: contextvars.ContextVar[str] = contextvars.ContextVar('user_id')


def get_db_session() -> Session:
    """Create a new database session for tool execution."""
    return SessionLocal()

@tool
def user_full_profile(query: str) -> str:
    """
    Retrieve the full profile of the user.
    Returns the full profile data from the database.
    
    Args:
        query: Optional query parameter (not used, but required for tool signature).
    
    Returns:
        A JSON string containing the user profile with all fields including id, full_name, email, education_level, preferred_career_track, skills, bio, location, experience_level, preferred_job_type, institution, field_of_study, graduation_year, cgpa, brief_experience, and other profile fields.
        Returns an error message if no profile is found for the user.
    """
    db = get_db_session()
    try:
        user_id = user_id_context.get()
        if not user_id:
            return "Error: User ID not found in context"
        
        user = get_user_by_id(db, user_id)
        
        if not user:
            return "Error: User profile not found"
        
        # Build comprehensive user profile dictionary
        user_dict = {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "education_level": user.education_level,
            "preferred_career_track": user.preferred_career_track,
            "skills": user.skills or [],
            "is_active": user.is_active,
            "bio": user.bio,
            "location": user.location,
            "preferred_job_location": user.preferred_job_location.value if user.preferred_job_location else None,
            "experience_level": user.experience_level.value if user.experience_level else None,
            "preferred_job_type": user.preferred_job_type.value if user.preferred_job_type else None,
            "linkedin_url": user.linkedin_url,
            "github_url": user.github_url,
            "phone_number": user.phone_number,
            "institution": user.institution,
            "field_of_study": user.field_of_study,
            "graduation_year": user.graduation_year,
            "cgpa": user.cgpa,
            "brief_experience": user.brief_experience,
            "project_description": user.project_description,
            "created_at": user.created_at.isoformat() if user.created_at else None,
            "updated_at": user.updated_at.isoformat() if user.updated_at else None
        }
        
        return json.dumps(user_dict, indent=2, default=str)
    except LookupError:
        return "Error: User ID not found in context"
    except Exception as e:
        return f"Error retrieving user profile: {str(e)}"
    finally:
        db.close()


@tool
def user_applied_jobs(query: str) -> str:
    """
    Retrieve the jobs that the user has applied to.
    Returns the full list of jobs with complete job details that the user has applied to.
    
    Args:
        query: Optional query parameter (not used, but required for tool signature).
    
    Returns:
        A JSON string containing a list of jobs the user has applied to, each with complete job details including id, title, company, description, job_type, job_location, required_skills, recommended_experience_level, salary_range_min, salary_range_max, url, and application created_at.
        Returns an empty list if the user has not applied to any jobs.
    """
    db = get_db_session()
    try:
        user_id = user_id_context.get()
        if not user_id:
            return "Error: User ID not found in context"
        
        # Get all applications for the user
        applications = get_applications_by_user(db, user_id)
        
        if not applications:
            return json.dumps([], indent=2)
        
        # Extract job IDs and get job details
        job_ids = [application.job_id for application in applications]
        jobs = [get_job_by_id(db, job_id) for job_id in job_ids]
        
        # Filter out None jobs (in case a job was deleted) and build job list
        job_list = []
        for application, job in zip(applications, jobs):
            if job is not None:
                job_dict = {
                    "id": job.id,
                    "title": job.title,
                    "company": job.company,
                    "description": job.description,
                    "job_type": job.job_type.value if job.job_type else None,
                    "job_location": job.job_location.value if job.job_location else None,
                    "required_skills": job.required_skills or [],
                    "recommended_experience_level": job.recommended_experience_level.value if job.recommended_experience_level else None,
                    "salary_range_min": job.salary_range_min,
                    "salary_range_max": job.salary_range_max,
                    "url": job.url,
                    "application_created_at": application.created_at.isoformat() if application.created_at else None
                }
                job_list.append(job_dict)
        
        return json.dumps(job_list, indent=2, default=str)
    except LookupError:
        return "Error: User ID not found in context"
    except Exception as e:
        return f"Error retrieving applied jobs: {str(e)}"
    finally:
        db.close()


@tool
def search_resources(query: str) -> str:
    """
    Search for learning resources using semantic search based on the query.
    Uses vector embeddings to find resources that semantically match the query.
    
    Args:
        query: A search query describing the type of resources or skills to find.
    
    Returns:
        A JSON string containing a list of resources with their details (id, name, description, url, tags, platform, duration, pricing, similarity_score).
        Results are ordered by similarity score (highest first), limited to top 20 matches.
    """
    db = get_db_session()
    try:
        # Generate embedding for the query
        query_embedding = embedding_service.generate_embedding(query)
        
        # Perform semantic search using cosine similarity
        results = (
            db.query(
                Resource,
                (1 - Resource.embedding.cosine_distance(query_embedding)).label("similarity")
            )
            .filter(Resource.embedding.isnot(None))
            .order_by((1 - Resource.embedding.cosine_distance(query_embedding)).desc())
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
        
        return json.dumps(resource_list, indent=2, default=str)
    except Exception as e:
        return f"Error searching resources: {str(e)}"
    finally:
        db.close()


@tool
def search_jobs(query: str) -> str:
    """
    Search for job opportunities using semantic search based on the query.
    Uses vector embeddings to find jobs that semantically match the query.
    
    Args:
        query: A search query describing the type of job, skills, or role to find.
    
    Returns:
        A JSON string containing a list of jobs with their details (id, title, company, description, job_type, job_location, required_skills, recommended_experience_level, salary_range_min, salary_range_max, url, similarity_score).
        Results are ordered by similarity score (highest first), limited to top 20 matches.
    """
    db = get_db_session()
    try:
        # Generate embedding for the query
        query_embedding = embedding_service.generate_embedding(query)
        
        # Perform semantic search using cosine similarity
        results = (
            db.query(
                Job,
                (1 - Job.embedding.cosine_distance(query_embedding)).label("similarity")
            )
            .filter(Job.embedding.isnot(None))
            .order_by((1 - Job.embedding.cosine_distance(query_embedding)).desc())
            .limit(20)
            .all()
        )
        
        # Convert to response format
        job_list = []
        for job, similarity in results:
            job_dict = {
                "id": job.id,
                "title": job.title,
                "company": job.company,
                "description": job.description,
                "job_type": job.job_type.value if job.job_type else None,
                "job_location": job.job_location.value if job.job_location else None,
                "required_skills": job.required_skills or [],
                "recommended_experience_level": job.recommended_experience_level.value if job.recommended_experience_level else None,
                "salary_range_min": job.salary_range_min,
                "salary_range_max": job.salary_range_max,
                "url": job.url,
                "similarity_score": round(float(similarity), 4)
            }
            job_list.append(job_dict)
        
        return json.dumps(job_list, indent=2, default=str)
    except Exception as e:
        return f"Error searching jobs: {str(e)}"
    finally:
        db.close()


@tool       
def user_skill_gap_analysis_report(query: str) -> str:
    """
    Retrieve the most recent skill gap analysis report for the user.
    Returns the full report data from the database (not using embeddings since reports are large).
    
    Args:
        query: Optional query parameter (not used, but required for tool signature).
    
    Returns:
        A JSON string containing the skill gap analysis report with id, user_id, gap_analysis_report, and created_at.
        Returns an error message if no report is found for the user.
    """
    db = get_db_session()
    try:
        user_id = user_id_context.get()
        if not user_id:
            return "Error: User ID not found in context"
        
        report = get_skill_gap_analysis_report(db, user_id)
        
        if not report:
            return "No skill gap analysis report found for this user. Please generate a report first."
        
        report_dict = {
            "id": report.id,
            "user_id": report.user_id,
            "gap_analysis_report": report.gap_analysis_report,
            "created_at": report.created_at.isoformat() if report.created_at else None
        }
        
        return json.dumps(report_dict, indent=2, default=str)
    except LookupError:
        return "Error: User ID not found in context"
    except Exception as e:
        return f"Error retrieving skill gap analysis report: {str(e)}"
    finally:
        db.close()


@tool
def user_career_roadmap_analysis(query: str) -> str:
    """
    Retrieve the most recent career roadmap analysis report for the user.
    Returns the full report data from the database (not using embeddings since reports are large).
    
    Args:
        query: Optional query parameter (not used, but required for tool signature).
    
    Returns:
        A JSON string containing the career roadmap report with id, user_id, career_roadmap_report, graph_data, and created_at.
        Returns an error message if no report is found for the user.
    """
    db = get_db_session()
    try:
        user_id = user_id_context.get()
        if not user_id:
            return "Error: User ID not found in context"
        
        report = get_most_recent_career_roadmap_report(db, user_id)
        
        if not report:
            return "No career roadmap report found for this user. Please generate a report first."
        
        report_dict = {
            "id": report.id,
            "user_id": report.user_id,
            "career_roadmap_report": report.career_roadmap_report,
            "graph_data": report.graph_data if report.graph_data else {},
            "created_at": report.created_at.isoformat() if report.created_at else None
        }
        
        return json.dumps(report_dict, indent=2, default=str)
    except LookupError:
        return "Error: User ID not found in context"
    except Exception as e:
        return f"Error retrieving career roadmap report: {str(e)}"
    finally:
        db.close()


mentor_tools_node = ToolNode(
    [
        user_career_roadmap_analysis,
        user_skill_gap_analysis_report,
        user_full_profile,
        user_applied_jobs,
        search_jobs,
        search_resources
    ],
    name='mentor_tools'
)


