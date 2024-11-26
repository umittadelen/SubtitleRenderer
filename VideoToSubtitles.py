import cv2
import numpy as np
from tqdm import tqdm  # Import tqdm for the progress bar

# Parameters
ascii_chars = ["`", ".", ":", "o", "8", "&", "%", "#", "@"]  # Adjusted ASCII characters list
output_vtt_file = "video_ascii.vtt"
frame_width = 160  # Width of ASCII output (in characters)

def video_to_ascii_vtt(video_path):
    # Open video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception("Error opening video file")

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_duration = 1 / fps  # Duration of each frame in seconds
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Resize factor to fit ASCII width
    aspect_ratio = height / width
    ascii_height = int(frame_width * aspect_ratio * 0.5)

    # Open the VTT file for writing subtitles in real-time
    with open(output_vtt_file, "w", encoding="utf-8") as vtt_file:
        # Write the WebVTT header
        vtt_file.write("WEBVTT\n\nSTYLE\n::cue {\n  font-size: 24px;\n    font-family: Monospace, sans-serif;\n    color: white;\n}\n\n")

        prev_ascii_frame = None
        start_time = 0  # Start time of the current subtitle
        frame_idx = 0

        # Get total frame count for the progress bar
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Wrap the loop with tqdm for the progress bar
        with tqdm(total=total_frames, unit="frame") as pbar:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    # End of video, write the last subtitle if it exists
                    if prev_ascii_frame is not None:
                        end_time = start_time + frame_duration * frame_idx
                        write_subtitle(vtt_file, start_time, end_time, prev_ascii_frame)
                    break

                # Convert frame to black and white (grayscale)
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Resize the grayscale frame to fit ASCII dimensions
                resized_frame = cv2.resize(gray_frame, (frame_width, ascii_height))

                # Map each pixel to ASCII characters based on brightness
                ascii_frame = "\n".join(
                    "".join(ascii_chars[int(pixel / (256 / len(ascii_chars)))] for pixel in row)
                    for row in resized_frame
                )

                if ascii_frame != prev_ascii_frame:
                    # Write the previous subtitle if the frame changed
                    if prev_ascii_frame is not None:
                        end_time = start_time + frame_duration * frame_idx
                        write_subtitle(vtt_file, start_time, end_time, prev_ascii_frame)
                    
                    # Update start time and reset frame index for the new frame
                    start_time += frame_duration * frame_idx
                    prev_ascii_frame = ascii_frame
                    frame_idx = 1  # Reset frame index for the new subtitle
                else:
                    # Increment the frame counter for identical frames
                    frame_idx += 1

                # Update progress bar
                pbar.update(1)

        cap.release()

    print(f"Subtitles saved to {output_vtt_file}")

def write_subtitle(vtt_file, start_time, end_time, ascii_frame):
    # Convert timestamps to VTT format
    start_vtt = seconds_to_vtt(start_time)
    end_vtt = seconds_to_vtt(end_time)

    # Write the subtitle entry to the VTT file
    if ascii_frame.strip():  # Ensure no empty subtitles
        vtt_file.write(f"{start_vtt} --> {end_vtt}\n{ascii_frame}\n\n")

def seconds_to_vtt(time_in_seconds):
    hours = int(time_in_seconds // 3600)
    minutes = int((time_in_seconds % 3600) // 60)
    seconds = int(time_in_seconds % 60)
    milliseconds = int((time_in_seconds - int(time_in_seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

# Example usage
video_path = "output_video.webm"  # Replace with your video file
video_to_ascii_vtt(video_path)
