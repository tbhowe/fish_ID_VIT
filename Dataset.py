
#%% Try again.
from datasets import load_dataset
import random
import os
import pandas as pd
from datasets import features
from PIL import ImageDraw, ImageFont, Image
from transformers import ViTFeatureExtractor


class Fish:
    "all images of an individual species category"
    def __init__(self, fish_name):
        self.images = listdir_nohidden(os.path.join("images", fish_name))
        self.images = [os.path.join("images", fish_name, fp)
                       for fp in self.images]
        self.name = fish_name

    def __repr__(self):
        "print number of images in category"
        return f"{self.name} ({len(self.images)} images)"

    def show(self):
        "show example image from category"
        img_fp = random.choice(self.images)
        img = Image.open(img_fp)
        img.show()

class FishDataset:

    def __init__(self):
        '''class constructor'''
        self.dataset=load_dataset("imagefolder", data_dir="images/")
        self.fish_species=self.dataset['train'].features['label'].names
    
    def show_examples(self,
                        seed: int = 1234, 
                        examples_per_class: int = 3, 
                        size=(350, 350)):
        ''' show an nx3 panel of example images from the dataset, where n is number of classes'''

        width, height = size
        labels = self.dataset['train'].features['label'].names
        grid = Image.new('RGB', size=(examples_per_class * width, len(labels) * height))
        draw = ImageDraw.Draw(grid)
        # font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", 24)
        for label_id, label in enumerate(labels):
            # Filter the dataset by a single label, shuffle it, and grab a few samples
            ds_slice = self.dataset['train'].filter(lambda ex: ex['label'] == label_id).shuffle(seed).select(range(examples_per_class))
            # Plot this label's examples along a row
            for i, example in enumerate(ds_slice):
                image = example['image']
                idx = examples_per_class * label_id + i
                box = (idx % examples_per_class * width, idx // examples_per_class * height)
                grid.paste(image.resize(size), box=box)
                draw.text(box, label, (255, 255, 255))
                
        return(grid)
    
    def transform(example_batch):
        # Take a list of PIL images and turn them to pixel values
        inputs = feature_extractor([x for x in example_batch['image']], return_tensors='pt')
        # include the labels
        inputs['labels'] = example_batch['labels']
        return inputs


    


# example=Fish('mackerel')
# example.show()
# example.__repr__()

test_dataset=FishDataset()
# labels = test_dataset.dataset['train'].features['label'].names
# print(labels)
test_dataset.show_examples()

# %%
