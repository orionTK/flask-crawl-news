import tensorflow as tf
from os import listdir
from os.path import isdir
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet')
#
def extract_feature_resnet50(directory):
    feature_test = []
    feature_train = []

    for subdir in listdir(directory):
		# path
        path = directory + subdir + '/'
        for filename in listdir(path):
            if filename.find('.jpg') != -1:
                img_path = path + filename
                print(filename)
                # ung dung
                img = image.load_img(img_path, target_size=(224, 224))
                img_data = image.img_to_array(img)
                img_data = np.expand_dims(img_data, axis=0)
                img_data = preprocess_input(img_data)
                resnet_feature = model.predict(img_data)
                resnet_feature = np.squeeze(resnet_feature)
                if filename.find('_0ID.jpg') != -1:
                    feature_train.append(resnet_feature)
                else:
                    feature_test.append(resnet_feature)

    return feature_train, feature_test


feature_test, feature_train = extract_feature_resnet50('E:/Hoc/BMI/venv/kieu/Data/')

print("test")
print(feature_test)
print("train")
print(len(feature_train))
