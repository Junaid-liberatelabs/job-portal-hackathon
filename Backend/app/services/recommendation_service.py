"""
Recommendation service for similarity-based recommendations using hybrid approach:
- TF-IDF for keyword-based similarity
- Vector embeddings for semantic similarity
- Combined scoring for better recommendations
"""

import logging
from typing import Dict, List, Tuple

import numpy as np
from app.db.model.job import Job
from app.db.model.resources import Resource
from app.db.model.user import User
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import desc
from sqlalchemy.orm import Session

from Backend.app.db.crud import job

logger = logging.getLogger(__name__)


class RecommendationService:
    """Service for generating recommendations using hybrid TF-IDF + vector similarity"""

    def _calculate_tfidf_similarity(
        self, user_text: str, items: List[Tuple], item_text_func
    ) -> Dict[str, float]:
        """
        Calculate TF-IDF similarity scores between user and items

        Args:
            user_text: User's profile text
            items: List of items (jobs or resources)
            item_text_func: Function to extract text from item

        Returns:
            Dictionary mapping item_id to TF-IDF similarity score
        """
        if not items:
            return {}

        # Prepare documents: user text + all item texts
        documents = [user_text]
        item_ids = []

        for item in items:
            item_text = item_text_func(item)
            documents.append(item_text)
            item_ids.append(item.id)

        # Calculate TF-IDF vectors
        try:
            vectorizer = TfidfVectorizer(
                max_features=1000,
                stop_words="english",
                ngram_range=(1, 2),  # Use unigrams and bigrams
            )
            tfidf_matrix = vectorizer.fit_transform(documents)

            # Calculate cosine similarity between user (first doc) and all items
            user_vector = tfidf_matrix[0:1]
            item_vectors = tfidf_matrix[1:]
            similarities = cosine_similarity(user_vector, item_vectors)[0]

            # Create mapping of item_id to similarity score
            tfidf_scores = {
                item_ids[i]: float(similarities[i]) for i in range(len(item_ids))
            }

            logger.debug(f"Calculated TF-IDF scores for {len(tfidf_scores)} items")
            return tfidf_scores
        except Exception as e:
            logger.error(f"TF-IDF calculation failed: {e}")
            return {}

    # def initial_job_ranking(self,
    #     db: Session,
    #     user: User = None,
    #     limit: int = 10,
    #     tfidf_weight: float = 0.4):
    #     jobs = job.get_jobs(db)
    #     user.

    def get_recommended_jobs(
        self,
        db: Session,
        user_embedding: List[float],
        user: User = None,
        limit: int = 10,
        embedding_weight: float = 0.6,
        tfidf_weight: float = 0.4,
    ) -> List[Tuple[Job, float]]:
        """
        Get jobs most similar to user profile using hybrid TF-IDF + vector similarity

        Args:
            db: Database session
            user_embedding: User's 384-dim embedding vector
            user: User object (optional, for TF-IDF)
            limit: Maximum number of results
            embedding_weight: Weight for embedding similarity (default: 0.6)
            tfidf_weight: Weight for TF-IDF similarity (default: 0.4)

        Returns:
            List of (Job, combined_similarity_score) tuples ordered by score desc
        """
        # Get candidates using vector similarity (fetch more for re-ranking)
        fetch_limit = limit * 3
        vector_results = (
            db.query(
                Job,
                (1 - Job.embedding.cosine_distance(user_embedding)).label("similarity")
            )
            .filter(Job.embedding.isnot(None))
            .order_by((1 - Job.embedding.cosine_distance(user_embedding)).desc())
            .limit(fetch_limit)
            .all()
        )

        if not vector_results:
            logger.info("No jobs with embeddings found")
            return []

        # If user object provided, calculate TF-IDF scores
        tfidf_scores = {}
        if user:
            user_text = " ".join(
                [
                    " ".join(user.skills) if user.skills else "",
                    user.education_level or "",
                    user.preferred_career_track or "",
                ]
            )

            jobs = [job for job, _ in vector_results]

            def job_text_func(job):
                return " ".join(
                    [
                        job.title or "",
                        job.description or "",
                        " ".join(job.required_skills) if job.required_skills else "",
                        job.recommended_experience_level.value
                        if job.recommended_experience_level
                        else "",
                    ]
                )

            tfidf_scores = self._calculate_tfidf_similarity(
                user_text, jobs, job_text_func
            )

        # Combine scores
        combined_results = []
        for job, vector_score in vector_results:
            tfidf_score = tfidf_scores.get(job.id, 0.0) if tfidf_scores else 0.0

            # Weighted combination
            if tfidf_scores:
                combined_score = (embedding_weight * float(vector_score)) + (
                    tfidf_weight * tfidf_score
                )
            else:
                combined_score = float(vector_score)

            combined_results.append((job, combined_score))

        # Sort by combined score and limit
        combined_results.sort(key=lambda x: x[1], reverse=True)
        final_results = combined_results[:limit]

        logger.info(
            f"Found {len(final_results)} recommended jobs (hybrid TF-IDF + vector)"
        )
        return final_results

    def get_recommended_resources(
        self,
        db: Session,
        user_embedding: List[float],
        user: User = None,
        limit: int = 10,
        embedding_weight: float = 0.6,
        tfidf_weight: float = 0.4,
    ) -> List[Tuple[Resource, float]]:
        """
        Get resources most similar to user profile using hybrid TF-IDF + vector similarity

        Args:
            db: Database session
            user_embedding: User's 384-dim embedding vector
            user: User object (optional, for TF-IDF)
            limit: Maximum number of results
            embedding_weight: Weight for embedding similarity (default: 0.6)
            tfidf_weight: Weight for TF-IDF similarity (default: 0.4)

        Returns:
            List of (Resource, combined_similarity_score) tuples ordered by score desc
        """
        # Get candidates using vector similarity (fetch more for re-ranking)
        fetch_limit = limit * 3
        vector_results = (
            db.query(
                Resource,
                (1 - Resource.embedding.cosine_distance(user_embedding)).label(
                    "similarity"
                ),
            )
            .filter(Resource.embedding.isnot(None))
            .order_by((1 - Resource.embedding.cosine_distance(user_embedding)).desc())
            .limit(fetch_limit)
            .all()
        )

        if not vector_results:
            logger.info("No resources with embeddings found")
            return []

        # If user object provided, calculate TF-IDF scores
        tfidf_scores = {}
        if user:
            user_text = " ".join(
                [
                    " ".join(user.skills) if user.skills else "",
                    user.education_level or "",
                    user.preferred_career_track or "",
                ]
            )

            resources = [resource for resource, _ in vector_results]

            def resource_text_func(resource):
                return " ".join(
                    [
                        resource.name or "",
                        resource.description or "",
                        " ".join(resource.tags) if resource.tags else "",
                    ]
                )

            tfidf_scores = self._calculate_tfidf_similarity(
                user_text, resources, resource_text_func
            )

        # Combine scores
        combined_results = []
        for resource, vector_score in vector_results:
            tfidf_score = tfidf_scores.get(resource.id, 0.0) if tfidf_scores else 0.0

            # Weighted combination
            if tfidf_scores:
                combined_score = (embedding_weight * float(vector_score)) + (
                    tfidf_weight * tfidf_score
                )
            else:
                combined_score = float(vector_score)

            combined_results.append((resource, combined_score))

        # Sort by combined score and limit
        combined_results.sort(key=lambda x: x[1], reverse=True)
        final_results = combined_results[:limit]

        logger.info(
            f"Found {len(final_results)} recommended resources (hybrid TF-IDF + vector)"
        )
        return final_results

    def get_similar_jobs(
        self,
        db: Session,
        job_embedding: List[float],
        exclude_job_id: str,
        limit: int = 5,
    ) -> List[Tuple[Job, float]]:
        """
        Get jobs similar to a specific job using cosine similarity

        Args:
            db: Database session
            job_embedding: Job's 384-dim embedding vector
            exclude_job_id: ID of the job to exclude from results
            limit: Maximum number of results

        Returns:
            List of (Job, similarity_score) tuples ordered by score desc
        """
        results = (
            db.query(
                Job,
                (1 - Job.embedding.cosine_distance(job_embedding)).label("similarity"),
            )
            .filter(Job.embedding.isnot(None))  # Filter out NULL embeddings
            .filter(Job.id != exclude_job_id)  # Exclude the original job
            .order_by((1 - Job.embedding.cosine_distance(job_embedding)).desc())
            .limit(limit)
            .all()
        )

        logger.info(f"Found {len(results)} similar jobs for job {exclude_job_id}")
        return [(job, float(similarity)) for job, similarity in results]

    def get_similar_resources(
        self,
        db: Session,
        resource_embedding: List[float],
        exclude_resource_id: str,
        limit: int = 5,
    ) -> List[Tuple[Resource, float]]:
        """
        Get resources similar to a specific resource using cosine similarity

        Args:
            db: Database session
            resource_embedding: Resource's 384-dim embedding vector
            exclude_resource_id: ID of the resource to exclude from results
            limit: Maximum number of results

        Returns:
            List of (Resource, similarity_score) tuples ordered by score desc
        """
        results = (
            db.query(
                Resource,
                (1 - Resource.embedding.cosine_distance(resource_embedding)).label(
                    "similarity"
                ),
            )
            .filter(Resource.embedding.isnot(None))  # Filter out NULL embeddings
            .filter(Resource.id != exclude_resource_id)  # Exclude the original resource
            .order_by(
                (1 - Resource.embedding.cosine_distance(resource_embedding)).desc()
            )
            .limit(limit)
            .all()
        )

        logger.info(
            f"Found {len(results)} similar resources for resource {exclude_resource_id}"
        )
        return [(resource, float(similarity)) for resource, similarity in results]


# Global instance
recommendation_service = RecommendationService()
