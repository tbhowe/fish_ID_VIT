#%%
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
import torch
import numpy as np

#TODO docstrings

class TrainingCongfig:
    def __init__(self):
        self.dataset=FishDataset()
        self.model_path = 'google/vit-base-patch16-224-in21k'
        self.feature_extractor = ViTFeatureExtractor.from_pretrained(self.model_path)
        self.prepared_ds = self.dataset.dataset.with_transform(self.dataset.transform)
        # self.prepared_ds.
        self.metric = load_metric("accuracy")
        self.labels = self.dataset.fish_species
        self.model = ViTForImageClassification.from_pretrained(  self.model_path,
                                                    num_labels=len(self.labels),
                                                    id2label={str(i): c for i, c in enumerate(self.labels)},
                                                    label2id={c: str(i) for i, c in enumerate(self.labels)}
                                                )
        self.training_args = TrainingArguments(  
                                    output_dir="./vit-fish-classifier",
                                    per_device_train_batch_size=16,
                                    evaluation_strategy="steps",
                                    num_train_epochs=6,
                                    # fp16=True,
                                    save_steps=100,
                                    eval_steps=100,
                                    logging_steps=10,
                                    learning_rate=2e-4,
                                    save_total_limit=2,
                                    remove_unused_columns=False,
                                    push_to_hub=False,
                                    report_to='tensorboard',
                                    load_best_model_at_end=True,
                                    )
        self.trainer = Trainer(
                    model=self.model,
                    args=self.training_args,
                    data_collator=self.collate_function,
                    compute_metrics=self.compute_metrics,
                    train_dataset=self.prepared_ds["train"],
                    eval_dataset=self.prepared_ds["validation"],
                    tokenizer=self.feature_extractor,
                )

    @staticmethod    
    def collate_function(batch):
        return {
            'pixel_values': torch.stack([x['pixel_values'] for x in batch]),
            'labels': torch.tensor([x['labels'] for x in batch])
        }
    
    def compute_metrics(self,p):
        return self.metric.compute(predictions=np.argmax(p.predictions, axis=1), references=p.label_ids)

test_trainer=TrainingCongfig()
print(test_trainer.prepared_ds)
# %%
