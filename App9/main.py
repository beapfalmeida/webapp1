import cv2
import time
from emailing import send_email
import glob
import os
from threading import Thread

video = cv2.VideoCapture(0)
time.sleep(1)
# reading only the first frame of the video

first_frame = None
status_list = []
count = 1


def clean_folder():
    images = glob.glob("images/*png")
    for image in images:
        os.remove(image)


while True:
    status = 0
    check, frame = video.read()

# turning the image gray to simplify the process
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# removing some noise. arg - (frame, blurriness, standard deviation)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

# Saving the first frame
    if first_frame is None:
        first_frame = gray_frame_gau

# Subtracting the other frames from the fist frame. To see the differences
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

# Simplify - make it only black and white pixels.
    # if pixel > 45 -> passa a ser branco (255)
    thresh_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

# Excluding small objects from the recognition
    # and drawing a rectangle around the object that entered the video
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))
        if rectangle.any():
            status = 1
            # Saving each frame as an image where the object appears
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1

            # Get the middle frame
            all_images = glob.glob("images/*png")
            index = int(len(all_images)/2)
            image_with_object = all_images[index]

    cv2.imshow("Video", frame)

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email,
                              args=(image_with_object, ))

        # email sending is being executed in the background:
        email_thread.daemon = True

        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True

        email_thread.start()

#  Stopping the program clicking in "q" in the keyboard
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
clean_thread.start()
