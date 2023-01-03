import os
from googleapiclient.discovery import build
from datetime import datetime, timezone, timedelta
import environ

from finvid.models import Video

env = environ.Env()
environ.Env.read_env()

def fetch_videos():

    """Fetch videos from YouTube API"""

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, developerKey=env('YOUTUBE_API_KEY'))

    request = youtube.search().list(
        part="snippet",
        publishedAfter=(datetime.now(timezone.utc)-timedelta(hours=1)).astimezone().isoformat(),
        order="date",
        maxResults=5,
        q="finance",
    )
    response = request.execute()
    videos_list = response['items']
    
    for video in videos_list:
        video_id = video['id']['videoId']
        title = video['snippet']['title']
        description = video['snippet']['description']
        publish_datetime = video['snippet']['publishTime']
        thumbnail = video['snippet']['thumbnails']['high']['url']
        video = Video.objects.get_or_create(video_id=video_id, defaults = {'title':title, 'description':description, 'publish_datetime':publish_datetime, 'thumbnail':thumbnail})
        print(video)
