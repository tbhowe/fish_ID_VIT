#%%
from PIL import Image
import os
from fnmatch import fnmatch
def get_image_fps(imagedir):
    image_file_list=[]
    root = 'images/'
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                image_file_list.append(os.path.join(path, name))

    return(image_file_list)
    

def force_image_type(image_file_list):
    for image_path in image_file_list:
        example_image=Image.open(image_path)
        if example_image.mode == 'RGBA':
            example_image=pure_pil_alpha_to_color_v2(example_image)
            example_image.save(image_path)
    
def pure_pil_alpha_to_color_v2(image, color=(255, 255, 255)):
    """Alpha composite an RGBA Image with a specified color.

    Simpler, faster version than the solutions above.

    Source: http://stackoverflow.com/a/9459208/284318

    Keyword Arguments:
    image -- PIL RGBA Image object
    color -- Tuple r, g, b (default 255, 255, 255)

    """
    image.load()  # needed for split()
    background = Image.new('RGB', image.size, color)
    background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
    return background

def listdir_nohidden(path):
        for f in os.listdir(path):
            if not f.startswith('.'):
                yield f
    


image_list=get_image_fps('images/')
print(image_list)
force_image_type(image_list)

example_image=Image.open('images/ballan/img_1.png')
print(example_image.mode)

# %%
