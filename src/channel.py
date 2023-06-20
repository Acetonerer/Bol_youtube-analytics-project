import json
import os

from googleapiclient.discovery import build


class Channel:
    """
    Класс для ютуб-канала
    """

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API
        """
        self.__channel_id = channel_id
        channel_info = self.get_service().channels().list(id=self.__channel_id, part='snippet, statistics').execute()
        self.title = channel_info['items'][0]['snippet']['title']
        self.description = channel_info['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.sub_count = int(channel_info['items'][0]['statistics']['subscriberCount'])
        self.video_count = channel_info['items'][0]['statistics']['videoCount']
        self.view_count = channel_info["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале
        """
        api_key: str = os.getenv('API_KEY')
        yt = build('youtube', 'v3', developerKey=api_key)
        chan = yt.channels()
        chan = chan.list(id=self.__channel_id, part='snippet, statistics').execute()

        print(json.dumps(chan, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        yt = build('youtube', 'v3', developerKey=api_key)
        return yt

    def to_json(self, fname):
        file = f"../src/{fname}"
        with open(file, 'w') as f:
            data = {"id": self.__channel_id,
                    "title": self.title,
                    "description": self.description,
                    "url": self.url,
                    "subs_count": self.sub_count,
                    "video_count": self.video_count,
                    "view_count": self.view_count,
                    }
            json.dump(data, f)
