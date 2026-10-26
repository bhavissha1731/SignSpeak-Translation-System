# SignSpeak Sample Test Cases

## Purpose
These test cases are designed to evaluate the initial hand-detection and finger-counting prototype.

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC01 | Start the program with a working webcam | Camera feed opens |
| TC02 | Show an open hand | Hand landmarks appear and the program attempts to count extended fingers |
| TC03 | Show a closed fist | Hand landmarks appear and the program may display "Fist detected" |
| TC04 | Keep hands outside the camera view | Message asks the user to show a hand |
| TC05 | Camera is unavailable | Error message is displayed |
| TC06 | Test under different lighting | Observe and record detection changes |

## Result Recording
Record the actual result for each test after running the program. Do not mark a test as passed until it has been performed.

## Limitations
Finger counting is a basic demonstration and may be inaccurate for some hand positions. These tests do not establish full sign-language translation accuracy.
