import face_recognition
import os
pictures = [f for f in os.listdir() if f.endswith('jpg')]
# Load all the images of those people who are known to us and calculate their face encodings

image_known_1 = face_recognition.load_image_file('person_1.jpg')
image_known_2 =face_recognition.load_image_file('person_2.jpg')
image_known_3 =face_recognition.load_image_file('person_3.jpg')

encoding_person_1 = face_recognition.face_encodings(image_known_1)[0]
encoding_person_2 = face_recognition.face_encodings(image_known_2)[0]
encoding_person_3 = face_recognition.face_encodings(image_known_3)[0]

known_encodings = [encoding_person_1,encoding_person_2,encoding_person_3]


# Now load the images we want to check and calculate their encodings.

unknown_person = face_recognition.load_image_file('unknown_7.jpg')
known_face_location = face_recognition.face_locations(unknown_person , number_of_times_to_upsample=2) # Enlarge the image to better detect faces

unknown_encoding = face_recognition.face_encodings(unknown_person , known_face_locations=known_face_location)
# call the compare_face function of the face_recognition library

for face_encodings in unknown_encoding:
    results = face_recognition.compare_faces(known_encodings , face_encodings) # only has True or False values based on the known encodings
    if results[0].all():
        print("Person 1 is detected")
    elif results[1].all():
        print("Person 2 is detected")
    elif results[2].all():
        print ("Person 3 is detected")
    else:
        print ("Unknown Person")






