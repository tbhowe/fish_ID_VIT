#%%
from datasets import load_dataset
from datasets import list_datasets
from datasets import features
import random
from PIL import ImageDraw, ImageFont, Image

def show_examples(  ds, 
                    seed: int = 1234, 
                    examples_per_class: int = 3, 
                    size=(350, 350)):
    
    ''' show an nx3 panel of example images from the dataset, where n is number of classes'''

    width, height = size
    labels = ds['train'].features['labels'].names
    grid = Image.new('RGB', size=(examples_per_class * width, len(labels) * height))
    draw = ImageDraw.Draw(grid)
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", 24)

ds = load_dataset('beans')

example = ds['train'][400]
image = example['image']
image
labels = ds['train'].features['labels']
labels.int2str(example['labels'])



# %%
