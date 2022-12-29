
#%% Try again.
from datasets import Dataset
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
        self.fish_types = self.get_fish().values()
        self.all_imgs=[]
        for fish_type in self.fish_types:
            self.all_imgs.extend(fish_type.images)
        self.get_dataframe()
        self.dataset=Dataset.from_pandas(self.get_dataframe())
        
    
    def get_fish(self):
        "get the set of all fish image folders"
        fish_map = {}
        fish_fps = listdir_nohidden("images")
        for fish_name in fish_fps:
            fish_map[fish_name] = Fish(fish_name)
        return fish_map
    
    def get_dataframe(self):
        df=pd.DataFrame(self.all_imgs)
        df.columns=['images']  
        df['labels'] = df.images.str.extract(r"/(.*?)/")
        return df

def listdir_nohidden(path):
    "modified listdir function that doesn't return hidden files"
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f



    


# example=Fish('mackerel')
# example.show()
# example.__repr__()

test_dataset=FishDataset()
print(test_dataset.dataset)


# %%
