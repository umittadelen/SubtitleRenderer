import subprocess
import os

def hardcode_subtitles_with_cpu(video_path, subtitle_path, output_path, ffmpeg_path):
    """
    Hardcodes subtitles from a .vtt file into a video using FFmpeg with GPU acceleration for encoding/decoding 
    and CPU for subtitle rendering.
    
    :param video_path: Path to the input video file.
    :param subtitle_path: Path to the input .vtt subtitle file.
    :param output_path: Path to the output video file with hardcoded subtitles.
    :param ffmpeg_path: Path to the ffmpeg executable.
    """
    # Check if the input files exist
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    if not os.path.exists(subtitle_path):
        raise FileNotFoundError(f"Subtitle file not found: {subtitle_path}")
    
    # FFmpeg command with GPU acceleration for video encoding/decoding (and CPU for subtitles)
    command = [
        ffmpeg_path,
        '-i', video_path,  # Input video file
        '-vf', f"drawbox=c=black:t=fill,subtitles={subtitle_path}:force_style='Fontname=Monospace,Fontsize=5.4'",  # Apply subtitles with monospaced font
        #'-c:v', 'h264_nvenc',  # Encode video using NVIDIA NVENC for GPU acceleration
        '-preset', 'fast',  # Set encoding preset for speed (adjust as needed)
        '-c:a', 'copy',  # Copy the audio without re-encoding
        '-threads', '16',
        output_path  # Output video file path
    ]
    
    try:
        # Run the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Video saved to {output_path} with hardcoded subtitles (GPU accelerated video encoding).")
    except subprocess.CalledProcessError as e:
        print(f"Error during FFmpeg execution: {e}")

# File paths
video_path = "./output_video.webm"  # Input video path
subtitle_path = "./video_ascii.vtt"  # Path to the .vtt subtitle file
output_path = "./video_with_hardcoded_subs.mp4"  # Output video path
ffmpeg_path = f"C:/Users/{os.getlogin()}/Desktop/ytdlp/ffmpeg/bin/ffmpeg.exe"  # Path to ffmpeg executable

# Hardcode subtitles into video with GPU acceleration for encoding (and CPU for subtitles)
hardcode_subtitles_with_cpu(video_path, subtitle_path, output_path, ffmpeg_path)
