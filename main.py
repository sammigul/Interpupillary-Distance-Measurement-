import cv2
import numpy as np
# dlib is a library for face detection and face landmark detection(68 points on face)
import dlib

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predectior = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Helper Method to calculate midpoit between two coordinates
def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

# Reading image
image_path = "test3.jpeg"

# For Image 
def imageAnalysis(image_path):
    image = cv2.imread(image_path)
    grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = detector(grey_image)
    for face in faces: 
        # x, y = face.left(), face.top()
        # x1, y1 = face.right(), face.bottom()
        # cv2.rectangle(image, (x,y), (x1,y1), (0,255,0), 2)

        # Detecting landmarks --> returns a list of 68 points

        landmarks = predectior(grey_image, face)  # left eye is 36 to 41 and right eye is 42 to 47
        

        # pupil detection -- pupil is located between the center of these points
        pupil_left = midpoint(landmarks.part(36), landmarks.part(39))   # left eye
        pupil_right = midpoint(landmarks.part(42), landmarks.part(45))  # right eye
        cv2.circle(image, pupil_left, 1, (0, 0, 255), 1)
        cv2.circle(image, pupil_right, 1, (0, 0, 255), 1)

        cv2.line(image,pupil_left,pupil_right,(0,255,0),2)
        # Calculating the distance of this line that is the distance between the two pupils
        distance = np.linalg.norm(np.array(pupil_left)-np.array(pupil_right)) 
        print(f"Left Pupil: {pupil_left} Right Pupil: {pupil_right} Distance: {distance}")

        '''
        This distance is in pixels so we need to convert it into centimeters
        we can use a reference object to convert pixels into centimeters
        reference object is an object whose dimensions are known
        we can use a credit card as a reference object
        credit card size is 85.60 X 53.98 mm
        '''

    cv2.imshow('Image', image)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


def live_video_analysis():
    # Live Video
    while True:
        ret, frame = cap.read()
        # Converting frame to grey scale
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

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
            cv2.line(frame,center_top,center_bottom,(0,255,0),2)

            # Calculating the distance of this line that is the distance between the two pupils
            distance = np.linalg.norm(np.array(pupil_left)-np.array(pupil_right)) 
            print(f"Left Pupil: {pupil_left} Right Pupil: {pupil_right} Distance: {distance}")

            '''
            This distance is in pixels so we need to convert it into centimeters
            we can use a reference object to convert pixels into centimeters
            reference object is an object whose dimensions are known
            we can use a credit card as a reference object
            credit card size is 85.60 X 53.98 mm
            '''
            # Drawing lines
            # hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
            # ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



'''
Using template matching to match the credit card in the image

'''
import cv2

def template_matching():
    img = cv2.resize(cv2.imread('test2.jpeg', 0), (0, 0), fx=0.8, fy=0.8)
    template = cv2.imread('template3.png', 0)
    
    # Preprocess the template by applying guassian blur
    # template = cv2.GaussianBlur(template, (5, 5), 0)
    
    h, w = template.shape
    
    # Choose 
    method = cv2.TM_CCORR_NORMED
    
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # threshold for matching
    threshold = 0.8
    
    if max_val > threshold:
        location = max_loc
        bottom_right = (location[0] + w, location[1] + h)
        cv2.line(img2, location, bottom_right, 255, 5)
        # cv2.rectangle(img2, location, bottom_right, 255, 5)
        cv2.imshow('Match', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Template not found")

template_matching()

# For Live Video 
# live_video_analysis()

# Calling Image Analysis Funct here 
# imageAnalysis(image_path)
