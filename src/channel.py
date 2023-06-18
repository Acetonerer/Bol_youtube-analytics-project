import json
import os

from googleapiclient.discovery import build


class Channel:
    """
    Класс для ютуб-канала
    """

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API
        """
        self.channel_id = channel_id

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале
        """
        api_key: str = os.getenv('API_KEY')
        yt = build('youtube', 'v3', developerKey=api_key)
        chan = yt.channels()
        chan = chan.list(id=self.channel_id, part='snippet, statistics')
        chann = chan.execute()
        print(json.dumps(chann, indent=2, ensure_ascii=False))
