# Data Preparation for Animal Recognition

This module extracts image frames from drone videos for use in training detection and classification models.

## Folder Contents

- `extract_images_from_video.py`: Script to extract frames from `.ts` video files.
- `videos/`: Folder containing raw drone video files organized by animal class (e.g., `pig`, `deer`, `kangaroo`).
- `images/`: Output folder where extracted frames are saved, organized in the same class-wise structure.

## How to Use

Navigate to the `data_preparation` folder and run:

```bash
python extract_images_from_video.py
```  

**Note:** To maintain data confidentiality, only one example per class is retained in the 'images' folder.


# Data Preparation for Animal Recognition

This module extracts image frames from drone videos for training detection and classification models.

## Folder Contents

- `extract_images_from_video.py`: Script to extract frames from `.ts` video files.
- `videos/`: Folder containing raw drone video files organized by animal class (e.g., `pig`, `deer`, `kangaroo`).
- `images/`: Output folder where extracted frames are saved, organized in the same class-wise structure.

## How to Use

Navigate to the `data_preparation` folder and run:

```bash
python extract_images_from_video.py
```

This will extract frames from videos save them into the `images/` folder.

**Note:** Only one example per class is retained in the `images/` folder to preserve data confidentiality.
