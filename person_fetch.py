import requests
import json
from functions import get_birth_date

# Search class
class Search():
    def __init__(self, string, im):
        self.refined_res = []
        # im = boolean value for returning images or not.
        self.string = string
        self.im = im
        self.identifier_phrases = [
            'political Party', 'Ugandan Parliament', 'politician', 'government', 'Governemt of Uganda', 'Commissioner-General',
            'Commissioner', 'Commissioner General' 'Parliament', 'president', 'President', 'vice president', 'Prime Minister ',
            'member of parliament', 'chief justice', 'judge', 'attorney general'
        ]

    def get_info(self):
        # lets get the reulsts here.
        url = "https://google-search3.p.rapidapi.com/api/v1/search/q=" + self.string + "&num=5"
        headers = {
            'x-user-agent': "desktop",
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': "18531cc5femshe002bc3470f9b5ap1e6e98jsn2e42b35c1e99"
            }
        resp = requests.request("GET", url, headers=headers)
        self.pep_identifier(resp)

        # if len(self.refined_res) <= 0:
        #     json_data = json.loads(resp.text)
        #     li = json_data['results']
        #     return li
        return (self.refined_res)

    def pep_identifier(self, data):
        json_data = json.loads(data.text)
        image_src= self.get_profile_url(self.string)

        # list of persons
        li = json_data['results']
        for each in li:

            for phrase in self.identifier_phrases:
                if phrase in each['description']:
                    each['PA'] = 'Person Flagged as pep'
                    each['PL'] = each['link']
                    each['DOB'] = get_birth_date(each['description'])
                    each['position'] = phrase
                    each['image'] = image_src
                    # each['PIC'] = each['picture']
                    # print (each)
                    self.refined_res.append(each)

    def get_profile_url(self, profile):

        url = "https://google-search3.p.rapidapi.com/api/v1/images/q="+ profile +""

        headers = {
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': "18531cc5femshe002bc3470f9b5ap1e6e98jsn2e42b35c1e99"
            }

        response = requests.request("GET", url, headers=headers)
        json_data = json.loads(response.text)
        pre_d = json_data['image_results'][0]
        img_src = pre_d['image']['src']
        return (img_src)