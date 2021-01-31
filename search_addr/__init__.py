import json
import requests
from os import path

REQ_SAVE_FILE_NAME = "place_address_to_google_places.json"

class AddrToGooglePlaces():
    def __init__(self):
        if not path.exists(REQ_SAVE_FILE_NAME):
            self.previous_search_request = {}
            self.update_file_data()

        with open(REQ_SAVE_FILE_NAME) as f:
            self.previous_search_request = json.load(f)

    def update_file_data(self):
        with open(REQ_SAVE_FILE_NAME, 'w') as outfile:
            json.dump(self.previous_search_request, outfile, indent=2)

    def update_search_request(self, search_key, search_google_places_obj):
        self.previous_search_request[search_key] = search_google_places_obj
        self.update_file_data()

    def search_google(self, addr):
        formatted_addr = addr.replace(", ", "+").replace(",", "+")
        if formatted_addr not in self.previous_search_request:
            resp = requests.get(
                "https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyBHRyhFuMKyjMdyiHQfiBuScnyOWGK2yks".format(
                    formatted_addr))
            self.previous_search_request[formatted_addr] = resp.json()
            self.update_file_data()
            print ("Made Google Request")
        return self.previous_search_request[formatted_addr]


if __name__ == '__main__':
    search_lib = AddrToGooglePlaces()
    search_lib.search_google("3, 186A, Vivek Khand 3, Gomti Nagar, Lucknow, Uttar Pradesh, 226010")
