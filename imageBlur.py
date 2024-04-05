import cv2

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Apply blur to each detected face
    for (x, y, w, h) in faces:
        # Apply Gaussian blur to the face region
        blurred_face = cv2.GaussianBlur(frame[y:y+h, x:x+w], (99, 99), 0)

        # Replace the face region with the blurred face
        frame[y:y+h, x:x+w] = blurred_face

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()