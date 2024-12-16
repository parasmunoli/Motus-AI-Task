



while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from webcam.")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        x_min = min([landmark.x for landmark in landmarks]) * frame.shape[1] - 40
        x_max = max([landmark.x for landmark in landmarks]) * frame.shape[1] + 40
        y_min = min([landmark.y for landmark in landmarks]) * frame.shape[0] - 50
        y_max = max([landmark.y for landmark in landmarks]) * frame.shape[0] + 30

        # Draw the bounding box around the detected human
        cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)

    # Display the video feed with pose landmarks and bounding box
    cv2.imshow("Real-Time Human Movement Tracker", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


