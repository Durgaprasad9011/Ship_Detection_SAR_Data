# Ship Detection in SAR (Synthetic Aperture radar) Data

## Data Preparation:

1) Initially, I downloaded the dataset from the provided repository, HRSID. Within this repository, a link was available for downloading the dataset.

2) The dataset comprises 5604 images, and the annotations are specified in the files: train2017.json, test2017.json, and train_test.json.

3) To organize the dataset, I utilized the information from train.json. I mapped image names in the JSON file to the corresponding folders containing images. Subsequently, I moved the mapped images to the "train" folder. This process was repeated for the "test" folder, resulting in a dataset split of 65% for training and 35% for testing.

4) For each image file, I generated a corresponding text file with annotations in the YOLO-supported format. The bounding box (bbox) values were extracted from the respective train.json and test.json files. These values were then normalized by the height and width of the images, with a class information column added (prefixed with 0). YOLO requires annotations in a 5-column format [class, x_min, y_min, z_max, y_max].


5) The dataset folder structure is now organized as follows:
    
    SUHORA INTERNSHIP
    |
    |--> train
    |       |
    |       |--> images
    |       |       |-> P0001_0_800_7200_8000.jpg
    |       |       |-> P0001_0_800_8400_9200.jpg
    |       |       |  ...
    |       |
    |       |--> labels
    |               |-> P0001_0_800_7200_8000.txt
    |               |-> P0001_0_800_8400_9200.txt
    |               |  ...
    |
    |--> val
            |
            |--> images
            |       |-> P0001_0_800_10190_10990.jpg
            |       |-> P0001_1200_2000_3600_4400.jpg
            |       |  ...
            |
            |--> labels
                    |-> P0001_0_800_10190_10990.txt
                    |-> P0001_1200_2000_3600_4400.txt
                    |  ...
    

Download the extracted dataset from [this link](www.googledrive.durga.com).

## Model Training:

- Used YOLOv8 Model for Ship Detection and trained on the dataset.
- Find the best model weights in the weights folder (best.pt).
- View training results in "[results.csv](results.csv)".

*Check the Code:*

- For more details on model training and evaluation, refer to the code in ship_detection.ipynb or ship_detection.py.

## Quantitative Results:

| Precision | Recall | mAP50 | mAP50-95 |
|-----------|--------|-------|----------|
| 0.906     | 0.777  | 0.879 | 0.626    |

## Qualitative:

### Results Plot:
![Results Plot](runs/detect/train/results.png)

### Confusion Matrix:
![Confusion Matrix](runs/detect/train/confusion_matrix.png)


*More results can be found in runs/detect/train folder.*
 
## Predictions:

| Left Image (1.jpg) | Right Image (2.jpg) |
|--------------------|----------------------|
| ![1.jpg](1.jpg)     | ![2.jpg](2.jpg)      |
| ...                | ...                  |

## Reference Paper:

Link to the reference paper comes here.
