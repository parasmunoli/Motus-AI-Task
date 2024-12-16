#Import required files
import cv2
import mediapipe as mp
import math

#Initializing MediaPipe Pose
pose_init = mp.solutions.pose
pose = pose_init.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

#Calculate squat angle
def calculate_angle(a, b, c):
    #Formula for calculating angle between 3 points i.e. a,b,c (a = Hip, b = Knee, c = Ankle)
    ab = [b[0] - a[0], b[1] - a[1]]
    bc = [c[0] - b[0], c[1] - b[1]]
    dot_product = ab[0] * bc[0] + ab[1] * bc[1]
    magnitude_ab = math.sqrt(ab[0] ** 2 + ab[1] ** 2)
    magnitude_bc = math.sqrt(bc[0] ** 2 + bc[1] ** 2)
    if magnitude_ab == 0 or magnitude_bc == 0:
        return 0
    angle = math.acos(dot_product / (magnitude_ab * magnitude_bc))
    return math.degrees(angle)

#Open video file
cap = cv2.VideoCapture("squat.mp4")
angles = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    #Convert video frame into RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    if results.pose_landmarks:
        # Draw pose landmarks
        mp.solutions.drawing_utils.draw_landmarks(
            frame, results.pose_landmarks, pose_init.POSE_CONNECTIONS)

        landmarks = results.pose_landmarks.landmark
        frame_height, frame_width, _ = frame.shape

        # Extract and scale landmark coordinates
        hip = [landmarks[pose_init.PoseLandmark.RIGHT_HIP.value].x * frame_width,
               landmarks[pose_init.PoseLandmark.RIGHT_HIP.value].y * frame_height]
        knee = [landmarks[pose_init.PoseLandmark.RIGHT_KNEE.value].x * frame_width,
                landmarks[pose_init.PoseLandmark.RIGHT_KNEE.value].y * frame_height]
        ankle = [landmarks[pose_init.PoseLandmark.RIGHT_ANKLE.value].x * frame_width,
                 landmarks[pose_init.PoseLandmark.RIGHT_ANKLE.value].y * frame_height]

        # Calculate Squat angle
        angle = calculate_angle(hip, knee, ankle)
        angles.append(angle)

        #Display angle in output frame
        cv2.putText(frame, f"Knee Angle: {int(angle)}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

    # Display the video
    cv2.imshow('Pose Detection', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#Save angle continuously in txt file
with open("angles.txt", "w") as file:
    file.write("\n".join(map(str, angles)))
