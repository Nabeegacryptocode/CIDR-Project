
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from Barcode_Generator import *
def square_matrix(imagestring):
    imagestring=str(imagestring)
    imagearray = [0, ]
    for i in imagestring:
        imagearray.append(i)
    squarematrix = np.array(imagearray).reshape(11, 11)
    return squarematrix


def findalgo(drawndigs, imgtolookfr, Matchingimages, matchsaved, iterator=1):
    imgs = drawndigs
    Querys = imgtolookfr
    hits = Matchingimages
    saveChoice = matchsaved
    Name9 = int(Querys / 10)
    image = np.asarray(imgs[Querys])
    convertedimgcd = Barcodegenerator(image)




    q= open("barcodes.txt", "r")
    strokes =q.readlines()
    q.close()
    Hdistancesvd = 1000
    sdIndex = None
    


    for j in range(0,len(strokes),1):
        stroke = strokes[j]
        stroke = stroke[:-1]
        
        Distancefrh = 0
        if len(convertedimgcd)!=len(stroke):
            print("The strings are disimilair")
        else:
            for x,(f,d) in enumerate(zip(stroke, convertedimgcd)):
                if f!=d:
                    Distancefrh += 1

        if(Distancefrh < Hdistancesvd and Distancefrh != 0):
            Hdistancesvd = Distancefrh
            sdIndex = int(j)

    similair_matrix =strokes[sdIndex][:-1]
    print('Hamming distance', Hdistancesvd)
    print('Square Array of original image \n ',square_matrix(convertedimgcd))
    print('Square Array of matching image \n ', square_matrix(similair_matrix))
    print("Total number of matches found:", int(sdIndex / 10))
    if(int(sdIndex / 10)==Name9):
        hits +=iterator


        if (saveChoice == 1):
                S, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
                ax1.imshow(get_image(Querys))
                ax1.set_facecolor('blue')
                ax1.axis('off')
                ax1.set_title('Successful')
                ax2.imshow(get_image(sdIndex))
                ax2.set_facecolor('blue')
                ax2.axis('off')
                ax2.set_title('Match')
                S.savefig('matches\\{}.png'.format(Querys), dpi=S.dpi)
    else:
        if (saveChoice == 1):
            S, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
            ax1.imshow(get_image(Querys))
            ax1.set_title('Failed')
            ax1.set_title('Successful')
            ax1.axis('off')
            ax2.imshow(get_image(sdIndex))
            ax2.axis('off')
            ax2.set_facecolor('blue')
            ax2.set_title('Match')
            S.savefig('matches\\{}.png'.format(Querys), dpi=S.dpi)
    return hits

def find_all(images, Matchingimages, saveImg):
    figure = images
    founds = Matchingimages
    saveChoice = saveImg

    for i in range(0,figure.shape[0]):
        index = i
        founds = findalgo(images, index, founds, saveChoice)
    

    print("Correct matches:",founds)


images = Openimgs()

BooleanController = False

while(BooleanController != True):
    print("Hello welcome to our CBIR program this program comes in 2 parts  \n One for calculating hit ratio \n and another for looking for matches given a specific query image. ")

    searchChoice = input("How would you like to proceed \n 1. Calculating hit ratio \n 2. Searching for a Matches using a specific query image \n (Please input 1 or 2):")

    if(searchChoice == "1"):
        BooleanController = True

    elif(searchChoice == "2"):
        BooleanController = True

    else:
        print("Invalid Entry try again")


BooleanController= False

while(BooleanController != True):
   print("\n Great choice , Your images will be saved to a folder called matches located in the project directory \n Would you like to proceed ?")
   saved=input("\n1.Yes\n2 .No \n (Please make a selection 1 or 2)")
   if (saved =="1"):
       saved= int(saved)
       BooleanController = True
   else:
       print("Thank you for your time feel free to exit out of the app")
       BooleanController = True

BooleanController = False
Matchingimages = 0
if (searchChoice == "1"):
    for i in range(0,images.shape[0]):
        Find = i
        Matchingimages = findalgo(images, Find, Matchingimages, saved)
    print("Your hit ratio is", Matchingimages ,"%")
    print("Thank you for your time!!!!!")



elif (searchChoice=="2"):
    print("Welcome to the query selector here you can input the index of an image and we will search for matches among the datset!! \n Lets get started")
    BooleanController = False
    while(BooleanController != True):
        #Obtain index of the image
        Find = input("Enter the index of query image (1-100) ")
        try:
            Find = int(Find)
            if(Find<=100 and Find>=1):
                Find -= 1
                BooleanController = True
        except:
            print("Invalid Entry try again")
    findalgo(images, Find, Matchingimages, saved)


