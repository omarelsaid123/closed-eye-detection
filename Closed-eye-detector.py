import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
previous_status = None

def get_distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    distance = (dx**2 + dy**2) ** 0.5
    return distance

def set_status(right_eye_distance, left_eye_distance):
    if right_eye_distance < 0.015 and left_eye_distance < 0.015: #alter this value if needed
        return True
    else:
        return False

cv2.namedWindow("Eye Detection", cv2.WINDOW_NORMAL)

with open('eye_log.txt', 'w') as f: #clear file
    f.write('')

with open('eye_log.txt', 'a') as f:
    while True:
        ret, frame = cap.read()
        

        height, width = frame.shape[:2] #grabs first 2 values form frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Right eye
                top_right = face_landmarks.landmark[159]
                bottom_right = face_landmarks.landmark[145]
                right_eye_distance = get_distance(top_right, bottom_right)

                # Left eye
                top_left = face_landmarks.landmark[386]
                bottom_left = face_landmarks.landmark[374]
                left_eye_distance = get_distance(top_left, bottom_left)

                # Draw landmarks as circles
                for i in (top_right, top_left, bottom_right, bottom_left):
                    x = int(i.x * width)
                    y = int(i.y * height)
                    cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
                

                current_status = set_status(right_eye_distance, left_eye_distance)

                if current_status != previous_status:
                    if current_status:
                        f.write("Eyes CLOSED\n")
                        print("Eyes CLOSED")
                    else:
                        f.write("Eyes OPEN\n")
                        print("Eyes OPEN")
                    
                    previous_status = current_status

        cv2.imshow("Eye Detection", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
