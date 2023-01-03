# fish_ID_VIT
Can we train a visual transformer network to identify fish species?

## Milestone 1:  Download example images from Google

The file fish_scrape.py contains a class GetImages, containing methods which use Selenium with Chrome Webdriver to access the google images site, clear the GDPR cookies popup, and download a pre-determined number of images corresponding to a given keyword search.

An instance of GetImages is passed a set of 10 keywords, each corresponding to a species of fish. The images for each keyword are downloaded to their own subfolder inside /images/ .

### Milestone 2: create the dataset from the images folder.

The dataset is created as an instance of the FishDataset class, defined in Dataset.py. The class contains methods to load the images from the /images/ folder into a transformers dataset, as well as to display example images from the dataset:

### Methods:
 
 - get_species() - builds a list of fish species based on directory structure of /images/. 
 - get_one_example() - returns a single example from the dataset
 - show_examples(seed,examples_per_class) - returns a grid of m by n images, where m is the number of categories in the dataset, and n is the number of examples to show per category.


## Milestone 3: implement a VIT model
The implementation of the VIT model leverages the Hugginface Transformers library, and is based around a class TrainingConfig, defined in trainer.py. The class constructor specifies the model, feature extractor, and the various hyperparameters and metrics for the training process. Methods defined within the class permit the collation of examples from the dataset into a batch, application of the feature extractor to the batch, and computation of the accuracy metric on the batch predictions.





