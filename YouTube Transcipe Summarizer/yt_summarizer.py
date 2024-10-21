from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id_from_url(url):
    # Use a regex to extract the video ID from the YouTube URL
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        return None

def get_youtube_transcript(video_url):
    try:
        # Extract the video ID from the provided URL
        video_id = get_video_id_from_url(video_url)
        if not video_id:
            return "Invalid YouTube URL. Please check the URL and try again."

        # Fetch the transcript using the video ID
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Create a list to store the transcript text
        transcript_text = []

        # Loop through each part of the transcript and add text to the list
        for entry in transcript:
            transcript_text.append(entry['text'])

        # Join the list into a single string separated by spaces
        full_transcript = " ".join(transcript_text)

        return full_transcript

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Ask user for the YouTube video URL
    video_url = input("Please enter the YouTube video URL: ")

    # Get the transcript for the provided video
    transcript = get_youtube_transcript(video_url)

    # Print the transcript or the error message
    if "An error occurred" not in transcript:
        print("Transcript:\n", transcript)
    else:
        print(transcript)
