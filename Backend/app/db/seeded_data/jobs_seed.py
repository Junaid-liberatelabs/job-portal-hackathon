"""
Seed data for job listings.
Provides diverse job opportunities across different types, experience levels, and skill requirements.
"""

from app.db.model.job import ExperienceLevel, Job, JobLocation, JobType


def get_jobs_seed_data():
    """
    Returns a list of job dictionaries for seeding the database.
    Covers various job types, experience levels, and skill combinations.
    """
    return [
        # Web Development Jobs
        {
            "title": "Frontend Developer Intern",
            "description": "Join our team to build modern web applications using React and TypeScript. Perfect for students looking to gain real-world experience.",
            "company": "TechStart Inc",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.REMOTE,
            "required_skills": ["JavaScript", "React", "HTML", "CSS"],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 15.0,
            "salary_range_max": 20.0,
        },
        {
            "title": "Junior Full Stack Developer",
            "description": "Work on both frontend and backend systems using modern technologies. We're looking for someone passionate about web development.",
            "company": "WebSolutions Co",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.HYBRID,
            "required_skills": ["JavaScript", "Node.js", "React", "MongoDB", "Git"],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 55000.0,
            "salary_range_max": 70000.0,
        },
        {
            "title": "WordPress Developer",
            "description": "Create and maintain WordPress websites for small businesses. Flexible part-time hours.",
            "company": "Digital Agency Pro",
            "job_type": JobType.PART_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": ["WordPress", "PHP", "HTML", "CSS", "JavaScript"],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 25.0,
            "salary_range_max": 35.0,
        },
        {
            "title": "React Native Mobile Developer",
            "description": "Build cross-platform mobile applications for our growing startup. Great opportunity for junior developers.",
            "company": "MobileFirst Labs",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.ON_SITE,
            "required_skills": [
                "React Native",
                "JavaScript",
                "TypeScript",
                "Mobile Development",
            ],
            "recommended_experience_level": ExperienceLevel.JUNIOR,
            "salary_range_min": 60000.0,
            "salary_range_max": 75000.0,
        },
        # Data Science & Analytics
        {
            "title": "Data Analysis Intern",
            "description": "Analyze business data and create visualizations. Learn from experienced data scientists.",
            "company": "DataDriven Corp",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.HYBRID,
            "required_skills": ["Python", "Excel", "SQL", "Data Visualization"],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 18.0,
            "salary_range_max": 22.0,
        },
        {
            "title": "Junior Data Scientist",
            "description": "Apply machine learning techniques to solve business problems. Work with large datasets and modern ML frameworks.",
            "company": "AI Innovations",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "Python",
                "Machine Learning",
                "Pandas",
                "SQL",
                "Statistics",
            ],
            "recommended_experience_level": ExperienceLevel.JUNIOR,
            "salary_range_min": 65000.0,
            "salary_range_max": 80000.0,
        },
        {
            "title": "Business Intelligence Analyst",
            "description": "Create dashboards and reports to help stakeholders make data-driven decisions.",
            "company": "Enterprise Analytics",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.HYBRID,
            "required_skills": ["SQL", "Tableau", "Power BI", "Excel", "Data Analysis"],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 50000.0,
            "salary_range_max": 65000.0,
        },
        # Backend & DevOps
        {
            "title": "Backend Developer Intern",
            "description": "Learn to build scalable APIs and work with databases. Mentorship provided.",
            "company": "CloudTech Systems",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.REMOTE,
            "required_skills": ["Python", "FastAPI", "PostgreSQL", "REST API"],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 16.0,
            "salary_range_max": 21.0,
        },
        {
            "title": "Junior DevOps Engineer",
            "description": "Help maintain CI/CD pipelines and cloud infrastructure. Great learning opportunity.",
            "company": "Infrastructure Pro",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": ["Docker", "Kubernetes", "AWS", "Linux", "Git"],
            "recommended_experience_level": ExperienceLevel.JUNIOR,
            "salary_range_min": 60000.0,
            "salary_range_max": 75000.0,
        },
        {
            "title": "Python Backend Developer",
            "description": "Develop RESTful APIs and microservices using Python frameworks.",
            "company": "API Masters",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.HYBRID,
            "required_skills": ["Python", "Django", "PostgreSQL", "Redis", "Docker"],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 55000.0,
            "salary_range_max": 70000.0,
        },
        # Design & Creative
        {
            "title": "UI/UX Design Intern",
            "description": "Create user interfaces and improve user experience for web and mobile apps.",
            "company": "Design Studio Plus",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.REMOTE,
            "required_skills": ["Figma", "UI Design", "UX Design", "Prototyping"],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 15.0,
            "salary_range_max": 19.0,
        },
        {
            "title": "Graphic Designer",
            "description": "Create visual content for marketing campaigns and social media. Part-time, flexible hours.",
            "company": "Creative Minds Agency",
            "job_type": JobType.PART_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "Adobe Photoshop",
                "Adobe Illustrator",
                "Graphic Design",
                "Branding",
            ],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 20.0,
            "salary_range_max": 30.0,
        },
        # QA & Testing
        {
            "title": "QA Tester Intern",
            "description": "Test software applications and report bugs. Learn about quality assurance processes.",
            "company": "Quality First Software",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.HYBRID,
            "required_skills": [
                "Manual Testing",
                "Bug Reporting",
                "Test Cases",
                "Attention to Detail",
            ],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 14.0,
            "salary_range_max": 18.0,
        },
        {
            "title": "Junior QA Automation Engineer",
            "description": "Write automated tests for web applications using modern testing frameworks.",
            "company": "TestAutomation Inc",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "Selenium",
                "Python",
                "Test Automation",
                "CI/CD",
                "Git",
            ],
            "recommended_experience_level": ExperienceLevel.JUNIOR,
            "salary_range_min": 50000.0,
            "salary_range_max": 65000.0,
        },
        # Freelance & Contract
        {
            "title": "Freelance Content Writer",
            "description": "Write technical blog posts and documentation for tech companies. Work on your own schedule.",
            "company": "Content Creators Network",
            "job_type": JobType.FREELANCE,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "Technical Writing",
                "Content Creation",
                "SEO",
                "Research",
            ],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 25.0,
            "salary_range_max": 50.0,
        },
        {
            "title": "Freelance Web Developer",
            "description": "Build websites for small businesses and startups. Project-based work.",
            "company": "Freelance Hub",
            "job_type": JobType.FREELANCE,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "WordPress",
                "Responsive Design",
            ],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 30.0,
            "salary_range_max": 60.0,
        },
        {
            "title": "Social Media Manager",
            "description": "Manage social media accounts for multiple clients. Flexible freelance opportunity.",
            "company": "Social Growth Agency",
            "job_type": JobType.FREELANCE,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "Social Media Marketing",
                "Content Creation",
                "Analytics",
                "Communication",
            ],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 20.0,
            "salary_range_max": 40.0,
        },
        # Cybersecurity
        {
            "title": "Cybersecurity Intern",
            "description": "Learn about network security, vulnerability assessment, and security best practices.",
            "company": "SecureNet Solutions",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.HYBRID,
            "required_skills": [
                "Network Security",
                "Linux",
                "Security Fundamentals",
                "Python",
            ],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 18.0,
            "salary_range_max": 23.0,
        },
        {
            "title": "Junior Security Analyst",
            "description": "Monitor security systems and respond to security incidents. Training provided.",
            "company": "CyberDefense Corp",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.ON_SITE,
            "required_skills": [
                "Security Analysis",
                "SIEM",
                "Incident Response",
                "Network Security",
            ],
            "recommended_experience_level": ExperienceLevel.JUNIOR,
            "salary_range_min": 55000.0,
            "salary_range_max": 70000.0,
        },
        # Marketing & Business
        {
            "title": "Digital Marketing Intern",
            "description": "Assist with email campaigns, social media, and content marketing initiatives.",
            "company": "Growth Marketing Co",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "Digital Marketing",
                "Social Media",
                "Email Marketing",
                "Analytics",
            ],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 14.0,
            "salary_range_max": 18.0,
        },
        {
            "title": "SEO Specialist",
            "description": "Optimize websites for search engines and improve organic traffic. Part-time position.",
            "company": "SEO Experts",
            "job_type": JobType.PART_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "SEO",
                "Google Analytics",
                "Keyword Research",
                "Content Strategy",
            ],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 22.0,
            "salary_range_max": 32.0,
        },
        # Additional Tech Roles
        {
            "title": "IT Support Specialist",
            "description": "Provide technical support to employees and maintain IT infrastructure.",
            "company": "TechSupport Plus",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.ON_SITE,
            "required_skills": [
                "Technical Support",
                "Windows",
                "Networking",
                "Troubleshooting",
            ],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 40000.0,
            "salary_range_max": 50000.0,
        },
        {
            "title": "Database Administrator Intern",
            "description": "Learn database management, optimization, and backup procedures.",
            "company": "Data Systems Inc",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.HYBRID,
            "required_skills": [
                "SQL",
                "PostgreSQL",
                "Database Management",
                "Data Backup",
            ],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 17.0,
            "salary_range_max": 22.0,
        },
        {
            "title": "Game Developer",
            "description": "Create indie games using Unity or Unreal Engine. Join our small passionate team.",
            "company": "Indie Game Studio",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": ["Unity", "C#", "Game Development", "3D Modeling"],
            "recommended_experience_level": ExperienceLevel.JUNIOR,
            "salary_range_min": 50000.0,
            "salary_range_max": 65000.0,
        },
        {
            "title": "Technical Support Engineer",
            "description": "Help customers troubleshoot technical issues via chat and email. Remote-first company.",
            "company": "SaaS Support Co",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "Customer Support",
                "Technical Troubleshooting",
                "Communication",
                "Problem Solving",
            ],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 45000.0,
            "salary_range_max": 55000.0,
        },
        {
            "title": "Cloud Engineer Intern",
            "description": "Work with AWS services and learn cloud architecture. Great mentorship opportunity.",
            "company": "CloudNative Tech",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.REMOTE,
            "required_skills": ["AWS", "Cloud Computing", "Linux", "Python"],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 19.0,
            "salary_range_max": 24.0,
        },
        {
            "title": "iOS Developer",
            "description": "Build native iOS applications using Swift. Work on consumer-facing apps.",
            "company": "Mobile Apps Inc",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.HYBRID,
            "required_skills": ["Swift", "iOS Development", "Xcode", "Mobile UI"],
            "recommended_experience_level": ExperienceLevel.JUNIOR,
            "salary_range_min": 60000.0,
            "salary_range_max": 75000.0,
        },
        {
            "title": "Android Developer",
            "description": "Develop Android applications using Kotlin. Join our mobile development team.",
            "company": "Android Solutions",
            "job_type": JobType.FULL_TIME,
            "job_location": JobLocation.REMOTE,
            "required_skills": ["Kotlin", "Android Development", "Java", "Mobile UI"],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 55000.0,
            "salary_range_max": 70000.0,
        },
        {
            "title": "Machine Learning Intern",
            "description": "Work on ML projects and learn about neural networks and deep learning.",
            "company": "AI Research Lab",
            "job_type": JobType.INTERNSHIP,
            "job_location": JobLocation.HYBRID,
            "required_skills": [
                "Python",
                "Machine Learning",
                "TensorFlow",
                "Mathematics",
            ],
            "recommended_experience_level": ExperienceLevel.STUDENT,
            "salary_range_min": 20.0,
            "salary_range_max": 25.0,
        },
        {
            "title": "Video Editor",
            "description": "Edit videos for YouTube channels and marketing campaigns. Freelance project-based work.",
            "company": "Video Production House",
            "job_type": JobType.FREELANCE,
            "job_location": JobLocation.REMOTE,
            "required_skills": [
                "Video Editing",
                "Adobe Premiere Pro",
                "After Effects",
                "Storytelling",
            ],
            "recommended_experience_level": ExperienceLevel.ENTRY,
            "salary_range_min": 25.0,
            "salary_range_max": 50.0,
        },
    ]


def seed_jobs(db_session):
    """
    Seeds the database with job listings.

    Args:
        db_session: SQLAlchemy database session

    Returns:
        int: Number of jobs created
    """
    jobs_data = get_jobs_seed_data()
    jobs_created = 0

    for job_data in jobs_data:
        # Check if job already exists (by title and company)
        existing_job = (
            db_session.query(Job)
            .filter(Job.title == job_data["title"], Job.company == job_data["company"])
            .first()
        )

        if not existing_job:
            job = Job(**job_data)
            db_session.add(job)
            jobs_created += 1

    db_session.commit()
    return jobs_created
