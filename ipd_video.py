import cv2
import numpy as np
import dlib
import cv2.aruco as aruco

from aruco_utils import calculate_pixel_mm_ratio_video
from utils import midpoint


# Loading detector and predictor
detector = dlib.get_frontal_face_detector()
predectior = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def live_video_analysis(marker_size_mm,aruco_dict_type):
    cap = cv2.VideoCapture(0)
    
    # Live Video
    while True:
        ret, frame = cap.read()
        if not ret : 
            break

        # Converting frame to grey scale
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

        
        px_mm_ratio = calculate_pixel_mm_ratio_video(frame, marker_size_mm, aruco_dict_type)
            
        # Detecting faces --> returns a list of rectangles(faces)
        faces = detector(grey) 
        for face in faces: 
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x,y), (x1,y1), (0,255,0), 2)

            # Detecting landmarks --> returns a list of 68 points

            landmarks = predectior(grey, face)  # left eye is 36 to 41 and right eye is 42 to 47
            
            left_point = (landmarks.part(36).x, landmarks.part(36).y)
            right_point = (landmarks.part(39).x, landmarks.part(39).y)
            center_top = midpoint(landmarks.part(37), landmarks.part(38))
            center_bottom = midpoint(landmarks.part(41), landmarks.part(40))


            # pupil detection -- pupil is located between the center of these points
            pupil_left = midpoint(landmarks.part(36), landmarks.part(39))   # left eye
            pupil_right = midpoint(landmarks.part(42), landmarks.part(45))  # right eye
            cv2.circle(frame, pupil_left, 1, (0, 0, 255), 1)
            cv2.circle(frame, pupil_right, 1, (0, 0, 255), 1)

            cv2.line(frame,pupil_left,pupil_right,(0,255,0),2)

            # Calculating the distance of this line that is the distance between the two pupils
            pixel_distance = np.linalg.norm(np.array(pupil_left)-np.array(pupil_right)) 
            '''
            This distance is in pixels so we need to convert it into millimetres
            we can use a reference object to convert pixels into mm
            reference object is an object whose dimensions are known
            For this purpose we are using aruco marker that the user will download from our website/app 
            and then place it on his/her forehead during the image capture
            '''
            # converting to mm
            if (px_mm_ratio != 0.0 ):
                distance = round((pixel_distance / px_mm_ratio),1)
                print(distance) 
            else:
                print(f"Aruco Marker isnot detected IPD in pixels is: {pixel_distance} ")

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



