import python_splitter
import os
from random import shuffle

# Specify the path to the images
pth = r"detection_dataset\train\images"

# Shuffle the list of files (if needed for manual processing)
files = [os.path.join(pth, fle) for fle in os.listdir(pth)]
shuffle(files)

# Perform the split using python_splitter (without needing to shuffle manually if it's handled inside)
python_splitter.split_from_folder(r"detection_dataset\train", train=0.8, val=0.1, test=0.1)
