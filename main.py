import cv2
import mediapipe
import pyautogui


def mouse():
    capture_hands=mediapipe.solutions.hands.Hands()
    drawing_option=mediapipe.solutions.drawing_utils


    screen_width,screen_height= pyautogui.size()
    camera = cv2.VideoCapture(0)
    x1=y1=x2=y2=z1=z2=a1=b1=a2=b2=0
    # x1=x2=x3=x4=y1=y2=y3=y4=0


    while True:
        _,image=camera.read()

        image_height,image_width,_ = image.shape
        image=cv2.flip(image,1)
        rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        output_hands=capture_hands.process(rgb_image)
        all_hands=output_hands.multi_hand_landmarks
        if all_hands:
            for hand in all_hands:
                drawing_option.draw_landmarks(image,hand)
                one_hand_landmarks=hand.landmark
                for id,lm in enumerate(one_hand_landmarks):
                    x=int(lm.x*image_width)
                    y=int(lm.y*image_height)
                    # print(x,y)
                    if id==8:
                        cv2.circle(image,(x,y),10,(0,255,255))#sarı renk ve mouse hareketi işaret parmak
                        mouse_x=int(screen_width/image_width * x)
                        mouse_y=int(screen_height/image_height * y)
                    
                    
                        pyautogui.moveTo(mouse_x,mouse_y)
                  
                    
                    if id == 4:
                        cv2.circle(image,(x,y),10,(0,255,0))#yeşil birinci parmak
                        
                        x2=x
                        y2=y
                        
                        
                    if id == 8:
                        cv2.circle(image,(x,y),10,(0,255,255))#sarı  işaret  parmak

                        # x1=x
                        # y1=y
                        
                    if id==12:
                        cv2.circle(image,(x,y),10,(139,69,19))#mavi orta parmak
                        x1=x
                        y1=y
                     
                        
                    if id==16:
                        cv2.circle(image,(x,y),10,(0,0,255))#kırmızı dördüncü parmak
                        x3=x
                        y3=y

                      
                        
                    if id==20:
                        cv2.circle(image,(x,y),10,(0 ,0 ,0))#siyah beşinci parmak
                        x4=x
                        y4=y
                           
            dist = y2-y1
          
            if(dist<20):
                pyautogui.rightClick()
                


            dist2 = y2-y3
            if(dist2<20):
                pyautogui.click()
        
                
            dist3 = y2-y4
            print(dist3)
            if(dist3<30):
              
          
                pyautogui.mouseDown()

        
           
        
                
        cv2.imshow("Hand Movement video Capture",image)
        key=cv2.waitKey(100)
        if key == 27:
            break
    camera.release()
    cv2.destroyAllWindows()