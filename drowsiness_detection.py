
import cv2
import mediapipe as mp
import numpy as np

EAR_THRESH = 0.25
CONSEC_FRAMES = 20
MAR_THRESH = 0.7

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [13, 14, 78, 308]

def eye_aspect_ratio(landmarks, eye_indices):
    eye = [landmarks[i] for i in eye_indices]
    A = np.linalg.norm(np.array(eye[1]) - np.array(eye[5]))
    B = np.linalg.norm(np.array(eye[2]) - np.array(eye[4]))
    C = np.linalg.norm(np.array(eye[0]) - np.array(eye[3]))
    return (A + B) / (2.0 * C)

def mouth_aspect_ratio(landmarks, mouth_indices):
    top_lip = landmarks[mouth_indices[0]]
    bottom_lip = landmarks[mouth_indices[1]]
    left = landmarks[mouth_indices[2]]
    right = landmarks[mouth_indices[3]]
    vertical = np.linalg.norm(np.array(top_lip) - np.array(bottom_lip))
    horizontal = np.linalg.norm(np.array(left) - np.array(right))
    return vertical / horizontal

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

counter = 0
yawn_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0]
        coords = [(int(p.x * w), int(p.y * h)) for p in landmarks.landmark]

        left_ear = eye_aspect_ratio(coords, LEFT_EYE)
        right_ear = eye_aspect_ratio(coords, RIGHT_EYE)
        avg_ear = (left_ear + right_ear) / 2.0

        mar = mouth_aspect_ratio(coords, MOUTH)

        if avg_ear < EAR_THRESH:
            counter += 1
            if counter >= CONSEC_FRAMES:
                cv2.putText(frame, "DROWSY!", (30, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
        else:
            counter = 0

        if mar > MAR_THRESH:
            yawn_counter += 1
            if yawn_counter >= 10:
                cv2.putText(frame, "YAWNING!", (30, 140),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
        else:
            yawn_counter = 0

        cv2.putText(frame, f"EAR: {avg_ear:.2f}", (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        cv2.putText(frame, f"MAR: {mar:.2f}", (30, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)

    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
