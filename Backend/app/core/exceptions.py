"""
Custom exception classes for the application.
"""


class EmbeddingGenerationError(Exception):
    """Raised when embedding generation fails"""
    pass


class EmbeddingNotAvailableError(Exception):
    """Raised when required embedding is NULL"""
    pass
