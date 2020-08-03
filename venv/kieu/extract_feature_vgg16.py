import tensorflow as tf
from os import listdir
from os.path import isdir
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import numpy as np

model = VGG16(weights='imagenet', include_top=False)
model.summary()

#
def extract_feature(directory):
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
                vgg16_feature = model.predict(img_data)
                vgg16_feature_np = np.squeeze(vgg16_feature)
                if filename.find('_0ID.jpg') != -1:
                    feature_train.append(vgg16_feature_np)
                else:
                    feature_test.append(vgg16_feature_np)
        #
        # labelsTrain = [subdir1 for _ in range(len(feature_train))]
        # labelsTest = [subdir2 for _ in range(len(feature_test))]
        # # summarize progress
        # print('>loaded %d examples for class: %s' % (len(labelsTest), subdir2))
        # print('>loaded %d examples for train: %s' % (len(labelsTrain), subdir1))
    return feature_train, feature_test


feature_test, feature_train = extract_feature('E:/Hoc/BMI/venv/kieu/Data/')
print(feature_train)
