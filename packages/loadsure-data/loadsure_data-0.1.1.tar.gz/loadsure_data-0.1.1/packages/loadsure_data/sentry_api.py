import requests


class SentryClient:

    def __init__(self, organization, project, token):

        self.host = f"https://sentry.io/api/0/projects/"
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}

        self.events_endpoint = self.host + f"{organization}/{project}/events/"
        self.issues_endpoint = self.host + f"{organization}/{project}/issues/"

    def get_events_project(self, cursor):
        cursor_parameter = f'?cursor=0:{cursor}:0'
        url = f"{self.events_endpoint}{cursor_parameter}"
        response = requests.get(url, headers=self.headers)
        try:
            return response.json()
        except:
            print(" Status Code: ", response.status_code)
            response.raise_for_status()

    def get_issues_project(self, cursor):
        cursor_parameter = f'?cursor=0:{cursor}:0'
        url = f"{self.issues_endpoint}{cursor_parameter}"
        response = requests.get(url, headers=self.headers)
        try:
            return response.json()
        except:
            print(" Status Code: ", response.status_code)
            response.raise_for_status()
