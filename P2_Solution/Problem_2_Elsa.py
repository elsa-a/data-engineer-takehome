from keys import access_key, secret_access_key

from PIL import Image
from io import BytesIO
import boto3

"""
function retrieves all objects in source bucket, checks if files are valid images
and if images are transparent, finally copies them separately based on the later.
"""


def main():
    # instanciate boto s3 client
    s3_client = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_access_key)
    # take user input for path to image file
    source_bucket = input(
        '\nHi, this is an image copying script. \nPlease enter a AWS S3 bucket name to read the images from.\n')
    destination_bucket = input(
        '\nPlease enter the name of a different S3 bucket as destination for the image files.".\n')

    # gets ojects in source bucket
    bucket_listing = s3_client.list_objects_v2(
        Bucket=source_bucket)

    # List images in source directory
    for object in bucket_listing['Contents']:

        # opening files with PIL
        try:
            imagefile = object['Key']
            # retrieve file from bucket and read into memory using io module
            new_obj = s3_client.get_object(Bucket=source_bucket, Key=imagefile)
            image_dl = new_obj['Body'].read()
            im = Image.open(BytesIO(image_dl))
            print()

        # catch Pillow errors if filename not an image file
        except IOError:
            print()
            print(f"File {object['Key']} is not a valid image file.")

        # catch all other errors
        except Exception as e:
            print()
            print(f"Sorry, something went wrong. \n\nERROR: {e}")

        else:
            # checks transparency using function
            transparency = check_transparency(im)
            if transparency == True:
                print(f"File {object['Key']} -> contains transparent pixels.")

                # log to separate file
                # (Leave blank if root level, include slash at end if Prefix specified)
                source_prefix = ''
                folder_to_copy = ''
                destination_prefix = 'transparent/'
                print(
                    f'Copying to {destination_prefix + object["Key"][len(source_prefix):]}')
                s3_client.copy_object(
                    CopySource={'Bucket': source_bucket, 'Key': object['Key']},
                    Bucket=destination_bucket,
                    # Remove source prefix, add destination prefix
                    Key=destination_prefix + object['Key'][len(source_prefix):]
                )
            else:

                # (Leave blank if root level, include slash at end if Prefix specified)
                source_prefix = ''
                folder_to_copy = ''
                destination_prefix = ''

                print(
                    f"File {object['Key']} -> does not contain transaprent pixels.")
                print(
                    f'Copying to {destination_prefix + object["Key"][len(source_prefix):]}')
                s3_client.copy_object(
                    CopySource={'Bucket': source_bucket, 'Key': object['Key']},
                    Bucket=destination_bucket,
                    # Remove source prefix, add destination prefix
                    Key=destination_prefix + object['Key'][len(source_prefix):]
                )


"""
function below takes in a PIL image and checks diferent properties
which are likely to mean the image has transparent pixels
"""


def check_transparency(img):
    # check if "transparency" property is defined in image
    if img.info.get("transparency", None) is not None:
        return True
    # check if image is using indexed colors (such as in GIFs) and gets index of the transparent color
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        print(img.info)
        # check if transaprent pixels in the canvas
        for _, index in img.getcolors():
            if index == transparent:
                return True
    # if image is in RGBA mode, double check by getting min and max values of color channels
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True
    # if none true, then image has no transparent pixels
    return False


""" transparency function source:
https://stackoverflow.com/questions/43864101/python-pil-check-if-image-is-transparent
"""

if __name__ == '__main__':
    main()
