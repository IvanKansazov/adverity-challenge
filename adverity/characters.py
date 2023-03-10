import requests
from datetime import datetime
from adverity.models import Planets

class Characters:
    def __init__(self):
        self.all_characters = {'Characters': []}
        self.swapi_response = None

    def get_all(self):
        sw_people_url = 'https://swapi.dev/api/people'
        while True:
            self.request(sw_people_url)
            if bool(self.swapi_response.get('next')):
                sw_people_url = self.swapi_response.get('next')
                self.transform_characters()
                self.append_characters()
            else:
                break
        return self.all_characters

    def request(self, _url='https://swapi.dev/api/people'):
        response = requests.get(_url)
        self.swapi_response = response.json()

    def transform_characters(self):
        for i, character in enumerate(self.swapi_response.get('results')):
            date = datetime.strptime(character.get('edited'), '%Y-%m-%dT%H:%M:%S.%fZ')
            self.swapi_response.get('results')[i]['edited'] = date.strftime('%Y-%m-%d')
            self.swapi_response.get('results')[i]['homeworld'] = self.get_homeworld(character.get('homeworld'))

    def get_homeworld(self, homeworld_url):
        homeworld_name = ''
        try:
            planet = Planets.objects.get(url=homeworld_url)
            homeworld_name = planet.name
        except Planets.DoesNotExist:
            homeworld_name = self.resolve_homeworld(homeworld_url)
            Planets(url=homeworld_url, name=homeworld_name).save()
        return homeworld_name

    @staticmethod
    def resolve_homeworld(homeworld_url):
        response = requests.get(homeworld_url)
        return response.json().get('name')

    def append_characters(self):
        self.all_characters['Characters'].extend(self.swapi_response.get('results'))
