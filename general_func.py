import cv2
import datetime
import numpy as np

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

# * Video record .VideoWrite is function for save new video
# todo1 Open camera
# todo2 Record video
# todo3 Save as a new video and type(mp4)
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
# * Draw Line/Arrow
# todo read image
# file = "D:\Python-Basic\OpenCV\image\ds_wordcloud.png"
# img = cv2.imread(file)
# todo edit image
# img = cv2.resize(img,(700,700))
# todo draw line
# ? line (image, start(x,y), end(x,y), color(BRG), weight)
# cv2.arrowedLine(img,(700,700),(100,100),(255,0,0),3)
# todo draw rectangle
# ? ractangle(image, มุมที่1ซ้ายบน, มุมที่2ล่างขวา, color, weight)
# cv2.rectangle(img, (0,0),(500,500),(255,0,0),2) #weight -1
# todo draw circle
# ? .circle(image, center(x,y)),radius,color(BRG),thickness)
# cv2.circle(img,(500,500),70,(255,0,0),3)
# todo put Text
# ?  .putText(image,text,coordinates(x,y),font,size,color,weight)
# cv2.putText(img,"Human",(400,400),2,2,(255,0,0),4)

# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# * Show date-time in video
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# result = cv2.VideoWriter("OutputwithDateTime.avi",fourcc,20.0,(640,480))
# while cap.isOpened():
#     check, frame = cap.read()

#     if check == True:
#         currentDate = str(datetime.datetime.now())
#         cv2.putText(frame,currentDate,(10,30),1,2,(0,0,0),2)
#         cv2.imshow("Output", frame)
#         result.write(frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break

# result.release();
# cap.release();
# cv2.destroyAllWindows();

# * Show mouse points with Mouse Event
# * Detect color with Mouse
# imgp = "image/ds_wordcloud.png" # Get filepath of image to variable
# img = cv2.imread(imgp)
# def clickPosition(event,x,y,flages,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         blue = img[y,x,0] #? blue is variable, img[y,x,0] 0 = color is a position to read. BGR (3 dimension)
#         green = img[y,x,1]
#         red = img[y,x,2]
#         colors = str(blue)+","+str(green)+","+str(red)
#         points = str(x)+","+str(y)
#         cv2.putText(img,colors,(x,y),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,0),2)
#         cv2.imshow("Image and Mouse Event",img)
#         print("X: ",x,"\nY: ",y)
#         print("BRG:"+colors)
# #todo Show OG
# cv2.imshow("Image and Mouse Event",img)
# #todo With Mouse Event
# cv2.setMouseCallback("Image and Mouse Event",clickPosition)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# * Demo show a image from pixel
# img = cv2.imread("image/ds_wordcloud.png")
# def clickPosition(event, x, y, flages, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         blue = img[
#             y, x, 0
#         ]  # ? blue is variable, img[y,x,0] 0 = color is a position to read. BGR (3 dimension)
#         green = img[y, x, 1]
#         red = img[y, x, 2]
#         imgcolor = np.zeros([300,300,3],np.uint8)
#         imgcolor[:] = [blue,green,red]
#         cv2.imshow("Result",imgcolor)
#         print(imgcolor)
# #todo Show OG
# cv2.imshow("Image and Mouse Event",img)
# #todo With Mouse Event
# cv2.setMouseCallback("Image and Mouse Event",clickPosition)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#*Connect point
img = np.zeros([400,400,3]) # 400,400 == width*height of window, 3 == read a colors value whit BGR

points = []

def click(event, x, y, flages, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(25,159,0),3)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),3)
            print(points)
            print(points[-1])
            print(points[-2])
        cv2.imshow("Image",img) #! Show recent image
        # print(x,y)


cv2.imshow("Image",img) #! Show OG image

cv2.setMouseCallback("Image",click)
cv2.waitKey(0)
cv2.destroyAllWindows()