"""
SpaCy NER
named entities extractor
"""
import logging
from dataclasses import dataclass
from typing import Dict, List, Tuple

import spacy

logging.basicConfig(
    format="[%(asctime)s] %(levelname)-8s %(name)-15s %(message)s",
    level=logging.INFO,
)

NLP_LIBRARY = "spacy"
MODEL_NAME = "en_core_web_sm"

logger = logging.getLogger(NLP_LIBRARY + "-" + MODEL_NAME)
logger.info("Loading model weights from %s", NLP_LIBRARY)
model = spacy.load(MODEL_NAME)


@dataclass
class SpacyNER:
    """
    Applying spaCy nlp model
    to extract named entities of text
    """

    nlp_library: str = NLP_LIBRARY
    model_name: str = MODEL_NAME
    settings: Dict[str, str] = None

    def __post_init__(self):

        self.settings = {
            "nlp_library": self.nlp_library,
            "model_name": self.model_name,
        }

    @staticmethod
    def extract(data: Dict) -> Dict[str, List[Tuple[str, str]]]:
        """
        Extract entities from text

        Args:
            data (Dict): text to extract entities from

        Returns:
            entities (Dict[str, List[Tuple[str, str]]]):
                    texts with their corresponding entities
        """
        logger.info("Extracting entities...")

        if not isinstance(data, dict):
            raise TypeError("input must be a dictionary")

        entities = {}
        for index, news in data.items():
            doc = model(data[str(index)][list(news.keys())[0]])
            entities[index] = [(ent.text, ent.label_) for ent in doc.ents]

        return entities

    @staticmethod
    def count(data: Dict) -> Dict[str, Dict]:
        """Count of the different entities of each unique news article

        Args:
            data (Dict): text index and text pair

        Returns:
            Dict[str, Dict]: text index with entities and counts
        """
        logger.info("Counting entities...")

        if not isinstance(data, dict):
            raise TypeError("input must be a dictionary")

        article_entities_count = {
            "ORG": 0,
            "MONEY": 0,
            "EVENT": 0,
            "PRODUCT": 0,
            "DATE": 0,
            "LANGUAGE": 0,
            "LOC": 0,
            "LAW": 0,
            "WORK_OF_ART": 0,
            "QUANTITY": 0,
            "GPE": 0,
            "PERCENT": 0,
            "NORP": 0,
            "PERSON": 0,
            "CARDINAL": 0,
            "ORDINAL": 0,
            "FAC": 0,
            "TIME": 0,
        }
        overall_count = {}
        for index, news in data.items():
            doc = model(data[str(index)][list(news.keys())[0]])
            for ent in doc.ents:
                article_entities_count[ent.label_] += 1
            overall_count[index] = article_entities_count
        return overall_count
