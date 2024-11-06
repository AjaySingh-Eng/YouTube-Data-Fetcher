# YouTube Channel Video and Comments Data Fetcher

## Project Overview
- This project is a Python script that fetches video data and the latest 100 comments with replies from a YouTube channel using the YouTube Data API v3.

## Features
- Collects data such as video ID, title, description, published date, view count, like count, comment count, duration, and thumbnail URL.
- Fetches up to 100 recent comments with replies for each video.

## Prerequisites
- Python 3.7+
- `pip` for managing Python packages
- API access to YouTube Data API v3

# Setup Instructions

## Clone the Repository
- git clone https://github.com/your-username/YouTube-Data-Fetcher.git
- cd YouTube-Data-Fetcher

## Create a Virtual Environment
- python -m venv env
- env\Scripts\activate

## Install Dependencies
- pip install -r requirements.txt

# Instructions for Creating a YouTube API Key:
## Sign in to Google Cloud Console:

- Go to the Google Cloud Console.
- Sign in with your Google account.
- Create a New Project:

- In the top-left corner, click on the project selector dropdown.
- Click New Project.
- Enter a project name (e.g., YouTube Data Project) and click Create.
- Once the project is created, select it from the project selector dropdown.
- Enable the YouTube Data API v3:

## Navigate to APIs & Services > Library.
- In the search bar, type YouTube Data API v3.
- Click on YouTube Data API v3 and then click Enable.
- Create Credentials:

## Go to APIs & Services > Credentials.
- Click on + Create Credentials and select API key.
- The API key will be generated and displayed in a pop-up window. Copy this key as you will need it for your application.
- Restrict Your API Key (Optional but Recommended):

## Click on Restrict Key to add restrictions.
- Under Application restrictions, select IP addresses, HTTP referrers, or other restrictions as needed.
- Under API restrictions, select Restrict key and choose YouTube Data API v3.
- Save the changes.
- Store the API Key Securely:

## Store your API key in a .env file in your project directory:
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
- Make sure not to share or expose your API key publicly (e.g., in a GitHub repository).
- Set Up dotenv in Your Project (Optional):

## To load your API key from a .env file, install the python-dotenv package:
pip install python-dotenv

- In your script, load the environment variables:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

## Notes:
Quota Limit: Each API key has a quota limit. Monitor your usage in the Google Cloud Console to avoid exceeding your quota.
Billing: Enabling billing on your Google Cloud account may grant you additional quotas.

## Example API Call (Python):
from googleapiclient.discovery import build

api_key = 'YOUR_API_KEY_HERE'
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    forUsername="GoogleDevelopers"
)
response = request.execute()

print(response)






## Set Up API Key
- Create a .env file in the project root and add:
- YOUTUBE_API_KEY=your_api_key_here

## Running the Script
- python src/youtube_data_fetcher.py

# Output:
## The script will create an Excel file (YouTube_Video_Data.xlsx) containing:
- Sheet 1: Video data with details like video ID, title, views, likes, and more.
- Sheet 2: Comments data with details like comment text, author name, and published date.

# Dependencies
- Python libraries: google-api-python-client, pandas, openpyxl, python-dotenv
- Install dependencies with:
- pip install -r requirements.txt

# Error Handling
- The script handles errors gracefully and prints informative error messages.

# Contribution
- Feel free to submit issues or pull requests for improvements

### Code Quality
- Ensure your code is well-organized, using functions or modules for different parts (e.g., fetching channel info, fetching video details, fetching comments).
- Add meaningful comments and adhere to Python's best practices (PEP 8).

### API Key Security
- Ensure your `.env` file is included in `.gitignore` to prevent the API key from being uploaded to GitHub.

### Excel Output Requirement
- Confirm that the script generates an Excel file with two sheets: one for video data and another for comments.

### Error Handling
- Make sure the script handles API-related errors (e.g., 403 errors for disabled comments) and any other issues gracefully, showing clear error messages.

### Final Checklist Before Submission
- Verify all files, including `README.md`, `requirements.txt`, and source code, are in your GitHub repository.
- Confirm your `.env` file is excluded.
- Push your latest changes to GitHub:
- git add .
- git commit -m "Final version of YouTube data fetcher project"
- git push origin main

  # Explanation:
- load_dotenv(): Loads the API key from .env file.
- build(): Creates a YouTube API client instance.
- get_channel_id(): Retrieves the channel ID using the channel handle.
- get_videos(): Fetches all videos from the channel using pagination.
- get_video_details(): Gets detailed information for each video.
- get_video_comments(): Fetches the latest 100 comments and replies for each video.
- main(): Combines the above functions, saves the video and comments data to an Excel file.

# Explanation of Each File/Directory:
- src/: Contains the main Python script (youtube_data_fetcher.py).
- .gitignore: Specifies files and directories that Git should ignore (e.g., .env, __pycache__, etc.).
- .env: Holds sensitive information like the API key (should not be committed).
- README.md: Provides project information, setup instructions, usage details, and more.
- requirements.txt: Lists the required Python packages for easy installation with pip.
- YouTube_Video_Data.xlsx: The generated Excel file containing the results (not included in Git to avoid large file uploads).


# File Structure
```bash
C:\youtube-data-fetcher\
└── YouTube-Data-Fetcher\
    ├── env\
    ├── src\
    │   └── youtube_data_fetcher.py
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    └── YouTube_Video_Data.xlsx



