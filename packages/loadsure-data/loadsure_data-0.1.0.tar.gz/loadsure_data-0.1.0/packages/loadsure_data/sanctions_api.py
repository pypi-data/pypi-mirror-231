import requests


class SanctionsClient:

    def __init__(self, token, version):
        self.host = 'https://api.sanctions.io'
        self.search = self.host + '/search'
        self.headers = {
            'Accept': f'application/json; version={version}',
            'Authorization': f'Bearer {token}'
        }

    def search_sanctions_name(self, min_score, name, country_residence, data_source):

        params = {
            'min_score': min_score,
            'name': name,
            'data_source': data_source,
            'country_residence': country_residence
        }

        response = requests.request('GET', self.search, headers=self.headers, params=params)
        try:
            return response.json()
        except:
            print(" Status Code", response.status_code)
            response.raise_for_status()
