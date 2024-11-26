import subprocess, os

def convert_webm_to_mp4(input_file, output_file):
    # Full path to your FFmpeg executable
    ffmpeg_path = f"C:/Users/{os.getlogin()}/Desktop/ytdlp/ffmpeg/bin/ffmpeg.exe"
    
    # Command to run FFmpeg and re-encode to a proper MP4 format
    command = [
        ffmpeg_path,             # Use the full path to FFmpeg
        "-i", input_file,        # Input file
        "-c:v", "libx264",       # Video codec (H.264 for MP4 compatibility)
        "-c:a", "aac",           # Audio codec (AAC for MP4 compatibility)
        "-strict", "experimental",  # Allow experimental codecs (for AAC)
        "-map", "0",             # Map all streams (video, audio, etc.)
        "-preset", "fast",       # Faster encoding (optional)
        output_file              # Output file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

# Example usage
input_file = "input_video.webm"  # Replace with your .webm file path
output_file = "output_video.mp4"  # Replace with your desired output path

convert_webm_to_mp4(input_file, output_file)
