# video_creator.py

from moviepy.editor import TextClip, AudioFileClip, CompositeVideoClip
from moviepy.config import change_settings

# Update this to match your system's actual path
change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick\magick.exe"
})

def create_video(summary_text, audio_path, output_video_path):
    audio_clip = AudioFileClip(audio_path)
    text_clip = TextClip(summary_text, fontsize=24, color='white', bg_color='black',
                         size=(720, 1280), method='caption').set_duration(audio_clip.duration)
    video = CompositeVideoClip([text_clip]).set_audio(audio_clip)
    video.write_videofile(output_video_path, fps=24)
    print("🎬 Video created successfully.")

if __name__ == "__main__":
    with open("data/summaries/os_summary.txt", "r", encoding="utf-8") as f:
        summary_text = f.read()

    create_video(
        summary_text=summary_text,
        audio_path="data/audio/os_summary.mp3",
        output_video_path="data/videos/os_summary.mp4"
    )
