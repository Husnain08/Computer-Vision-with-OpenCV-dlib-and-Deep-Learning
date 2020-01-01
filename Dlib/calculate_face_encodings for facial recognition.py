import face_recognition
image = face_recognition.load_image_file('person.jpg')
# Calculate face encodings for all faces found in the image
face_encodings = face_recognition.face_encodings(image)
print("{} faces found in the picture".format(len(face_encodings)))
if len(face_encodings) ==0: # If there are no faces in the faces
    print("No faces were found")
else:
    first_face = face_encodings[0]
    print("The first image has encodings {}".format(first_face))
