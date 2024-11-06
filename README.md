YouTube Channel Video and Comments Data Fetcher
Project Overview
This Python script fetches video data and comments from a YouTube channel specified by its handle and outputs the information into an Excel file with two sheets: one for video data and another for comments.

Prerequisites
Python 3.7 or higher installed on your system.
Access to the YouTube Data API v3 (API key needed).
Step-by-Step Guide
1 Clone the Repository
Clone the GitHub repository (replace <repo-link> with your repo link):


git clone <repo-link>
cd youtube-data-fetcher
2 Create a Virtual Environment
Create a virtual environment to isolate your project dependencies:


python -m venv env
env\Scripts\activate

3 Install Dependencies
Install the necessary Python packages:


pip install -r requirements.txt
4 Set Up the YouTube Data API

Go to the Google Cloud Console.

Create a new project (or select an existing one).

Enable the YouTube Data API v3 for your project.

Under APIs & Services > Credentials, create an API key.

Copy the API key and store it in a .env file in the project root:

Create a .env file:

YOUTUBE_API_KEY=your-api-key-here
5 Run the Script
Execute the Python script to fetch YouTube data:


python src/youtube_data_fetcher.py

6 Output
The script outputs an Excel file named YouTube_Video_Data.xlsx in the project directory.
Sheet 1: Contains video data (e.g., title, description, view count).
Sheet 2: Contains the latest 100 comments and their replies.
Error Handling and Tips
Error Handling: The script includes basic error handling to notify you if something goes wrong (e.g., missing API key or invalid channel URL).
Environment Variables: Ensure that your .env file is included in .gitignore to prevent exposing your API key.
Dependencies
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
pandas
openpyxl
python-dotenv
Installing Individual Packages (Optional)
If needed, install packages individually:

pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas openpyxl python-dotenv
License
This project is licensed under the MIT License.

Project Description:-

This project is a Python script to fetch video details and comments from a YouTube channel using its handle. The data is saved in an Excel file with two sheets: Video Data and Comments Data.

Prerequisites
1 Python 3.x
2 A Google Cloud project with the YouTube Data API v3 enabled.


Explanation:

load_dotenv(): Loads the API key from .env file.
build(): Creates a YouTube API client instance.
get_channel_id(): Retrieves the channel ID using the channel handle.
get_videos(): Fetches all videos from the channel using pagination.
get_video_details(): Gets detailed information for each video.
get_video_comments(): Fetches the latest 100 comments and replies for each video.
main(): Combines the above functions, saves the video and comments data to an Excel file.
