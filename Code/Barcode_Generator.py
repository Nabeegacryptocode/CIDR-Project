import os
import numpy as np
import skimage.transform as ski
from cv2 import cv2
#Function in order to open images and crop them
def Openimgs():

    Croppedimgs = np.empty((0,20,20))

    for i in range(0,10,1):
        for FILENAME in os.listdir('MNIST_DS\\{}'.format(i)):
            img = cv2.imread(os.path.join('MNIST_DS\\{}'.format(i),FILENAME),0)
            if img is not None:
                Oimg = np.array(img)
                crimg = Oimg[6:26,6:26]
                Croppedimgs = np.append(Croppedimgs,[crimg], axis=0)
    return Croppedimgs
#Get image function
def get_image(index):
    filename = os.listdir('MNIST_DS\\{}'.format(int(index/10)))
    img = cv2.imread(os.path.join('MNIST_DS\\{}'.format(int(index/10)),filename[int((str(index))[-1])]),0)
    if img is not None:
        return img
#Barcodegenerator function with projections
def Barcodegenerator(image):
    bcde = np.array([])
    for i in range(0,180,30):
        VectorProjection = ski.radon(image, [i], circle=True, preserve_range=True)
        Thresholdvalues = np.mean(VectorProjection)
        for i in range(0, VectorProjection.size, 1):
            if (VectorProjection[i]>=Thresholdvalues):
                VectorProjection[i] = 1
            else:
                VectorProjection[i] = 0

        bcde = np.append(bcde, VectorProjection)


    stringcode = ''
    for i in range(0, bcde.size, 1):
        stringcode += str(int(bcde[i]))

    return stringcode


def Barcodesetgen():
    try:
#Opens barcodes.txt
        f = open("barcodes.txt", "x")
    except:
        f = open("barcodes.txt", "w")
#Accessing each image in the dataset in order to convert and crop.
    images = Openimgs()
    num_images = images.shape[0]

#Iterates within the dataset images converting each to a binary string and writing to file Barcodes.txt each on a new line
    for i in range(0,num_images,1):
        code_string = Barcodegenerator(np.asarray(images[i]))
        f.write(code_string +'\n')
#Closing of barcodes.txt file
    f.close()

Barcodesetgen()
