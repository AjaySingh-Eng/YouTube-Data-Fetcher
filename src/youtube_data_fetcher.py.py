import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import pandas as pd

# Load API key from .env file
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please check your .env file.")

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Function to get channel ID from a channel handle URL
# Modified function to get the channel ID
def get_channel_id(channel_url):
    handle = channel_url.split('@')[-1]
    request = youtube.search().list(
        part="snippet",
        q=handle,
        type="channel",
        maxResults=1
    )
    response = request.execute()
    if "items" in response and response["items"]:
        return response["items"][0]["snippet"]["channelId"]
    else:
        raise ValueError("Channel ID could not be retrieved. Check the URL or handle.")


# Function to fetch all videos for a channel
def get_videos(channel_id):
    videos = []
    request = youtube.search().list(
        part="id,snippet",
        channelId=channel_id,
        maxResults=50,
        type="video"
    )
    while request:
        response = request.execute()
        for item in response.get("items", []):
            video_id = item["id"]["videoId"]
            video_details = get_video_details(video_id)
            if video_details:
                videos.append(video_details)
        request = youtube.search().list_next(request, response)
    return videos

# Function to get detailed information for a specific video
def get_video_details(video_id):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()
    if "items" in response and response["items"]:
        item = response["items"][0]
        duration = item["contentDetails"].get("duration", "N/A")  # Use .get() to avoid KeyError
        return {
            "Video ID": video_id,
            "Title": item["snippet"]["title"],
            "Description": item["snippet"]["description"],
            "Published Date": item["snippet"]["publishedAt"],
            "View Count": item["statistics"].get("viewCount"),
            "Like Count": item["statistics"].get("likeCount"),
            "Comment Count": item["statistics"].get("commentCount"),
            "Duration": duration,
            "Thumbnail URL": item["snippet"]["thumbnails"]["high"]["url"]
        }
    return None

# Function to fetch the latest 100 comments for a video
def get_video_comments(video_id):
    comments = []
    try:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=video_id,
            maxResults=100,
            textFormat="plainText"
        )
        response = request.execute()
        for item in response.get("items", []):
            top_comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "Video ID": video_id,
                "Comment ID": item["id"],
                "Comment Text": top_comment["textDisplay"],
                "Author Name": top_comment["authorDisplayName"],
                "Published Date": top_comment["publishedAt"],
                "Like Count": top_comment["likeCount"],
                "Reply To": None
            })
            # Handle replies
            if "replies" in item:
                for reply in item["replies"]["comments"]:
                    reply_snippet = reply["snippet"]
                    comments.append({
                        "Video ID": video_id,
                        "Comment ID": reply["id"],
                        "Comment Text": reply_snippet["textDisplay"],
                        "Author Name": reply_snippet["authorDisplayName"],
                        "Published Date": reply_snippet["publishedAt"],
                        "Like Count": reply_snippet["likeCount"],
                        "Reply To": item["id"]
                    })
    except HttpError as e:
        if e.resp.status == 403 and "commentsDisabled" in str(e):
            print(f"Comments are disabled for video ID: {video_id}. Skipping...")
        else:
            print(f"An error occurred while fetching comments for video ID: {video_id}. Error: {e}")
    return comments

# Main function to run the script
def main():
    channel_url = input("Enter the YouTube channel URL with a handle (e.g., https://www.youtube.com/@channelhandle): ")
    try:
        channel_id = get_channel_id(channel_url)
        videos = get_videos(channel_id)

        # Create DataFrame for video data
        video_df = pd.DataFrame(videos)
        video_df.to_excel("YouTube_Video_Data.xlsx", sheet_name="Video Data", index=False)

        # Collect and save comments data
        all_comments = []
        for video in videos:
            video_id = video["Video ID"]
            comments = get_video_comments(video_id)
            all_comments.extend(comments)

        comments_df = pd.DataFrame(all_comments)
        with pd.ExcelWriter("YouTube_Video_Data.xlsx", mode="a", engine="openpyxl") as writer:
            comments_df.to_excel(writer, sheet_name="Comments Data", index=False)

        print("Data has been successfully saved to 'YouTube_Video_Data.xlsx'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
