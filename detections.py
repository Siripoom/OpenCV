import cv2
import numpy


# * Color Detection
# while True:
#     img = cv2.imread("image/image.jpg")
#     # color range
#     lower = numpy.array([40, 4, 140])
#     upper = numpy.array([161, 87, 245])
#     mask = cv2.inRange(img, lower, upper)
#     mask = cv2.bitwise_and(img, img, mask=mask)
#     if cv2.waitKey(0) & 0xFF == ord("e"):
#         break

#     cv2.imshow("Image Original", img)
#     cv2.imshow("Pink Detect", mask)
# cv2.destroyAllWindows()

# # * Image with Face Detection
# img = cv2.imread("image/face.jfif")
# img = cv2.resize(img, (400, 400))

# # todo read file for classification การแยกประเภท
# faceCascade = cv2.CascadeClassifier("detect/frontalface_default.xml")
# grayImag = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # color to gray
# # todo face cascade
# scaleFactor = 1.10  # value default 1.1 , img reduced size 10%(.1)
# minNeighber = 1  # value 3, detect face position
# faceDetect = faceCascade.detectMultiScale(grayImag, scaleFactor, minNeighber)

# for x, y, w, h in faceDetect:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


# # todo show Image
# cv2.imshow("Face Detection OG", img)
# # cv2.imshow("Face Detection",faceDetect)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # * Video with Face detection
# cap = cv2.VideoCapture(0)  # ? Use web camera
# faceCascade = cv2.CascadeClassifier(
#     "detect/frontalface_default.xml"
# )  # ? use model Classifier
# while True:
#     check, frame = cap.read()  # ? receive image from camera frame per frame
#     if check == True:
#         grayscale = cv2.cvtColor(
#             frame, cv2.COLOR_BGR2GRAY
#         )  # change footage color to gray scale.
#         # todo face cascade
#         faceDetect = faceCascade.detectMultiScale(grayscale, 1.1, 3)  #
#         for x, y, w, h in faceDetect:
#             cv2.rectangle(
#                 frame, (x, y), (x + w, y + h), (255, 0, 0), 2
#             )  # draw rectangle on face
#         cv2.imshow("Camera ", frame)  # show result
#         if cv2.waitKey(1) & 0xFF == ord("e"):  # the press e for stop program
#             break
#     else:
#         break
# cv2.release()
# cv2.destroyAllWindows()  # return memory

# * Eye/Face detection image
# todo read image
img = cv2.imread("image/Kayla-Person.jpg")
#@img = cv2.resize(img, (400, 400))
# todo image color image rgb to gray
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# todo read file for classification
faceCascade = cv2.CascadeClassifier("detect/frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("detect/eye_tree_eyeglasses.xml")
# todo face and eye cascade
faces = faceCascade.detectMultiScale(grayscale, 1.1, 4)
eyes = eyeCascade.detectMultiScale(grayscale, 1.1, 4)
# todo draw rectangle for face and eye
for x, y, h, w in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)
    for ex, ey, eh, ew in eyes:
        cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (255, 0, 0),2)
# todo show image
cv2.imshow("Face&Eye detection image",img)
cv2.waitKey(0)
cv2.desstroyAllWindows()  # ? return memory
