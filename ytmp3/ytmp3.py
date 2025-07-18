import requests

DEFAULT_API_BASE_URL = "https://api-den-0woa.onrender.com"

class YTtoMP3:
    def __init__(self, base_url=DEFAULT_API_BASE_URL):
        self.base_url = base_url.rstrip('/')

    def convert(self, video_id):
        url = f"{self.base_url}/convert"
        response = requests.post(url, json={"video_id": video_id})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
