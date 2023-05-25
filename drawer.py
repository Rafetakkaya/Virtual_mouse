import cv2
import mediapipe
import pyautogui
import numpy as np

# Global variables to track previous mouse coordinates
prev_x = 0
prev_y = 0

# Create a canvas image for drawing lines
canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

def mouse():
    capture_hands = mediapipe.solutions.hands.Hands()
    drawing_option = mediapipe.solutions.drawing_utils

    screen_width, screen_height = pyautogui.size()
    camera = cv2.VideoCapture(0)

    while True:
        _, image = camera.read()
        image_height, image_width, _ = image.shape
        image = cv2.flip(image, 1)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        output_hands = capture_hands.process(rgb_image)
        all_hands = output_hands.multi_hand_landmarks

        if all_hands:
            for hand in all_hands:
                drawing_option.draw_landmarks(image, hand)
                one_hand_landmarks = hand.landmark

                for id, lm in enumerate(one_hand_landmarks):
                    x = int(lm.x * image_width)
                    y = int(lm.y * image_height)

                    if id == 5:
                        cv2.circle(image, (x, y), 10, (0, 255, 255))
                        mouse_x = int(screen_width / image_width * x)
                        mouse_y = int(screen_height / image_height * y)

                        # Draw line on the canvas
                        global prev_x, prev_y
                        if prev_x != 0 and prev_y != 0:
                            cv2.line(canvas, (prev_x, prev_y), (mouse_x, mouse_y), (0, 0, 255), 5)

                        prev_x = mouse_x
                        prev_y = mouse_y

                        pyautogui.moveTo(mouse_x, mouse_y)

        # Overlay the canvas on top of the camera feed
        overlay = cv2.addWeighted(image, 1, canvas, 0.5, 0)

        cv2.imshow("Hand Movement Video Capture", overlay)

        key = cv2.waitKey(1)
        if key == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

# Run the mouse function
mouse()
