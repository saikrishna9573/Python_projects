from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video():
    # Open a file dialog to select the download location
    download_path = filedialog.askdirectory()

    # URL of the YouTube video to download
    video_url = input("Please enter a YouTube url: ")

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution stream available
    stream = yt.streams.get_highest_resolution()

    # Download the video to the selected path
    stream.download(output_path=download_path)

    print(f"Downloaded '{yt.title}' to '{download_path}'")


# Create a simple GUI
root = tk.Tk()
root.title("YouTube Video Downloader")

# Add a button to trigger the download
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
