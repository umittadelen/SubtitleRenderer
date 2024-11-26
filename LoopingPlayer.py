import cv2

def play_video_loop(video_path, width=640, height=480):
    # Capture video from the specified file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Rewind video to the start
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Resize the frame to the desired size
            frame = cv2.resize(frame, (width, height))
            
            cv2.imshow('Video Player', frame)
            
            # Exit if 'q' is pressed
            if cv2.waitKey(30) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return

# Replace 'your_video_file.mp4' with your actual video file path
play_video_loop('your_video_file.mp4')
