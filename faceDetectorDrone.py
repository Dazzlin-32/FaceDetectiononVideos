import cv2 
import numpy as np
import mss 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



vid = cv2.VideoCapture(0)


# #size of the video capture
# frame_width = int(vid.get(3)) 
# frame_height = int(vid.get(4)) 
   
# size = (frame_width, frame_height) 
# # videowriter for full screen
out = cv2.VideoWriter("output.avi", cv2.VideoWriter.fourcc(*'DIVX'), 10.0, (1920, 1080))

# #videowriter for videocapture
# out = cv2.VideoWriter("output.avi", cv2.VideoWriter.fourcc(*'DIVX'), 30.0, size)
# while(True): 
      
#     # Capture the video frame 
#     # by frame 
#     ret, frame = vid.read() 

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
  
#     # Display the resulting frame 
#     cv2.imshow('Detecting Faces', frame) 

#     #write the frame
#     out.write(frame)
      
#     # the 'q' button is set as the 
#     # quitting button you may use any 
#     # desired button of your choice 
#     if cv2.waitKey(1) & 0xFF == ord('q'): 
#         break
  
# # After the loop release the cap object 
# vid.release() 
# #Release resources
# out.release()
# # # Destroy all the windows 
# # cv2.destroyAllWindows() 



#CODE FOR SCREEN RECORD


with mss.mss() as sct:
    monitor = sct.monitors[1]

    while True:
        # Capture screen
        screenshot = sct.grab(monitor)
        
        # Convert the screenshot to a numpy array
        frame = np.array(screenshot)
        
        # Convert the frame from BGRA to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Display the frame
        #cv2.imshow("Screen Capture with Face Detection", frame)

        #write the frame
        out.write(frame)
        
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#Release resources
out.release()
cv2.destroyAllWindows()