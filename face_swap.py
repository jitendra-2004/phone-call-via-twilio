import cv2
import mediapipe as mp
import numpy as np

class FaceSwapper:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(max_num_faces=2)

    def get_face_bbox(self, landmarks, shape):
        x_list = [int(p.x * shape[1]) for p in landmarks]
        y_list = [int(p.y * shape[0]) for p in landmarks]
        return min(x_list), min(y_list), max(x_list) - min(x_list), max(y_list) - min(y_list)

    def swap_faces(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if results.multi_face_landmarks and len(results.multi_face_landmarks) == 2:
            lm1 = results.multi_face_landmarks[0].landmark
            lm2 = results.multi_face_landmarks[1].landmark

            x1, y1, w1, h1 = self.get_face_bbox(lm1, frame.shape)
            x2, y2, w2, h2 = self.get_face_bbox(lm2, frame.shape)

            face1 = frame[y1:y1+h1, x1:x1+w1].copy()
            face2 = frame[y2:y2+h2, x2:x2+w2].copy()

            try:
                face1 = cv2.resize(face1, (w2, h2))
                face2 = cv2.resize(face2, (w1, h1))

                frame[y1:y1+h1, x1:x1+w1] = face2
                frame[y2:y2+h2, x2:x2+w2] = face1
            except:
                pass

        return frame

def main():
    swapper = FaceSwapper()
    cap = cv2.VideoCapture(0)
    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        swapped = swapper.swap_faces(frame)
        cv2.imshow("Face Swapper", swapped)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()