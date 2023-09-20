from .hf import (
    FeatureExtractionPredictor,  # noqa: F401
    HuggingFacePipelinePredictor,  # noqa: F401
    ImageClassificationPredictor,  # noqa: F401
    TextClassificationPredictor,  # noqa: F401
)
from .main import get_predictor  # noqa: F401
from .sbert import SentenceTransformersFeatureExtractionPredictor  # noqa: F401
from .text_generation import TextGenerationPredictor  # noqa: F401


__version__ = "0.0.4"
