import mediapipe as mp
import cv2
import numpy as np
import pyautogui

class HandMouseController:
    """
        Lớp khởi tạo và chạy game

        tham số cần thiết:
        - camera_width VD: camera_width=1920 (int)
        - camera_height VD: camera_height=1080 (int)
        - min_detection_confidence VD: min_detection_confidence=0.8 (float)
        - min_tracking_confidence VD: min_tracking_confidence=0.5 (float)
    """
    def __init__(self, screen_width=1920, screen_height=1080, min_detection_confidence=0.8, min_tracking_confidence=0.5):
        # Kích thước của cửa sổ camera
        self.camera_width = screen_width
        self.camera_height = screen_height
        
        # Kích thước của cửa sổ game, gấp 3 lần kích thước camera theo tỷ lệ 3:1
        self.game_window_width = screen_width * 3
        self.game_window_height = screen_height * 3

        # Vị trí của cửa sổ game
        self.game_window_left = 0
        self.game_window_top = 0

        self.cap = cv2.VideoCapture(0)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=min_detection_confidence, min_tracking_confidence=min_tracking_confidence)

    def convert_to_screen_coordinates(self, x, y, frame_width, frame_height):
        # Tính toán tọa độ chuột tương đối với cửa sổ game
        screen_x = self.game_window_left + int(self.game_window_width * x / frame_width)
        screen_y = self.game_window_top + int(self.game_window_height * y / frame_height)
        
        # Đảm bảo tọa độ chuột nằm trong giới hạn của cửa sổ game
        screen_x = max(self.game_window_left, min(screen_x, self.game_window_left + self.game_window_width - 1))
        screen_y = max(self.game_window_top, min(screen_y, self.game_window_top + self.game_window_height - 1))
        
        return screen_x, screen_y

    def is_hand_closed(self, hand_landmarks):
        # Tính khoảng cách giữa ngón giữa(12) và vị trí cuối của ngón giữa(9)
        middle_finger_tip = hand_landmarks.landmark[12]
        end_middle_finger = hand_landmarks.landmark[9]
        distance = np.linalg.norm(np.array([middle_finger_tip.x - end_middle_finger.x, middle_finger_tip.y - end_middle_finger.y]))
        return distance < 0.05

    def run(self):
        pyautogui.FAILSAFE = False
        cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Hand Tracking", self.camera_width, self.camera_height)

        with self.hands:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                
                if not ret:
                    continue
                
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = cv2.flip(image, 1)
                image.flags.writeable = False
                
                results = self.hands.process(image)
                
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                # frame_height, frame_width, _ = image.shape
                # top_left = ((frame_width - self.camera_width) // 2, (frame_height - self.camera_height) // 2)
                # bottom_right = (top_left[0] + self.camera_width, top_left[1] + self.camera_height)
                # cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)

                if results.multi_hand_landmarks:
                    for hand in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(image, hand, self.mp_hands.HAND_CONNECTIONS,
                                                       self.mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                                       self.mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2))
                        wrist_x = hand.landmark[0].x
                        wrist_y = hand.landmark[0].y
                        
                        # Tính toán tọa độ chuột từ điểm wrist
                        screen_x, screen_y = self.convert_to_screen_coordinates(wrist_x * frame.shape[1], wrist_y * frame.shape[0], frame.shape[1], frame.shape[0])
                        
                        pyautogui.moveTo(screen_x, screen_y)
                        
                        if self.is_hand_closed(hand):
                            pyautogui.mouseDown()
                        else:
                            pyautogui.mouseUp()
                
                cv2.imshow('Hand Tracking', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        self.cap.release()
        cv2.destroyAllWindows()
