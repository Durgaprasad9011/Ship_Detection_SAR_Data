#!/usr/bin/env python
# coding: utf-8

# ## Verifying CUDA Installation for GPU Utilization

# In[31]:


import torch


# In[2]:


torch.__version__


# In[3]:


torch.cuda.is_available()


# ## Installing ultralytics for YOLO Implementation

# In[5]:


#I ran the code but to minimize the notebook length, and I have simply commented it.
# ! pip install ultralytics


# ## Importing essential libraries

# In[62]:


import os
import random
from PIL import Image
from IPython.display import Image, display
from ultralytics import YOLO


# ## Data

# In[72]:


def count_images_in_folder(folder_path):
    images_folder_path = os.path.join(folder_path, 'images')
    
    if not os.path.exists(images_folder_path):
        print(f"Warning: 'images' folder not found in {folder_path}")
        return 0
    
    num_images = len([f for f in os.listdir(images_folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))])
    return num_images

def count_text_files_in_folder(folder_path):
    labels_folder_path = os.path.join(folder_path, 'labels')
    
    if not os.path.exists(labels_folder_path):
        print(f"Warning: 'labels' folder not found in {folder_path}")
        return 0
    
    num_text_files = len([f for f in os.listdir(labels_folder_path) if f.endswith('.txt')])
    return num_text_files
    
dataset_path = "C:\\SUHORA INTERNSHIP"

train_path = os.path.join(dataset_path, 'train')
val_path = os.path.join(dataset_path, 'val')

num_train_images = count_images_in_folder(train_path)
num_val_images = count_images_in_folder(val_path)

print(f"Number of images in 'train' folder: {num_train_images}")
print(f"Number of images in 'val' folder: {num_val_images}")
print()
print(f"Number of text files in 'train' folder: {num_train_text_files}")
print(f"Number of text files in 'val' folder: {num_val_text_files}")


# ## Model Training

# In[6]:


model = YOLO('yolov8n.yaml')


# In[7]:


result = model.train(data='dataset.yaml', epochs=100, imgsz=640, workers=1, batch=8)


# ## Evaluation and Testing

# In[11]:


infer=YOLO("C:\\SUHORA INTERNSHIP\\runs\\detect\\train\\weights\\best.pt")


# In[ ]:


#I ran the code but to minimize the notebook length, and I have simply commented it.
#infer.predict("C:\\SUHORA INTERNSHIP\\val\\images", save=True,save_txt=True)


# In[58]:


def display_random_images(folder_path, num_images=5):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg'))]
    selected_images = random.sample(image_files, min(num_images, len(image_files)))
    
    for image in selected_images:
        img_path = os.path.join(folder_path, image)
        display(Image(filename=img_path))

folder_path = "C:\\SUHORA INTERNSHIP\\runs\\detect\\predict"
display_random_images(folder_path, num_images=5)


# ## Results

# In[66]:


display(Image("C:\\SUHORA INTERNSHIP\\runs\\detect\\train\\results.png"))


# In[65]:


display(Image("C:\\SUHORA INTERNSHIP\\runs\\detect\\train\\confusion_matrix.png"))


# In[68]:


display(Image(filename="C:\\SUHORA INTERNSHIP\\runs\\detect\\train\\F1_curve.png"), 
        Image(filename="C:\\SUHORA INTERNSHIP\\runs\\detect\\train\\P_curve.png"),
       Image(filename="C:\\SUHORA INTERNSHIP\\runs\\detect\\train\\PR_curve.png"),
       Image(filename="C:\\SUHORA INTERNSHIP\\runs\\detect\\train\\R_curve.png"))


# In[ ]:




