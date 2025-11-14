"""
Embedding service for generating text embeddings using FastEmbed.
"""

import logging
from typing import List, Optional

from app.core.exceptions import EmbeddingGenerationError
from app.db.model.job import Job
from app.db.model.resources import Resource
from app.db.model.user import User
from fastembed import TextEmbedding

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Service for generating text embeddings using FastEmbed"""

    _instance: Optional["EmbeddingService"] = None
    _model: Optional[TextEmbedding] = None

    def __new__(cls):
        """Singleton pattern to avoid reloading model"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize FastEmbed model (BAAI/bge-small-en-v1.5)"""
        if self._model is None:
            try:
                logger.info("Initializing FastEmbed model: BAAI/bge-small-en-v1.5")
                self._model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
                logger.info("FastEmbed model initialized successfully")
            except Exception as e:
                logger.critical(
                    f"Failed to initialize FastEmbed model: {e}", exc_info=True
                )
                raise EmbeddingGenerationError(
                    f"Failed to initialize FastEmbed model: {e}"
                )

    def generate_embedding(self, text: str) -> List[float]:
        """
        Generate 384-dimensional embedding for input text

        Args:
            text: Input text to embed

        Returns:
            List of 384 float values representing the embedding

        Raises:
            EmbeddingGenerationError: If embedding generation fails
        """
        if not text or not text.strip():
            logger.warning("Empty or None text provided for embedding generation")
            raise EmbeddingGenerationError("Cannot generate embedding for empty text")

        try:
            # FastEmbed returns a generator, we take the first result
            embeddings = list(self._model.embed([text.strip()]))
            if not embeddings:
                raise EmbeddingGenerationError("No embedding generated")

            embedding = embeddings[0].tolist()

            # Verify dimensions
            if len(embedding) != 384:
                raise EmbeddingGenerationError(
                    f"Expected 384 dimensions, got {len(embedding)}"
                )

            return embedding
        except EmbeddingGenerationError:
            raise
        except Exception as e:
            logger.error(f"Failed to generate embedding: {e}", exc_info=True)
            raise EmbeddingGenerationError(f"Failed to generate embedding: {e}")

    def generate_user_embedding(self, user: User) -> List[float]:
        """
        Generate embedding from user profile fields

        Args:
            user: User model instance

        Returns:
            List of 384 float values representing the embedding

        Raises:
            EmbeddingGenerationError: If embedding generation fails
        """
        # Concatenate user profile fields
        skills_text = " ".join(user.skills) if user.skills else ""
        text_parts = [
            skills_text,
            user.education_level or "",
            user.preferred_career_track or "",
        ]

        text = " ".join(part for part in text_parts if part.strip())

        if not text.strip():
            raise EmbeddingGenerationError("User profile has no content to embed")

        logger.debug(f"Generating embedding for user {user.id}")
        return self.generate_embedding(text)

    def generate_job_embedding(self, job: Job) -> List[float]:
        """
        Generate embedding from job listing fields

        Args:
            job: Job model instance

        Returns:
            List of 384 float values representing the embedding

        Raises:
            EmbeddingGenerationError: If embedding generation fails
        """
        # Concatenate job fields
        skills_text = " ".join(job.required_skills) if job.required_skills else ""
        experience_text = (
            job.recommended_experience_level.value
            if job.recommended_experience_level
            else ""
        )

        text_parts = [
            job.title or "",
            job.description or "",
            skills_text,
            experience_text,
        ]

        text = " ".join(part for part in text_parts if part.strip())

        if not text.strip():
            raise EmbeddingGenerationError("Job listing has no content to embed")

        logger.debug(f"Generating embedding for job {job.id}")
        return self.generate_embedding(text)

    def generate_resource_embedding(self, resource: Resource) -> List[float]:
        """
        Generate embedding from resource fields

        Args:
            resource: Resource model instance

        Returns:
            List of 384 float values representing the embedding

        Raises:
            EmbeddingGenerationError: If embedding generation fails
        """
        # Concatenate resource fields
        tags_text = " ".join(resource.tags) if resource.tags else ""

        text_parts = [resource.name or "", resource.description or "", tags_text]

        text = " ".join(part for part in text_parts if part.strip())

        if not text.strip():
            raise EmbeddingGenerationError("Resource has no content to embed")

        logger.debug(f"Generating embedding for resource {resource.id}")
        return self.generate_embedding(text)


# Global instance
embedding_service = EmbeddingService()
