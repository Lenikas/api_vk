import pathlib
import urllib
import requests
from request_data import RequestFormat


def do_request(link: str):
    try:
        page = requests.get(link)
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError from e
    return page


def preparse_rq(method, optional_params=""):
    rq = RequestFormat(method, optional_params=optional_params)
    response = do_request(rq.format_request())
    return response.json()['response']['items']


def get_friends():
    data_friends = preparse_rq("friends.get", "fields=nickname&order=hints&")
    with open("friends.txt", "w", encoding="utf-8") as f:
        for friend in data_friends:
            f.write(friend["first_name"] + " " + friend["last_name"] + "\n")


def get_groups():
    data_groups = preparse_rq("groups.get", "extended=1&fields=name&")
    with open("groups.txt", "w", encoding="utf-8") as f:
        for group in data_groups:
            f.write(group["name"] + "\n")


def download_images(image, num):
    try:
        urllib.request.urlretrieve(image, pathlib.Path.cwd() / "photos" / f"{num}.jpg")
    except urllib.error.URLError as e:
        raise e


def get_photos_from_search():
    data_photos = preparse_rq("photos.search", "sort=1&count=10&")
    for data in data_photos:
        download_images(data["photo_1280"], str(data["owner_id"]))


def get_photos_from_albums():
    data_albums = preparse_rq("photos.getAlbums")
    for item in data_albums:
        download_images(item["src"], str(item["id"]))


if __name__ == '__main__':
    get_friends()
    get_groups()
    get_photos_from_search()
    get_photos_from_albums()
