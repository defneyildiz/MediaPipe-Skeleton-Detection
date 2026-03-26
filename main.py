import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # Camera number (0 for the default camera)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Mirror the image horizontally
    frame = cv2.flip(frame, 1)
    
    # Display the image
    cv2.imshow("YAPTIM", frame)

    # Exit the program when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""
import cv2
import mediapipe as mp

# MediaPipe araçlarını hazırla
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Kamerayı başlat (Varsayılan kamera 0'dır)
cap = cv2.VideoCapture(0)

print("Kamera açılıyor... Kapatmak için klavyeden 'q' tuşuna bas!")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Kamera görüntüsü alınamadı.")
        break

    # Görüntüyü işle
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    # İskelet çizgilerini çiz
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Pencereyi göster
    cv2.imshow('HCI Lab - Skeleton Test', image)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""