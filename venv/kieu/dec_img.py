# face detection for the 5 Celebrity Faces Dataset
from os import listdir
from os.path import isdir
from PIL import Image
from matplotlib import pyplot
from numpy import savez_compressed
from numpy import asarray
from numpy import load
# from keras.models import load_model
from mtcnn.mtcnn import MTCNN
# model = load_model('facenet_keras.h5')
# extract a single face from a given photograph
def extract_face(filename, required_size=(160, 160)):
	# load image from file
    img1 = Image.open(filename)  # open the image
    img1 = img1.convert('RGB')  # convert the image to RGB format
    pixels = asarray(img1)  # chuyển từ ảnh sang mảng
    detector = MTCNN()  # assign the MTCNN detector
    f = detector.detect_faces(pixels)
    # fetching the (x,y)co-ordinate and (width-->w, height-->h) of the image
    x1, y1, w, h = f[0]['box']
    x1, y1 = abs(x1), abs(y1)
    x2 = abs(x1 + w)
    y2 = abs(y1 + h)
    # locate the co-ordinates of face in the image
    store_face = pixels[y1:y2, x1:x2]
    plt.imshow(store_face)
    image1 = Image.fromarray(store_face, 'RGB')  # convert the numpy array to object
    image1 = image1.resize((160, 160))  # resize the image
    face_array = asarray(image1)  # image to array
    return face_array

# load images and extract faces for all images in a directory

def load_faces(directory,i):
	facesTest , facesTrain = [], []
	# dem=0;
	k = 0;
	# enumerate files
	for filename in listdir(directory):
		# path

		if filename.find('.jpg') != -1:
			path = directory + filename
			face = extract_img(path)
			if filename.find('_0ID.jpg') != -1:
				facesTrain.append(face)
			else:

				facesTest.append(face)

		# # get face
		#
		# store
		#
	if i == 0:
		return facesTrain
	else:
		return facesTest


# load a dataset that contains one subdir for each class that in turn contains images
# def load_dataset(directory, i):
#     x, y = [], []
#     i = 1
# 	# enumerate folders, on per class
#     for subdir in listdir(directory):
# 		# path
# 		path = directory + subdir + '/'
# 		# load all faces in the subdirectory
# 		faces= load_faces(path, i);
# 		# create labels
# 		labels = [subdir for _ in range(len(faces))]
# 		# summarize progress
# 		print('>loaded %d examples for class: %s' % (len(faces), subdir))
# 		# store
# 		X.extend(faces)
# 		y.extend(labels)
# 	return asarray(X), asarray(y)
#
# # load train dataset
# trainX, trainy = load_dataset('C:/Users/SV_Guest/Desktop/Kieu/FaceNet/venv/FaceNetBT/Dataset/Data/', 0)
# print(trainX.shape, trainy.shape)
# # # load test dataset
# testX, testy = load_dataset('C:/Users/SV_Guest/Desktop/Kieu/FaceNet/venv/FaceNetBT/Dataset/Data/', 1)
# print(testX.shape, testX.shape)
#
# # # save arrays to one file in compressed format
# savez_compressed('dataf.npz', trainX, trainy, testX, testy)
#
#
# # load the face dataset
# with load('dataf.npz') as data:
# 	trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
# print('Loaded: ', trainX.shape, trainy.shape, testX.shape, testy.shape)

for subdir in listdir('E:/Hoc/BMI/venv/kieu/Data/'):
# 		# path
    path = 'E:/Hoc/BMI/venv/kieu/Data/' + subdir + '/'
# 		# load all faces in the subdirectory
    faces= load_faces(path, 1);