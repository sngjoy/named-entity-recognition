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
            pass

        entities = {}
        for index, news in data.items():
            doc = model(data[str(index)][list(news.keys())[0]])
            entities[index] = [(ent.text, ent.label_) for ent in doc.ents]

        return entities
