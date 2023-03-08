import cv2
import os

os.makedirs('Media', exist_ok=True)

for j in range (1, 21) :
        
        if j < 10 :
            
            path = 'D:/JiSongYoung/JiSongYoung/kt/D/NIA_SL_WORD150' + str(j) + '_REAL01_D.mp4'

            fourcc = cv2.VideoWriter_fourcc(*'MP4V') 

            for k in range (1, 11) :
                
                for s in range (1, 11) :

                    out = cv2.VideoWriter('SUEO_' + str(s) + '_output.mp4', fourcc, 30.0, (1920,1080))
                
                    cap = cv2.VideoCapture(path)
                        
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
        
        else :
            path = 'D:/JiSongYoung/JiSongYoung/kt/D/NIA_SL_WORD15' + str(j) + '_REAL01_D.mp4'

            fourcc = cv2.VideoWriter_fourcc(*'MP4V') 

            for k in range (1, 11) :
                
                for s in range (11, 21) :

                    out = cv2.VideoWriter('SUEO_' + str(s) + '_output.mp4', fourcc, 30.0, (1920,1080))
                    
                    cap = cv2.VideoCapture(path)
        
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