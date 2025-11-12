from sqlalchemy import Column, String, DateTime, Enum, ARRAY, Float, Tuple
from app.db.base import Base

class JobType(Enum):
    #Internship / Part-time / Full-time / Freelance
    INTERNSHIP = "internship"
    PART_TIME = "part_time"
    FULL_TIME = "full_time"
    FREELANCE = "freelance"

class JobLocation(Enum):
   REMOTE = "remote"
   HYBRID = "hybrid"
   ON_SITE = "on_site"

class ExperienceLevel(Enum):
    STUDENT = "student"
    ENTRY = "entry"
    JUNIOR = "junior" # included for a touch of flexibility
    
class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    company = Column(String, nullable=False)
    job_type = Column(Enum(JobType), nullable=False) #mandatory
    job_location = Column(Enum(JobLocation), nullable=True) #optional

    required_skills = Column(ARRAY(String), nullable=False)
    
    recommended_experience_level = Column(Enum(ExperienceLevel), nullable=False)

    salary_range = Column(Tuple[Float, Float], nullable=True) #optional

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title}, company={self.company}, job_type={self.job_type}, job_location={self.job_location}, required_skills={self.required_skills}, recommended_experience_level={self.recommended_experience_level}, salary_range={self.salary_range})>"