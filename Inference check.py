import cv2
import numpy as np
import tensorflow as tf
import time

tflite_model_path = "model.tflite"
interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

cap = cv2.VideoCapture("squat.mp4")
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
inf_time = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    input_size = input_details[0]['shape'][1:3]
    resized_frame = cv2.resize(frame, (input_size[1], input_size[0]))
    input_data = np.expand_dims(resized_frame, axis=0).astype(np.float32) / 255.0

    start_time = time.time()
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    inference_time = (time.time() - start_time) * 1000  # in milliseconds

    output_data = interpreter.get_tensor(output_details[0]['index'])

    print(f"Inference Time: {inference_time:.2f} ms")
    inf_time.append(inference_time)

    cv2.imshow("Pose Detection", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

with open("inference_time.txt", "w") as file:
    file.write("\n".join([f"{time:.2f}" for time in inf_time]))
