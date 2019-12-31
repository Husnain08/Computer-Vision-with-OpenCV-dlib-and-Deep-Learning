import PIL.Image
import PIL.ImageDraw
import face_recognition
import os
dir = os.listdir()
from PIL import Image
print (dir)
file = [f for f in dir if f.endswith('jpg')]
for i , f_ in enumerate(file):
    image = face_recognition.load_image_file(f_) # loads the images and converts in into an array where each value corresponds to a pixel
    face_locations = face_recognition.face_locations(image) #Use a pre-trained HOG Classifier
    total_pictures = len(image)

    total_faces = len(face_locations)
    print ("{} faces were found in the {}  picture".format(total_faces , i+1))
    print("The coordinates of the face are {}".format(face_locations))
    pil_image = Image.fromarray(image)
    for face_location in face_locations:
        top , right , bottom , left = face_location
        print("A face is located on these pixels\n Top: {}\n Left: {}\n Bottom: {}\n Right: {}".format(top,right,bottom,left))
        draw = PIL.ImageDraw.Draw(pil_image)
        draw.rectangle([left , top ,right, bottom] , outline="red")
        pil_image.show()
# Converting our image to a PIL Formatted image so that we can draw bounding boxes on them
#from PIL import  Image
#il_image = Image.fromarray(file)
