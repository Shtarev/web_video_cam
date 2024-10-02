import time
import cv2

video = 'video/' + str(time.ctime(time.time())).replace(' ', '_') # name of the video file
check: int = 0 # setting the minute counter
stop: int = 3 # set working time is 3 minutes

def foo(video):
    i: int = 1
    j: int = 60
    br: int = 0
    font = cv2.FONT_ITALIC

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("нет подключения к камере")
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter(video + '.avi', fourcc, 20.0, (320, 240))

    while True:
        tip = cv2.waitKey(1)
        if tip == 27:
            br = 1
            break

        ret, frame = cap.read()
        frame = cv2.putText(frame, str(time.ctime(time.time())), (10, 40), font, 1, (210, 155, 155), 4, cv2.LINE_4)
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
        out.write(frame)
        cv2.imshow('Input', frame)
        i = i + 1
        if i > j:
            break

        time.sleep(1)

    out.release()
    return br

while True:
    if check == stop:
        break
    br = foo(video)
    if br == 1:
        break

    check = check +  1
    video = 'video/' + str(time.ctime(time.time())).replace(' ', '_')

cv2.destroyAllWindows()
