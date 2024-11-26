# Project Setup and Usage Guide

To successfully run this project, follow these steps carefully.

### Prerequisites

1. **FFmpeg**: Download and extract FFmpeg to the `./ffmpeg/` folder, ensuring the `/bin/ffmpeg.exe` is located inside it.
2. **yt-dlp**: Download `yt-dlp.exe` and place it in the same `./ffmpeg/` folder.
   
   **Note**: The directory structure should look like this:
    ```
    /project-root/
    ├── /ffmpeg/
    │   ├── /bin/
    │       └── ffmpeg.exe
    ├── yt-dlp.exe
    └── (other project files)
    ```

### Step-by-Step Instructions

1. **Download the Video**
- Run the `DownloadVideo.py` script.
- Enter the URL of the video you want to download when prompted.
- The video will be downloaded and saved in the `./output/` folder.

2. **Prepare the Video**
- After downloading, rename the video file (either `.mp4` or `.webm`) in the `./output/` folder to `output_video`.
- Move the renamed `output_video` file to the root directory of the project (`/project-root/`).

3. **Generate Subtitles**
- Run the `VideoToSubtitles.py` script.
- This will generate a `.vtt` subtitle file containing the rendered frames as text-based subtitles, saved in the root folder.

4. **Hardcode Subtitles into the Video**
- Run the `HardcodeSubsAsTextToVideo.py` script.
- This will render the subtitles onto the video, creating a new video file with hardcoded subtitles.

### Output Files

- **Video**: The original video (`output_video.mp4` or `output_video.webm`) is used as input.
- **Subtitles**: A `.vtt` subtitle file will be generated after running `VideoToSubtitles.py`.
- **Final Video**: The video with hardcoded subtitles will be the final output after running `HardcodeSubsAsTextToVideo.py`.
