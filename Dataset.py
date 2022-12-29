#%%
from PIL import Image
import random
import os
class Fish:
    def __init__(self, fish_name):
        self.images = os.listdir(os.path.join("images", fish_name))
        self.images = [os.path.join("images", fish_name, fp)
                       for fp in self.images]
        self.name = fish_name

    def __repr__(self):
        return f"{self.name} ({len(self.images)} images)"

    def show(self):
        img_fp = random.choice(self.images)
        img = Image.open(img_fp)
        img.show()
