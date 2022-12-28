#%%
from datasets import load_dataset
from datasets import load_metric
from datasets import list_datasets
from datasets import features
from PIL import ImageDraw, ImageFont, Image
from transformers import ViTFeatureExtractor
import numpy as np
import random
import torch







    

def show_examples(  ds, 
                    seed: int = 1234, 
                    examples_per_class: int = 3, 
                    size=(350, 350)):
    ''' show an nx3 panel of example images from the dataset, where n is number of classes'''

    width, height = size
    labels = ds['train'].features['labels'].names
    grid = Image.new('RGB', size=(examples_per_class * width, len(labels) * height))
    draw = ImageDraw.Draw(grid)
    # font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", 24)

    for label_id, label in enumerate(labels):
        # Filter the dataset by a single label, shuffle it, and grab a few samples
        ds_slice = ds['train'].filter(lambda ex: ex['labels'] == label_id).shuffle(seed).select(range(examples_per_class))
        # Plot this label's examples along a row
        for i, example in enumerate(ds_slice):
            image = example['image']
            idx = examples_per_class * label_id + i
            box = (idx % examples_per_class * width, idx // examples_per_class * height)
            grid.paste(image.resize(size), box=box)
            draw.text(box, label, (255, 255, 255))
            
    return(grid)

def process_example(example):
    inputs = feature_extractor(example['image'], return_tensors='pt')
    inputs['labels'] = example['labels']
    return inputs

def transform(example_batch):
    # Take a list of PIL images and turn them to pixel values
    inputs = feature_extractor([x for x in example_batch['image']], return_tensors='pt')
    # include the labels
    inputs['labels'] = example_batch['labels']
    return inputs

def collate_function(batch):
    return {
        'pixel_values': torch.stack([x['pixel_values'] for x in batch]),
        'labels': torch.tensor([x['labels'] for x in batch])
    }

# get dataset
ds = load_dataset('beans')
show_examples(ds, seed=random.randint(0, 1337), examples_per_class=3)

# setup model
model_name_or_path = 'google/vit-base-patch16-224-in21k'
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name_or_path)
prepared_ds = ds.with_transform(transform)


# %%
