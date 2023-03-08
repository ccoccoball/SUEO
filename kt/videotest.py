import cv2
import os

os.makedirs('Media', exist_ok=True)

fourcc = cv2.VideoWriter_fourcc(*'MP4V') 

out = cv2.VideoWriter('SUEO_01_output.mp4', fourcc, 30.0, (1920,1080))

for j in range (1, 11) :    

    cap = cv2.VideoCapture('D:/JiSongYoung/JiSongYoung/kt/D/NIA_SL_WORD1501_REAL01_D.mp4')
        
    # if cap.isOpened:

    while(cap.isOpened()):
            ret, frame = cap.read()
            # if ret==True:
            #         cv2.imshow('frame',frame)
            #         out.write(frame)   
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            # else:
            #     break

            if ret == False :
                break

            for k in range (1, 11) :
                cv2.imshow('frame', frame)
                out.write(frame)

                if cv2.waitKey(1) & 0xFF == ord('q') :
                    break

    cap.release()
    out.release()
    # else :
    # print("Can't open Video")

    
    cv2.destroyAllWindows()