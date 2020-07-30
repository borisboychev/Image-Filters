import cv2

capture_device = cv2.VideoCapture(0)


def make_1080p():
    capture_device.set(3, 1920)
    capture_device.set(4, 1080)


def apply_invert(frame):
    # inverts values
    return cv2.bitwise_not(frame)


make_1080p()

while True:

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    ret, frame = capture_device.read()

    inverted = apply_invert(frame)

    cv2.imshow('inverted', inverted)
    # cv2.imshow('normal', frame)

cv2.destroyAllWindows()
