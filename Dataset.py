
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
        self.dataset=load_dataset("imagefolder", data_dir="images/" )['train']
        # self.fish_species=self.get_species()
        self.fish_species=self.dataset.features['label'].names
        self.dataset=self.dataset.train_test_split(test_size=0.3)
        self.splitter=self.dataset['test'].train_test_split(test_size=0.5)
        self.dataset['test']=self.splitter['test']
        self.dataset['validation']=self.splitter['train']
        

    def get_species(self):
        return self.listdir_nohidden("images/")

    def get_one_example(self,idx):
        example=self.dataset['train'][idx]
        return example

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

    
    
    @staticmethod
    def listdir_nohidden(path):
        for f in os.listdir(path):
            if not f.startswith('.'):
                yield f
    


    



if __name__ == '__main__':
    test_dataset=FishDataset()
    example=test_dataset.get_one_example(400)
    print(example)
    # print(test_dataset.dataset)
    # print(test_dataset.fish_species)
    # labels = test_dataset.dataset['train'].features['label'].names
    # print(labels)
    # test_dataset.show_examples()
    # model_name_or_path = 'google/vit-base-patch16-224-in21k'
    # feature_extractor = ViTFeatureExtractor.from_pretrained(model_name_or_path)
    # prepared_ds = test_dataset.dataset.with_transform(test_dataset.transform)

# %%
