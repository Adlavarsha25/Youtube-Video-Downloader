import pytube

# Ask user to input the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object from the URL
yt = pytube.YouTube(url)

# Choose the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
print("Downloading...")
stream.download()
print("Download completed.")
