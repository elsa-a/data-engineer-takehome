# Solutions to the takehome test by Elsa

Please note that solution to problem 2 requires the file "keys.py" to be modified with valid credentials in order for the main script to run correctly.

To do so, please open **keys.py** and provide said key and secret key to execute the script.
___

### 💠 Folder 1: **P1 Solution**
____
Contains:

▪️ **haarcascade_frontalface_default.xml**   -> the cascade filter .xml

▪️ **IMG_9721.jpg** example image with multiple faces

▪️ **Problem_1_Elsa.py**       -> solution script

▪️ **results** -> folder containg cropped headshots

___
### 💠 Folder 2: **P2 Solution**
____
Contains:

▪️ **Problem_2_Elsa.py**       -> solution script

▪️ **keys.py** -> file imported by the main script with the keys to access s3.


___

Original description:

### Data Engineer Takehome Test
Please clone this repo in your account, send us the link of the solution in your GitHub account together with your application.

##### Problem 1:
Build a Python script that detects faces in an image using OpenCV, and saves the headshots of the detected faces to a specified directory. The script should take as input a file path to an image, a directory path to save the headshots, and output the number of faces detected in the image.
Instructions:
- Use OpenCV's Haar Cascade classifier for face detection
- The script should be written in Python and use the following libraries: OpenCV, Numpy, and PIL (Python Imaging Library)
- The script should be well commented and easy to understand
- The script should be able to handle a variety of image types (e.g. jpeg, png, etc.)
- The script should be able to handle images with multiple faces
- The script should save the headshots in the specified directory with the file name in the format "face_1.jpg", "face_2.jpg", etc.


##### Problem 2: 
Move all image files from one S3 bucket to another S3 bucket, but only if the image has no transparent pixels.

Objective: Write a Python script that uses the Boto3 library to accomplish the following:

- List all the image files in a given S3 bucket
- Check if each image file has transparent pixels
- If an image file has no transparent pixels, copy it to a different S3 bucket
- If an image file has transparent pixels, log it in a separate file

Guidelines:
- Your script should take the name of the source and destination buckets as input
- You should use the Boto3 library to interact with S3
- You should use the Pillow library to check for transparent pixels in an image
- Your script should handle any errors that may occur during the opening of image file, copy process and anywhere else you deem necessary
- Your script should be well commented and easy to understand
- Your script should be executed from the command line
