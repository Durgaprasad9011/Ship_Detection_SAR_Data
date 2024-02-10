#!/usr/bin/env python
# coding: utf-8

# In[1]:


''' To organize the dataset, I utilized the information from train.json. I mapped image names in the JSON file to the corresponding folders containing images. Subsequently, I moved the mapped images to the "train" folder. This process was repeated for the "test" folder, resulting in a dataset split of 65% for training and 35% for testing. '''


# In[ ]:


import os
import json
import shutil


# In[ ]:


def move_images(json_file, source_folder, destination_folder):
    with open(json_file, 'r') as f:
        data = json.load(f)

    for image_info in data["images"]:
        image_name = image_info["file_name"]
        source_path = os.path.join(source_folder, image_name)
        destination_path = os.path.join(destination_folder, image_name)
        shutil.move(source_path, destination_path)
        print(f"Moved {image_name} to {destination_folder}")

def split_images(train_json, test_json, source_folder, train_folder, test_folder):
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    move_images(train_json, source_folder, train_folder)
    move_images(test_json, source_folder, test_folder)

if _name_ == "_main_":
    source_folder = "path"
    train_folder = "path"
    test_folder = "path"
    train_json = "path"
    test_json = "path"

    split_images(train_json, test_json, source_folder, train_folder, test_folder)


# In[2]:


'''For each image file, I generated a corresponding text file with annotations in the YOLO-supported format. The bounding box (bbox) values were extracted from the respective train.json and test.json files. These values were then normalized by the height and width of the images, with a class information column added (prefixed with 0).'''


# In[ ]:


annotations_file = 'path'
output_annotations_dir = 'path'
os.makedirs(output_annotations_dir, exist_ok=True)

with open(annotations_file) as f:
    coco_annotations = json.load(f)

def convert_to_yolo_format(box, img_width, img_height):
    x_center = (box[0] + box[2] / 2) / img_width
    y_center = (box[1] + box[3] / 2) / img_height
    width = box[2] / img_width
    height = box[3] / img_height
    return [x_center, y_center, width, height]

id_to_file = {img['id']: img['file_name'] for img in coco_annotations['images']}

for ann in coco_annotations['annotations']:
    img_id = ann['image_id']
    img_file_name = id_to_file[img_id]
    bbox = ann['bbox'] 
    img_data = next((img for img in coco_annotations['images'] if img['id'] == img_id), None)
    if img_data is None:
        continue
    img_width, img_height = img_data['width'], img_data['height']
    yolo_bbox = convert_to_yolo_format(bbox, img_width, img_height)
    line = f"0 {' '.join(map(str, yolo_bbox))}\n"
    yolo_file_path = os.path.join(output_annotations_dir, os.path.splitext(img_file_name)[0] + '.txt')
    with open(yolo_file_path, 'a') as file:
        file.write(line)

print("Conversion to YOLO format completed.")

