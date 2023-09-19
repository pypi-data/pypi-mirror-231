from .hf import (
    FeatureExtractionPredictor,
    ImageClassificationPredictor,
    TextClassificationPredictor,
)
from .sbert import SentenceTransformersFeatureExtractionPredictor
from .text_generation import TextGenerationPredictor


task2predictor = {
    "text-generation": TextGenerationPredictor,
    "text-classification": TextClassificationPredictor,
    "image-classification": ImageClassificationPredictor,
    "feature-extraction": FeatureExtractionPredictor,
    "sentence-transformers-feature-extraction": SentenceTransformersFeatureExtractionPredictor,
}


def get_predictor(task: str, **kwargs):
    klass = task2predictor[task]
    for k, v in kwargs.items():
        setattr(klass, k, v)
    return klass
