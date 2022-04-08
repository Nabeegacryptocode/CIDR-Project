# CBIR-Barcode
Content based image retrieval program using radon barcodes generated for 28x28 pixel handwritten digits, in Python.
The CBIR pdf contained within the main folder includes the full version of this report including sample images.

Created by Daniel Gohara Kamel and Jessica Leishman

## Introduction
This report seeks to explore the use of content based image retrieval through the use of handwritten digits and the radon barcode method. Using a text-based image search can only be as accurate as the annotations on an image; utilizing an image as a query yields new data possibilities and patterns not inherently visible to the human eye. This leads to new and unique ways to approach the typical keyword search.

Images are composed of pixels, which are a series of bits that describe the colour to be displayed. This program procedurally analyzes these images by taking various projection angles that emanate from the centre of the image, as this is an effective way to get several “snapshots” of what the image might be. This was then used to generate a barcode and compare this to other images to find similar images.

For this program, the images in the MNIST_DS folder provided are used as both the user_given_dataset and the dataset to compare against.

## Required Packages and Folders
This repository should contain an empty folder called matches. This must be present in order for the use of the program. If you do not see this, please create it.

In addition to this folder, please ensure the following packages are installed on your system:
OpenCV
NumPy
Scikit-image
Matplotlib
pillow

---
## Retrieval Accuracy in Terms of Hit Ratio(%):
The retrieval accuracy of the program created is 73%. Each of the 100 images within the dataset were used as the query.

Each category had varying success rates, as can be seen in the breakdown below:

**Table 1: Hit Ratio Breakdown of 12 Projection method:**
| Digit: | Correct Match Percentage by Digit | Digit of Incorrect Matches:|
| ---- | ----| ---- |
| 0 | 90% | 1 |
| 1 | 100% | N/A |
| 2 | 90% | 8 |
| 3 | 70% | 4,5,6,7 |
| 4 | 70% | 6,6,6 |
| 5 | 50% | 3, 4, 6, 6, 9|
| 6 | 80% | 4, 5 |
| 7 | 70% | 1, 2, 9|
| 8 | 50% | 5, 7, 9, 9, 9|
| 9 | 70% | 4, 7, 7 |

**Table 2: Barcode Generation and Search Algorithm Times of 4 and 12 Projections:**
| Method: | 4 Projections | 12 Projections |
| ---- | ---- | ----|
| Hit Ratio (cropped images) | 68% | 73% |
| Average* time to generate barcodes (ms) | 95.535755157470703125 | 231.7333221435546875 |
| Average* time to find query index 1 match (ms) | 4.9550533294677734375 | 13.066530227661132813 |
| Average* time to find query index 50 match (ms) | 6.9320201873779296875 | 18.4078216552734375 |
| Average* time to find query index 100 match (ms) | 5.9814453125 | 15.038728713989257813 |
| Average* time to find single query match (ms) | 5.95617294311523 |15.5043601989746 |
| Average* time to find and save single query match (ms) | 232.150872548421 | 225.95238685607910156 |
| Average* time to find all matches (ms) | 358.28065872192382813 (0.3583 seconds) | 673.38228225708007813 (0.6734 seconds) |
| Average* time to find and save all matches (ms) | 17575.805187225341797 (17.5758 seconds) | 18359.216213226318359 (18.3592 seconds) |

*_each average time was taken from 5 sample runs of the program under the same conditions._

---
## Results Analysis
### Process Analysis:
Searching using the original images un-cropped using the 4 recommended projections 0, 45, 90, 135 degrees resulted in a hit accuracy of 51%

Increasing the number of projections from the recommended 4 to 9 using 15 degree increments allowed the program to achieve a hit accuracy of 59%. These projections were taken from [0°,135°]. 

The images were then cropped to remove blank space that made a border around most of the digits in the dataset. They were first cropped to a 20x20 pixel image, using rows and columns 3 to 23 of the image-array, which yielded a hit accuracy of 67%. This was further refined to an 18x18 pixel image, using rows and columns 4 to 22 to produce a hit accuracy of 69%. This final crop of rows and columns 4 to 22 was found by trial and error, and was the best setting found for this data set. 

Further increasing the projections to 12, using 15 degree increments over [0°,165°] resulted in an accuracy increase of 4%, increasing the final hit accuracy to 73%


