import numpy as np
import cv2
# import matplotlib.pyplot as plt

# b o r g y brown
colorlist=[(255,128,0),(0,128,255),(0,0,255),(0,255,128),(0,255,255),(0,0,102),(204,0,102),(102,0,102)]

def drawbirdview(detObj,label,X,finalcoor):

    img = np.zeros((800, 750, 3), np.uint8)
    img.fill(255)

    # cv2.putText(img,'0',(365,730),cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 0), 1, cv2.LINE_AA)
    # cv2.putText(img,'50',(605,730),cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 0), 1, cv2.LINE_AA)
    # cv2.putText(img,'-50',(85,730),cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 0), 1, cv2.LINE_AA)

    # x line
    for j in range(0,15):
        cv2.line(img,(0,750-j*50),(750,750-j*50),(200,200,200),1)
    # y line
    for j in range(-7,8):
        cv2.line(img,(375+j*50,750),(375+j*50,0),(200,200,200),1)

    cv2.line(img,(375,750),(375,0),(200,200,200),2)       
    cv2.line(img,(0,750),(750,750),(200,200,200),2) 

    numObj=detObj["numObj"]
    for i in range(numObj):
        x = int((X[i,0] + 75) * 5)
        y = int((150 - X[i,1])*5 )
        if label[i] == -1:
            cv2.circle(img,(x,y),8,(255, 0, 255), -1)

        else:
            cv2.circle(img,(x,y),8,colorlist[label[i]], -1)
 
    for coordinate in finalcoor:
        x = int((coordinate["x"] + 75)*5)
        y = int((150- coordinate["y"])*5 )
        cv2.rectangle(img,(x-50,y-50),(x+50,y+50),(51,51,255),5)
    
    cv2.imshow('real-time Bird plot result', img)
    cv2.waitKey(1)
