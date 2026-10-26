# SignSpeak Technical Design Document

## 1. System Overview
SignSpeak is a prototype that uses a camera and hand-landmark detection to demonstrate basic hand gesture recognition.

## 2. System Architecture
Camera Input → Image Processing → Hand Landmark Detection → Finger Counting → Text Display

## 3. Technologies Used
- Python
- OpenCV: camera capture and image processing
- MediaPipe: hand landmark detection

## 4. Processing Flow
1. Capture frames from the webcam.
2. Flip the frame for a mirror-like view.
3. Convert the frame to RGB.
4. Detect hand landmarks using MediaPipe.
5. Estimate extended fingers using landmark positions.
6. Display a basic label on the video frame.

## 5. Inputs and Outputs
Input: Live webcam frames.
Output: Hand landmarks and simple finger-count labels.

## 6. Current Limitations
The current prototype is not a complete sign-language translator. It uses simple finger counting and does not interpret full signs, sentences, facial expressions, or sign-language grammar. Thumb detection and finger counting may be inaccurate for some hand orientations.

## 7. Future Improvements
- Add a trained model for a defined set of signs.
- Collect and evaluate suitable sample data.
- Measure recognition accuracy.
- Explore text-to-speech output.
- Evaluate possible embedded-device integration.

## 8. Testing Plan
Test with no hand visible, an open hand, a fist, different lighting conditions, and different camera angles. Record actual results after running the program.

## 9. Privacy
Obtain consent before recording or collecting images. Avoid storing identifiable video unless necessary and authorized.
