import pandas as pd
from youtube_api import download_channels_videos
from youtube_api import merge_channel_videos
from utils import create_topic_columns
from language_api import download_sentiments

def crawl_merge():

	channels = pd.read_csv('channels.csv')
	download_channels_videos(channels)
	merge_channel_videos(channels)


def get_relevent():

	topics = pd.read_csv('topics.csv')
	videos = pd.read_csv('videos-MERGED.csv')
	create_topic_columns(videos, topics)
	videos.to_csv('videos.csv', index=False, encoding='utf-8')
	relevent_videos = videos[videos['relevant']]
	relevent_videos.to_csv('videos-relevant.csv', index=False, encoding='utf-8')


def sentiment():

	relevent_videos = pd.read_csv('videos-relevant.csv')
	download_sentiments(relevent_videos)

if __name__ == '__main__':
    crawl_merge()
    get_relevent()
    sentiment()
