import cv2
import sys


def main():
    image = cv2.imread(sys.argv[1])
    gray_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_detection_cascade = cv2.CascadeClassifier(sys.argv[2])

    faces = face_detection_cascade.detectMultiScale(
        gray_scale_image,
        scaleFactor = 1.2,  # 1.1 originally
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    number_of_faces = len(faces)
    print "Found %d %s!" % (number_of_faces, "face" if number_of_faces is 1 else "faces")

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()