import os
from pathlib import Path
from PIL import Image
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


class VideoGenerator:
    def __init__(self):
        self.temp_dir = Path("data/temp_frames")
        self.temp_dir.mkdir(exist_ok=True)

    def _prepare_frame(self, img_path: str, target_res: tuple = (1280, 720)) -> str:
        """Standardize image format and resolution"""
        output_path = str(self.temp_dir / f"processed_{Path(img_path).name}")
        with Image.open(img_path) as img:
            img = img.convert("RGB").resize(target_res, Image.LANCZOS)
            img.save(output_path, quality=90)
        return output_path

    def generate(
            self,
            audio_path: str,
            image_paths: list,
            output_path: str,
            fps: int = 24,
            resolution: tuple = (1280, 720)
    ) -> str:
        """
        Generate video from audio and images

        Args:
            audio_path: Path to audio file
            image_paths: List of image paths
            output_path: Output video path (.mp4 recommended)
            fps: Framerate (24 is standard)
            resolution: Target (width, height)

        Returns:
            Path to generated video
        """
        try:
            # 1. Process all images to consistent format
            processed_images = [self._prepare_frame(p, resolution) for p in image_paths]

            # 2. Calculate durations
            audio = AudioFileClip(audio_path)
            duration = audio.duration / len(processed_images)

            # 3. Create and concatenate clips
            clips = [ImageClip(img, duration=duration) for img in processed_images]
            video = concatenate_videoclips(clips, method="compose").set_audio(audio)

            # 4. Export with optimized settings
            video.write_videofile(
                str(output_path),
                fps=fps,
                codec="libx264",
                audio_codec="aac",
                preset="fast",
                threads=4,
                ffmpeg_params=["-pix_fmt", "yuv420p"]
            )

            return str(output_path)

        except Exception as e:
            print(f"Video generation failed: {str(e)}")
            raise
        finally:
            # Cleanup
            if 'video' in locals():
                video.close()
            audio.close()
            for clip in clips:
                clip.close()