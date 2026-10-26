
"""
SignSpeak Translation System
Starter prototype: webcam hand detection and finger counting.

This is a demonstration prototype, not a complete sign-language
translation model.
"""

import cv2
import mediapipe as mp

def main():
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open the camera.")
        return

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6
    ) as hands:

        while True:
            success, frame = camera.read()

            if not success:
                print("Could not read camera frame.")
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            message = "Show your hand to the camera"

            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(
                        frame,
                        hand,
                        mp_hands.HAND_CONNECTIONS
                    )

                    points = hand.landmark

                    # Count four extended fingers.
                    fingers = 0
                    for tip in [8, 12, 16, 20]:
                        if points[tip].y < points[tip - 2].y:
                            fingers += 1

                    # Simple demonstration labels only.
                    if fingers == 0:
                        message = "Fist detected"
                    elif fingers == 4:
                        message = "Open hand detected"
                    else:
                        message = f"{fingers} fingers extended"

            cv2.putText(
                frame, message, (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 255, 0), 2
            )

            cv2.imshow("SignSpeak Prototype", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
  
