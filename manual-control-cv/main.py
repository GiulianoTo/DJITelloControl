# manual-control-cv

from djitellopy import Tello
import cv2, math, time

fly = False

tello = Tello()
tello.connect()
tello.streamon()
frame_read = tello.get_frame_read()

print(f"Battery Life Pecentage: {tello.get_battery()}")

if fly:
    try:
        tello.takeoff()
        print("Takeoff successful")
        time.sleep(3)

    except Exception as e:
        print(f"Error during takeoff: {e}")

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    # they will freeze while the drone moves.
    img = frame_read.frame

    # Converti il frame al formato corretto BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)
    elif key == ord('t'):
        # Only for test purpose...
        tello.send_rc_control(0, 10, 0, 0)
        time.sleep(5)
        tello.send_rc_control(0, 0, 0, 0)


tello.streamoff()

if fly:
    try:
        tello.land()
        print("Land successful")

    except Exception as e:
        print(f"Error during Land: {e}")
