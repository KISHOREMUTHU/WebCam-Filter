
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier("haarcascade_mcs_eyepair_big.xml")
nose_cascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")
mustache = cv2.imread('mustache.png',-1)
glasses = cv2.imread('glasses.png',-1)

while True :
       ret ,frame = cap.read()
       gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       faces= face_cascade.detectMultiScale(gray,1.5,5)
       frame = cv2.cvtColor(frame ,cv2.COLOR_BGR2BGRA)
       for (x,y,w,h) in faces :q
                   roi_gray =gray[y:y+h,x:x+h]
                   roi_color =frame[y:y+h,x:x+h]
                   eyes = eyes_cascade.detectMultiScale(roi_gray,1.5,5)
                   for (ex,ey,ew,eh) in eyes:
                          roi_eyes =roi_gray[ey:ey +eh,ex:ex+ew]
                          glasses2 =cv2.resize(glasses.copy(),(int(ew),int(2*eh)))
                          gw,gh,gc = glasses2.shape
                          for i in range(0, gw):
                                 for j in range(0, gh):
                                        print(glasses[i, j]) #RGBA
                                        if glasses2[i, j][3] != 0:  # alpha 0
                                               roi_color[ey - int(eh / 2) + i, ex + j] = glasses2[i, j]
                   nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
                   for (nx, ny, nw, nh) in nose:
                          # cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
                          roi_nose = roi_gray[ny: ny + nh, nx: nx + nw]
                          mustache2 = cv2.resize(mustache.copy(), (nw, int(0.5 * ny)))

                          mw, mh, mc = mustache2.shape
                          for i in range(0, mw):
                                 for j in range(0, mh):
                                        # print(glasses[i, j]) #RGBA
                                        if mustache2[i, j][3] != 0:  # alpha 0
                                               roi_color[ny + int(nh / 2.0) + i, nx + j] = mustache2[i, j]

       frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

       cv2.imshow('frame', frame)
       if cv2.waitKey(120) & 0xFF == ord('q'):

                       break

                   # When everything done, release the capture
cap.release()

cv2.destroyAllWindows()


