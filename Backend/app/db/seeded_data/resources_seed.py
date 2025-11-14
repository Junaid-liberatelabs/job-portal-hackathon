"""
Seed data for learning resources.
Provides diverse educational content covering various skills and learning paths.
"""

from app.db.model.resources import Resource


def get_resources_seed_data():
    """
    Returns a list of resource dictionaries for seeding the database.
    Covers various learning paths and skill development areas.
    """
    return [
        # Web Development Resources
        {
            "name": "The Odin Project - Full Stack JavaScript",
            "description": "A free, open-source curriculum for learning web development. Covers HTML, CSS, JavaScript, Node.js, and React with hands-on projects.",
            "url": "https://www.theodinproject.com/paths/full-stack-javascript",
            "tags": [
                "Web Development",
                "JavaScript",
                "React",
                "Node.js",
                "Free",
                "Full Stack",
            ],
        },
        {
            "name": "freeCodeCamp - Responsive Web Design",
            "description": "Learn responsive web design by building projects. Covers HTML, CSS, Flexbox, Grid, and accessibility best practices.",
            "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/",
            "tags": ["Web Development", "HTML", "CSS", "Responsive Design", "Free"],
        },
        {
            "name": "MDN Web Docs - JavaScript Guide",
            "description": "Comprehensive JavaScript documentation and tutorials from Mozilla. Perfect for beginners and intermediate developers.",
            "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
            "tags": ["JavaScript", "Web Development", "Documentation", "Free"],
        },
        {
            "name": "React Official Tutorial",
            "description": "Official React documentation with interactive tutorials. Learn React fundamentals by building a tic-tac-toe game.",
            "url": "https://react.dev/learn",
            "tags": ["React", "JavaScript", "Frontend", "Free", "Web Development"],
        },
        # Backend & Databases
        {
            "name": "FastAPI Tutorial",
            "description": "Official FastAPI documentation with step-by-step tutorials. Learn to build modern, fast APIs with Python.",
            "url": "https://fastapi.tiangolo.com/tutorial/",
            "tags": ["Python", "FastAPI", "Backend", "REST API", "Free"],
        },
        {
            "name": "PostgreSQL Tutorial",
            "description": "Comprehensive PostgreSQL tutorial covering basics to advanced topics. Includes SQL queries, indexing, and optimization.",
            "url": "https://www.postgresqltutorial.com/",
            "tags": ["PostgreSQL", "SQL", "Database", "Backend", "Free"],
        },
        {
            "name": "Node.js Best Practices",
            "description": "A comprehensive guide to Node.js best practices, covering security, performance, and code structure.",
            "url": "https://github.com/goldbergyoni/nodebestpractices",
            "tags": ["Node.js", "Backend", "JavaScript", "Best Practices", "Free"],
        },
        # Data Science & Machine Learning
        {
            "name": "Python for Data Science - Kaggle",
            "description": "Free micro-courses on Python, Pandas, data visualization, and machine learning. Hands-on exercises included.",
            "url": "https://www.kaggle.com/learn",
            "tags": ["Python", "Data Science", "Machine Learning", "Pandas", "Free"],
        },
        {
            "name": "Google Machine Learning Crash Course",
            "description": "Fast-paced introduction to machine learning with TensorFlow. Includes video lectures and hands-on exercises.",
            "url": "https://developers.google.com/machine-learning/crash-course",
            "tags": [
                "Machine Learning",
                "TensorFlow",
                "Python",
                "Data Science",
                "Free",
            ],
        },
        {
            "name": "SQL for Data Analysis - Mode Analytics",
            "description": "Interactive SQL tutorial focused on data analysis. Learn to write complex queries and analyze real datasets.",
            "url": "https://mode.com/sql-tutorial/",
            "tags": ["SQL", "Data Analysis", "Database", "Free"],
        },
        # DevOps & Cloud
        {
            "name": "Docker Getting Started Guide",
            "description": "Official Docker tutorial for beginners. Learn containerization basics and how to deploy applications.",
            "url": "https://docs.docker.com/get-started/",
            "tags": ["Docker", "DevOps", "Containers", "Free"],
        },
        {
            "name": "AWS Free Tier Training",
            "description": "Free AWS training courses covering cloud fundamentals, EC2, S3, and more. Perfect for cloud beginners.",
            "url": "https://aws.amazon.com/training/digital/",
            "tags": ["AWS", "Cloud Computing", "DevOps", "Free"],
        },
        {
            "name": "Kubernetes Basics",
            "description": "Official Kubernetes tutorial covering pods, deployments, and services. Interactive learning environment included.",
            "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/",
            "tags": ["Kubernetes", "DevOps", "Cloud", "Containers", "Free"],
        },
        # Design & UX
        {
            "name": "Google UX Design Certificate",
            "description": "Professional certificate program covering UX research, wireframing, prototyping, and usability testing.",
            "url": "https://www.coursera.org/professional-certificates/google-ux-design",
            "tags": ["UX Design", "UI Design", "Design", "Figma", "Paid"],
        },
        {
            "name": "Figma Tutorial for Beginners",
            "description": "Free comprehensive Figma tutorial on YouTube. Learn interface design, prototyping, and collaboration features.",
            "url": "https://www.youtube.com/watch?v=FTFaQWZBqQ8",
            "tags": ["Figma", "UI Design", "Design", "Free"],
        },
        # Programming Fundamentals
        {
            "name": "CS50 - Introduction to Computer Science",
            "description": "Harvard's famous intro to CS course. Covers algorithms, data structures, and multiple programming languages.",
            "url": "https://cs50.harvard.edu/x/",
            "tags": ["Computer Science", "Programming", "Algorithms", "Free"],
        },
        {
            "name": "Python for Everybody",
            "description": "Free Python course from University of Michigan. Perfect for absolute beginners with no programming experience.",
            "url": "https://www.py4e.com/",
            "tags": ["Python", "Programming", "Beginner", "Free"],
        },
        # Cybersecurity
        {
            "name": "TryHackMe - Complete Beginner Path",
            "description": "Interactive cybersecurity training with hands-on labs. Learn penetration testing and security fundamentals.",
            "url": "https://tryhackme.com/path/outline/beginner",
            "tags": ["Cybersecurity", "Network Security", "Ethical Hacking", "Free"],
        },
        {
            "name": "OWASP Top 10",
            "description": "Learn about the most critical web application security risks. Essential reading for web developers.",
            "url": "https://owasp.org/www-project-top-ten/",
            "tags": ["Cybersecurity", "Web Security", "OWASP", "Free"],
        },
        # Soft Skills & Career
        {
            "name": "Technical Interview Handbook",
            "description": "Free guide to preparing for technical interviews. Covers algorithms, system design, and behavioral questions.",
            "url": "https://www.techinterviewhandbook.org/",
            "tags": ["Interview Prep", "Career", "Algorithms", "Free"],
        },
        {
            "name": "Git and GitHub for Beginners",
            "description": "Learn version control with Git and collaboration on GitHub. Essential skill for all developers.",
            "url": "https://www.freecodecamp.org/news/git-and-github-for-beginners/",
            "tags": ["Git", "GitHub", "Version Control", "Free"],
        },
    ]


def seed_resources(db_session):
    """
    Seeds the database with learning resources.

    Args:
        db_session: SQLAlchemy database session

    Returns:
        int: Number of resources created
    """
    resources_data = get_resources_seed_data()
    resources_created = 0

    for resource_data in resources_data:
        # Check if resource already exists (by URL)
        existing_resource = (
            db_session.query(Resource)
            .filter(Resource.url == resource_data["url"])
            .first()
        )

        if not existing_resource:
            resource = Resource(**resource_data)
            db_session.add(resource)
            resources_created += 1

    db_session.commit()
    return resources_created
