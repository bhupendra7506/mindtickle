import os
import requests

from configurations import serverConfig
from services.utils.commonUtils import fileUtils

host_url = serverConfig.AUTHORS_SERVICE_HOST
resources_folder = fileUtils.getProjectRootDir() + os.sep + "resources" + os.sep \
                   + "authorsService"


def get_authors():
    return requests.get(host_url + "/api/v1/Authors", params={}, headers={"accept": "text/plain"})


def add_author(id, book_id, firstName, lastName):
    body_json = fileUtils.readJsonFile(resources_folder + os.sep + "author_api_request_response_body.json")
    body_json["id"] = id
    body_json["idBook"] = book_id
    body_json["firstName"] = firstName
    body_json["lastName"] = lastName

    return requests.post(host_url + "/api/v1/Authors",
                         json=body_json,
                         headers={"Content-Type": "application/json", "v": "1.0", "accept": "text/plain"})


def update_author(id, book_id, firstName, lastName):
    body_json = fileUtils.readJsonFile(resources_folder + os.sep + "author_api_request_response_body.json")
    body_json["id"] = id
    body_json["idBook"] = book_id
    body_json["firstName"] = firstName
    body_json["lastName"] = lastName

    return requests.put(host_url + "/api/v1/Authors" + id,
                        json=body_json,
                        headers={"Content-Type": "application/json", "v": "1.0", "accept": "text/plain"})


def get_authors_by_book_id(book_id):
    return requests.get(host_url + "/api/v1/Authors/authors/books/" + book_id,
                        params={}, headers={"accept": "text/plain"})


def get_authors_by_id(id):
    return requests.get(host_url + "/api/v1/Authors/" + id, params={}, headers={"accept": "text/plain"})


def delete_authors_by_id(id):
    return requests.delete(host_url + "/api/v1/Authors/" + id, params={}, headers={"accept": "text/plain"})
