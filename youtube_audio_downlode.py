from moviepy import VideoFileClip
import os

def convert_video_to_mp3(video_path, output_path="./audio"):
    try:
        print("Please wait...")

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        video = VideoFileClip(video_path)

        filename = os.path.splitext(os.path.basename(video_path))[0]
        output_file = os.path.join(output_path, filename + ".mp3")

        print("Converting...")
        video.audio.write_audiofile(output_file)

        print("Done! Check:", output_file)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    path = input("Enter local video file path: ").strip()
    convert_video_to_mp3(path)

