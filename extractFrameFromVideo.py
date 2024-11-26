import cv2

def extract_frame(video_path, timestamp):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Convert timestamp to seconds
    hours, minutes, seconds = map(int, timestamp.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Set video capture position to the desired timestamp
    cap.set(cv2.CAP_PROP_POS_MSEC, total_seconds * 1000)

    # Capture frame
    success, frame = cap.read()

    if success:
        # Save the frame
        cv2.imwrite("extracted_frame.png", frame)
        print("Frame extracted successfully!")
    else:
        print("Failed to extract frame. Timestamp may be out of range.")

    # Release video capture
    cap.release()

# Example usage
video_path = input('enter video location (./video.webm) >')
timestamp = input("enter timestamp (00:01:27) >")
extract_frame(video_path, timestamp)
