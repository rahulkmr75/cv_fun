import cv2
import numpy as np
import mnt

s=""
#to store the list of moments
d=[]

#value in state 1
val=[]
state=0
sec=0
def findVariance(d):
    m1=0
    m2=0
    for i in range(0,len(d),3):
	m1=m1+d[i][0]
	m2=m2+d[i][1]
    m1=m1/(len(d)/3.0)
    m2=m2/(len(d)/3.0)
    
    var=0
    for i in range(0,len(d),3):
	var=var+(d[i][0]-m1)*(d[i][0]-m1)+(d[i][1]-m2)*(d[i][1]-m2)
    return m1,m2,var 
def drawLine(img,state):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if(state==0):
	cv2.rectangle(img,(180,140),(360,320),(0,255,0),3)
	cv2.rectangle(img,(360,140),(540,320),(0,255,0),3)
	cv2.putText(img,'Numpad',(215,300), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.putText(img,'Image',(420,300), font, 1,(255,255,255),2,cv2.LINE_AA)
    elif(state==1):
	global s
	cv2.rectangle(img,(180,0),(270,140),(0,255,0),3)
	cv2.putText(img,'1',(225,70), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(270,0),(360,140),(0,255,0),3)
	cv2.putText(img,'2',(315,70), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(360,0),(450,140),(0,255,0),3)
	cv2.putText(img,'3',(405,70), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(450,0),(540,140),(0,255,0),3)
	cv2.putText(img,'back',(465,70), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(180,140),(270,280),(0,255,0),3)
	cv2.putText(img,'4',(225,210), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(270,140),(360,280),(0,255,0),3)
	cv2.putText(img,'5',(315,210), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(360,140),(450,280),(0,255,0),3)
	cv2.putText(img,'6',(405,210), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(450,140),(540,280),(0,255,0),3)
	cv2.putText(img,'d',(495,210), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(180,280),(270,420),(0,255,0),3)
	cv2.putText(img,'7',(225,350), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(270,280),(360,420),(0,255,0),3)
	cv2.putText(img,'8',(315,350), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(360,280),(450,420),(0,255,0),3)
	cv2.putText(img,'9',(405,350), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(450,280),(540,420),(0,255,0),3)
	cv2.putText(img,'0',(495,350), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(180,420),(540,480),(0,255,0),3)
	cv2.putText(img,s,(190,470), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
    elif(state==2):
	cv2.rectangle(img,(500,320),(640,480),(0,255,0),3)
	cv2.putText(img,'back',(550,400),font,1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(360,320),(500,480),(0,255,0),3)
	cv2.putText(img,'edge',(380,400),font,1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(220,320),(360,480),(0,255,0),3)
	cv2.putText(img,'blur',(230,400),font,1,(255,255,255),2,cv2.LINE_AA)
	cv2.rectangle(img,(80,320),(220,480),(0,255,0),3)
	cv2.putText(img,'gray',(90,400),font,1,(255,255,255),2,cv2.LINE_AA)



cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    global state
    global sec

    ret,img=cap.read()
    drawLine(img,state)    
    
    cnt=mnt.findMoment(img)
    cv2.circle(img,(cnt[0],cnt[1]),5,(0,0,255),3)

    if(len(d)<30):
	d.append(cnt)
    else:
	d.pop(0)
	d.append(cnt)
 
    
    mx,my,var=findVariance(d)
    if(var<1000 and len(d)==30):
	if(state==0):
	    if(my<320 and my >140):
		if(mx>180 and mx<360):
		    state=1
		elif(mx>360 and mx<540):
		    state=2
		for i in range(0,30):
		    d.pop(0)
	elif(state==1):
	    row=-1
	    col=-1
	    if(my>0 and my<140):
		row=0
	    elif(my>140 and my<280):
		row=1
	    elif(my>280 and my<420):
		row=2
	    else:
		row=-1


	    if(mx>180 and mx<270):
		col=0
	    elif(mx<360 and mx>270):
		col=1
	    elif(mx<450 and mx>360):
		col=2
	    elif(mx>450 and mx<540):
		col=3
	    else:
		col=-1
	    
	    if(col==3):
		if(row==0):
		    state=0
		    for i in range(0,len(val)):
			val.pop(0)
		elif(row==1 and len(val)>0):
		    val.pop(len(val)-1)
		elif(row==2):
		    val.append('0')
	    else:
		num=row*3+col+1
		if(row*col>=0):
		    val.append(`num`)
	    s="".join(val) 

	    for i in range(0,30):
		    d.pop(0)
	elif(state==2):
	    if(my>320 and my<480):
		if(mx<640 and mx>500):
		    state=0
		    sec=0
		    for i in range(0,len(val)):
			val.pop(i)
		elif((mx<500 and mx>360)):
		    sec=1
		    for i in range(0,len(val)):
			val.pop(i)
		elif(mx<360 and mx>220):
		    sec=3
		    for i in range(0,len(val)):
			val.pop(i)

		elif((mx<220 and mx>80)):
		    sec=2
		    for i in range(0,len(val)):
			val.pop(i)
		
		if(sec==1):
		    img=cv2.Canny(img,100,200)
		elif(sec==2):
		    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		elif(sec==3):
		    img=cv2.GaussianBlur(img,(9,9),0)
	    print state,sec,mx,my

    cv2.imshow("img",img)
    k=cv2.waitKey(20) & 0xFF
    if k==27:
        break


