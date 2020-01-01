import PIL.Image
import PIL.ImageDraw
import face_recognition
import os
image = [image for image in os.listdir() if image.endswith('jpg') or image.endswith('jfif')]
for i , image in enumerate(image):
    picture = face_recognition.load_image_file(image)
    face_landmarks = face_recognition.face_landmarks(picture) # find face landmarks
    print("{} faces found in image number {}".format(len(face_landmarks) , i+1))
    pil_image = PIL.Image.fromarray(picture) # convert Image into the PIL Format
    draw = PIL.ImageDraw.Draw(pil_image)
    for face_landmarks in face_landmarks:
        for  face , list_of_points in (face_landmarks.items()):
            print(" {} on the face {} has the following landmark points {}".format(face,i+1, list_of_points))
            draw.line(list_of_points , fill= 'green' , width= 2)
pil_image.show()
