import yt_dlp
import os

def download_youtube_video(url, output_path="video") :
    try:
        #Create output folder if it not having
        if not os.path.exists(output_path) :
            os.makedirs(output_path)

        # yt_dlp options
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'noplaylist': True, # Download single video
        }

        print(f"Attending to download: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed! Video saved to {output_path}")
    
    except yt_dlp.utils.DownloadError as de:
        print(f"Download error: {str(de)}")
        # List available formats if download fails
        print("\nLisitng available formats...")
        try:
            with yt_dlp.YoutubeDL({'listformats': True}) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"Failed to list formats: {str(e)}")
    except Exception as e:
        print(f"An error occured: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)