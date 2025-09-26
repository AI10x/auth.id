from insightface.app import FaceAnalysis
import face_recognition
import cv2
import os
import random

import numpy as np
import sys

#add to /lib/security


def embeddings(image):
    app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    image1 = cv2.imread(image)
    faces = app.get(image1)

    faceid_embeds = (faces[0].normed_embedding)
    return(faceid_embeds)

def face_verify(facex1, facex2):
    facex1 = embeddings(facex1)
    known_face_encoding = embeddings(facex2)

    matches = face_recognition.compare_faces([known_face_encoding], facex1, tolerance=0.75)
    
    if bool(matches[0]) == True: 
       print('TRUE')




print(face_verify('/home/emmanuel/genai/capture.jpg', '/home/emmanuel/genai/capture1.jpg'))
