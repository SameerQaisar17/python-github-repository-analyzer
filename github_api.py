import requests


class GitHubAPI:

    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github+json"
        })

    def make_request(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"

        try:
            response = self.session.get(url, timeout=10)

            if response.status_code == 404:
                raise Exception("GitHub username not found.")

            if response.status_code == 403:
                raise Exception(
                    "GitHub API rate limit reached. Try again later."
                )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            raise Exception("Request timed out. Please try again.")

        except requests.exceptions.ConnectionError:
            raise Exception("Internet connection problem.")

        except requests.exceptions.HTTPError:
            raise Exception("GitHub API request failed.")

        except requests.exceptions.RequestException:
            raise Exception("Something went wrong with the request.")

    def get_profile(self, username):
        return self.make_request(f"users/{username}")

    def get_repositories(self, username):
        return self.make_request(
            f"users/{username}/repos?per_page=100&sort=updated"
        )