from Dataset import FishDataset
from datasets import load_dataset
from datasets import load_metric
from datasets import list_datasets
from datasets import features
from PIL import ImageDraw, ImageFont, Image
from transformers import ViTFeatureExtractor
from transformers import ViTForImageClassification
from transformers import TrainingArguments
from transformers import Trainer
import numpy as np

class Trainer:
    def __init__(self):
        self.dataset=FishDataset()
        self.mode_path = 'google/vit-base-patch16-224-in21k'
        self.feature_extractor = ViTFeatureExtractor.from_pretrained(self.model_path)
        self.prepared_ds = self.dataset.with_transform(self.dataset.transform)
        
        pass