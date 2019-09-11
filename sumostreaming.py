import numpy as np
import cv2
import interface as ifd


#window = namedWindow("TheWindow",1)
#ser = serial.Serial(port='/dev/tty.usbserial-AD01QBMW', timeout=0)

controller = ifd.SumoController()


while(True):

    frame = controller.get_pic()

    if (frame):

        nparr = np.fromstring(frame, np.uint8)
        #img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #controller.move(10)

        cv2.imshow("SumoScreen", img_np)

    command = cv2.waitKey(1)

    if command & 0xFF == ord('w'):
        controller.move(10)
    elif command & 0xFF == ord('W'):
        controller.move(100)
    elif command & 0xFF == ord('a'):
        controller.move(10,-10)
    elif command & 0xFF == ord('d'):
        controller.move(10,10)
    elif command & 0xFF == ord('s'):
        controller.move(-30)
    elif command & 0xFF == ord('S'):
        controller.move(-100)

    if command & 0xFF == ord('q'):
        break

#When everything done, release the capture
cv2.destroyAllWindows()
