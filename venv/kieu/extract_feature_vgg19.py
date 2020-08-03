import tensorflow as tf
from os import listdir
from os.path import isdir
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.models import Model
import numpy as np

base_model = VGG19(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('block4_pool').output)

#
def extract_feature_vgg19(directory):
    feature_test = []
    feature_train = []

    for subdir in listdir(directory):
		# path
        path = directory + subdir + '/'
		# skip any files that might be in the dir
		# if not isdir(path):
		# 	continue
		# load all faces in the subdirectory
        for filename in listdir(path):
            if filename.find('.jpg') != -1:
                img_path = path + filename
                print(filename)
                # ung dung
                img = image.load_img(img_path, target_size=(224, 224))
                img_data = image.img_to_array(img)
                img_data = np.expand_dims(img_data, axis=0)
                img_data = preprocess_input(img_data)
                vgg19_feature = model.predict(img_data)
                vgg19_feature_np = np.squeeze(vgg19_feature)
                if filename.find('_0ID.jpg') != -1:
                    feature_train.append(vgg19_feature_np)
                else:
                    feature_test.append(vgg19_feature_np)
        #
        # labelsTrain = [subdir1 for _ in range(len(feature_train))]
        # labelsTest = [subdir2 for _ in range(len(feature_test))]
        # # summarize progress
        # print('>loaded %d examples for class: %s' % (len(labelsTest), subdir2))
        # print('>loaded %d examples for train: %s' % (len(labelsTrain), subdir1))
    return feature_train, feature_test


feature_test, feature_train = extract_feature_vgg19('E:/Hoc/BMI/venv/kieu/Data/')

print("test")
print(feature_test)
print("train")
print(len(feature_train))
