import requests


TOKEN_YANDEX = 'y0_AgAAAABqIlxsAADLWwAAAAD_W48jAAAWOUGANvtMnpEWsmIYRVato6SrQA'


def create_foler(token, name_folder):
    """Создать папку"""
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {"Authorization": token}
    response = requests.put(url, params={"path": name_folder}, headers=headers)
    return response.status_code
