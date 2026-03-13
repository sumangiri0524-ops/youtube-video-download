import su_dlp
import os

def download_youtube_video(url, output_path="video"):
    try:
        # Create output folder if it does not exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # yt_dlp options
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'noplaylist': True  # Download single video only
        }

        print(f"Attempting to download: {url}")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download completed! Video saved to '{output_path}' folder.")

    except yt_dlp.utils.DownloadError as de:
        print(f"Download error: {str(de)}")

        # List available formats if download fails
        print("\nListing available formats...")

        try:
            with yt_dlp.YoutubeDL({'listformats': True}) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"Failed to list formats: {str(e)}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)
