import cv2

# * READ IMAGE
# file = "D:\Python-Basic\OpenCV\image\ds_wordcloud.png" #? get image file path to file(variable)
# img = cv2.imread(file)  #? read image file path with .imread(image read function)
# print(type(img.ndim)) #? print ndim is dimension and type of image

# #* SHOW IMAGE
# file = "D:\Python-Basic\OpenCV\image\ds_wordcloud.png" #? get image file path to file(variable)
# img = cv2.imread(file,0)  #? read image file path with .imread(image read function,0=grey scale,1=color scale)
# #todo show image
# cv2.resize(img,(400,400)) #todo Resize image .resiez(image read,(w,h))
# cv2.imshow("my image ",img) #? .imshow(title,image red)
# cv2.waitKey(delay=5000)
# cv2.destroyAllWindows() #? return memory / close window

# * Export image
# cv2.imwrite("newImage.png",img) #? .imwrite("filename.type(jpeg,png)",img read)

# * Open camera with OpenCV
# cap = cv2.VideoCapture(0)

# while(True):
#     check,result = cap.read() #? receive image from camera frame per frame
#     cv2.imshow("Camera ",result)

#     if cv2.waitKey(1) & 0xff == ord("e"):
#         break
# cv2.release()
# cv2.destroyAllWindows()

# * Open video with OpenCV
# cap = cv2.VideoCapture()  # ? (video file path) for open video

# while (cv2.isOpened()):
#     check, result = cap.read()  # ? receive image from camera frame per frame
#     if check == True:
#         cv2.imshow("Camera ", result)
#         if cv2.waitKey(1) & 0xff == ord("e"):
#             break
#     else:
#         break
# cv2.release()
# cv2.destroyAllWindows()

#* Video record .VideoWrite is function for save new video
#todo1 Open camera
#todo2 Record video
#todo3 Save as a new video and type(mp4)
# cap = cv2.VideoCapture(0)   #? todo change number according to your webcam
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# result = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480)) #? setting video

# while (cap.isOpened()):
#     check, frame = cap.read()  # ? receive image from camera frame per frame
#     if check == True:
#         cv2.imshow("Camera ", frame)
#         result.write(frame)
#         if cv2.waitKey(1) & 0xff == ord("e"):
#             break

# result.release()
# cv2.release()
# cv2.destroyAllWindows()
#* Draw Line/Arrow
#todo read image
file = "D:\Python-Basic\OpenCV\image\ds_wordcloud.png"
img = cv2.imread(file)
#todo edit image
img = cv2.resize(img,(700,700))
#todo draw line
#? line (image, start(x,y), end(x,y), color(BRG), weight)
cv2.arrowedLine(img,(700,700),(100,100),(255,0,0),3)
cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()