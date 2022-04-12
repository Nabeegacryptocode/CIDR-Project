from PIL import Image
import random
import os
import seaborn as sns;
from matplotlib import pyplot as plt

sns.set()
import numpy as np
def square_matrix(imagestring):
    imagestring=str(imagestring)
    imagearray = [0, ]
    for i in imagestring:
        imagearray.append(i)
    squarematrix = np.array(imagearray).reshape(11, 11)
    return squarematrix
def returnheatmaps(number):
# Part 1 this is the part that I used to get the classification of each of the access of an image so i have been able to load the image and convert each image to nd array

    def generateimageurl(c):
        arrayofimgurls = []
        images = os.listdir(os.path.join(os.getcwd(), 'MNIST_DS/' + c))
        for img in images:
            arrayofimgurls.append(os.path.join(os.getcwd(), 'MNIST_DS/' + c, img))
        return arrayofimgurls

    folderidentificationarray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_arr = []
    for iden in folderidentificationarray:
        new_arr.append(generateimageurl(iden))
    images_in_folder0 = new_arr[0]
    images_in_folder1 = new_arr[1]
    images_in_folder2 = new_arr[2]
    images_in_folder3 = new_arr[3]
    images_in_folder4 = new_arr[4]
    images_in_folder5 = new_arr[5]
    images_in_folder6 = new_arr[6]
    images_in_folder7 = new_arr[7]
    images_in_folder8 = new_arr[8]
    images_in_folder9 = new_arr[9]

    def open_image_and_covert_to_array(num):
        empty_array = []
        for imgurl in num:
            image = Image.open(imgurl)
            empty_array.append(np.asarray(image))
        return empty_array

    converted0 = open_image_and_covert_to_array(images_in_folder0)
    converted1 = open_image_and_covert_to_array(images_in_folder1)
    converted2 = open_image_and_covert_to_array(images_in_folder2)
    converted3 = open_image_and_covert_to_array(images_in_folder3)
    converted4 = open_image_and_covert_to_array(images_in_folder4)
    converted5 = open_image_and_covert_to_array(images_in_folder5)
    converted6 = open_image_and_covert_to_array(images_in_folder6)
    converted7 = open_image_and_covert_to_array(images_in_folder7)
    converted8 = open_image_and_covert_to_array(images_in_folder8)
    converted9 = open_image_and_covert_to_array(images_in_folder9)
    r3= random.randint(0,9)

    if (number/10==0):
        g= converted0[r3]
    elif (number/10==1):
        g= converted1[r3]

    elif (number/10==2):
        g= converted2[r3]
    elif (number/10==3):
        g= converted3[r3]
    elif (number/10==4):
        g = converted4[r3]
    elif (number/10==5):
        g= converted5[r3]

    elif (number/10==6):
        g= converted6[r3]

    elif (number/10==7):
        g= converted7[r3]
    elif (number/10==8):
        g = converted8[r3]
    elif (number/10==9):
        g= converted9[r3]
    else :
        g = converted0[1]


    ax = sns.heatmap(g, annot=True, fmt="d")
    plt.show()


