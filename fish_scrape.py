from google_images_download import google_images_download


def download_fish_images(fish_type,prefix_string,number_of_images,chromedriver_path):
    ''' Function scrapes google for images based on keyword
        
        input args:
            fish_type (str)         - keyword of interest
            prefix_string (str)     - additional keywords as prefix (eg. river name)
            number_of_images (int)  - limit number of images to download
            chromedriver path (str) - path to local chromedriver install
            
        top n images are scraped from google and downloaded 
        into path specified in "output_directory '''

    response = google_images_download.googleimagesdownload() 
    arguments = {"keywords": fish_type,  
                "prefix_keywords": prefix_string, 
                "limit":number_of_images,
                "print_urls":False,
                'output_directory':'fish_images/', 
                'chromedriver': chromedriver_path, 
                'extract_metadata':False,
                'type':'photo' ,
                'size': 'medium',
                'thumbnail_only':False} 
                
    response.download(arguments) 

# script:
    
chromedriver_path='/Users/rrritalin/miniconda3/envs/zoopla/bin/chromedriver'
number_of_images=50
fish_type='perch'
prefix_string=None
download_fish_images(fish_type,prefix_string,number_of_images,chromedriver_path)
