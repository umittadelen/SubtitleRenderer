import os

# Ensure the 'subtitles' directory exists
os.makedirs("output", exist_ok=True)

os.system(
    f'yt-dlp.exe {input("Enter video link: ")} '
    f'--write-subs --sub-langs all '
    f'--output "./output/%(title)s.%(ext)s" '
    f'--ffmpeg-location C:/Users/{os.getlogin()}/Desktop/ytdlp/ffmpeg/bin/ffmpeg.exe '
    f'-f bv+ba --no-check-certificate'
)

input("Done> ")