### Running Time Analysis:
With 4 projections, the barcode generation takes 95.535755157470703125 ms (0.0955 seconds). The time to generate the matches for the entirety of the dataset is 358.28065872192382813 ms (0.3583 seconds), and the time to generate these matches and save them to the test computer is 17575.805187225341797 ms (17.5758 seconds).
The hit accuracy was 68%.

The time to generate a single match with 4 projections for dataset index 1, 50, and 100 were 4.9550533294677734375 ms (0.0050 seconds), 6.9320201873779296875 ms (0.0069 seconds), and 5.9814453125 (0.0060 seconds) respectively.

The time to generate a single match and save it to the test computer with 4 projections for dataset index 1, 50, and 100 were 211.60602569580078125 ms (0.2116 seconds), 216.46332740783691406 ms (0.2165 seconds), and 268.38326454162597656 ms (0.2684 seconds) respectively.

With 12 projections, the barcode generation takes 231.7333221435546875 ms (0.2317 seconds). The time to generate the matches for the entirety of the dataset is 673.38228225708007813 ms (0.6734 seconds), and the time to generate these matches and save them to the test computer is 18359.216213226318359 ms (18.3592 seconds).

The time to generate a single match with 12 projections for dataset index 1, 50, and 100 were 13.066530227661132813 ms (0.0131 seconds), 18.4078216552734375 ms (0.0184 seconds),  and 15.038728713989257813 ms (0.0151 seconds) respectively.

The time to generate a single match and save it to the test computer with 12 projections for dataset index 1, 50, and 100 were 244.56787109375 ms (0.2446 seconds), 218.28866004943847656 ms (0.2183 seconds), and 216.907501220703125 ms (0.2169 seconds) respectively.

---
## Concluding Remarks
Overall, the program operates successfully. It runs with a hit accuracy of 73% and runs almost equally as well with the addition of newly created images. The program runs in O(n) time to find a match for a single image in the database, and runs in O(n2) to find matches for all of the images in the database.

Searching using the original images, un-cropped, using the 4 recommended projections 0, 45, 90, 135 degrees resulted in a hit ratio of 51%. Uncropped images with 12 projections had a hit ratio of 64% (from Table 2).

Cropping the image to only use rows and columns 4 to 22 to eliminate the empty space that made a border around the images, and increasing the projections to 12 allowed for the hit ratio of the program to increase 22%.

Cropping played the most significant role in improving the hit ratio, as it led to an increase of 17% (51% to 68%) with 4 projections contrasted to the 13% hit ratio increase seen by increasing the projections.

Voting was initially introduced to help further increase the hit accuracy, but this was removed as the hamming distances across the numerous different results varied greatly, and often the closest match was the number returned even if it did not correspond to the digit’s label. The varying hamming distances resulted in voting not yielding enough accurate contenders without introducing even more contenders that were incorrect matches, leading to more overall incorrect matches as a whole.

Introducing new hand drawn images into the data set yielded similar results. After the inclusion of 10 new zeroes (drawn on paper, scanned, then colour inverted), the hit accuracy only decreased to 72%, as 8 out of 10 zeroes were matched correctly. See Appendix A for the images introduced and their matches.

One key factor which may have contributed to a reduced hit ratio is the format in which the images were provided. As they are jpeg images, their compression leads to discoloured pixels surrounding the main image, called artifacts. Using an alternative file format, such as gzip (the format of the original dataset), or png could have eliminated the possibility of “false positives” in the radon techniques used to generate the barcode from the projections. Alternatively, some preimage processing could have been done to reduce the noise in the images and filter out these artifacts before attempting to take projections.

To further improve the program, one might consider adding even more projections. While this slows down the overall speed at which it runs due to each barcode increasing by 18 digits for every projection. Currently, each barcode is 216 digits long. When each image was processed using only 4 projections, the accuracy is 68% with barcodes that are 72 digits long.

12 projections were decided upon as it most thoroughly covered the image, and yielded a reasonable increase in accuracy with a relatively small increase in running time as seen in the running time analysis section above and Table 2. While tripling the projections did lead to an  increase in running time by a factor of 3, the increase in accuracy is valuable enough to warrant it for a dataset of this size. It is for this reason that 12 projections were utilized. If the dataset were to increase in size significantly the programmer may decide that the trade off is not worth it. 

