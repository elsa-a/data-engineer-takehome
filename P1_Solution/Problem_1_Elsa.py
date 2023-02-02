import os
import cv2

# print cwd for reference
print(f"\nHi, this is a face detector script. \n\nCurrent directory is: {os.getcwd()}\nYou may use the example image file contained in this directory: IMG_9721.jpg.")

# take user input for path to image file
file_path = input(
    '\nPlease enter the path to the example image file or any other:\n')
print(f"\file path: '{file_path}'")

try:
    # reads image using opencv
    img = cv2.imread(file_path)
    # instanciate cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # cnvert color image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect faces in image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.07,
        minNeighbors=4,
        minSize=(200, 200))
    # parameter 1: Matrix containing image where face is detected.
    # scaleFactor: how much the image size is reduced at each image scale.
    # nimNeighbors: how many neighbors each rectangle should have to retain it
    # minSize: Minimum possible object size

# catch cv2 errors if imread, color conversion or face detection fail.
except cv2.error as e:
    print("Sorry. Something went wrong.")

# if image is processed correctly
else:
    # check if faces were detected
    if len(faces) == 0:
        print("\nNo faces were detected.")

    # if detected, ask for directory, crop faces and save into directory
    else:
        # take user input for output directory
        out_path = input('\nEnter a directory path to save the images to: ')

        # crop and save files
        files = []
        for i, (x, y, w, h) in enumerate(faces):

            p = 20  # padding
            # crop
            cropped_image = img[y - p + 1:y + h + p, x - p + 1:x + w + p]
            file_name = (f'face_{str(i + 1)}.jpg')
            files.append(os.path.join(out_path, file_name))

            # write cropped image into directory
            try:
                cv2.imwrite(os.path.join(out_path, file_name), cropped_image)
            except:
                print("Sorry, something happened.")

        print(f"\nhi, number of faces detected: {len(faces)}.")
        print(f"\nCropped headshots saved to:")
        print("\n".join(files))
