import os
import requests

TOKEN = os.getenv("TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def get_pull_requests(state):
    """
    Example of return:
    [
        {"title": "Add useful stuff", "num": 56, "link": "https://github.com/boto/boto3/pull/56"},
        {"title": "Fix something", "num": 57, "link": "https://github.com/boto/boto3/pull/57"},
    ]
    """

    # Write your code here
    api_url = "https://api.github.com/repos/boto/boto3/pulls"
    params = {"state": state, "per_page": 100}

    response = requests.get(api_url, params=params, headers=HEADERS)
    if response.status_code != 200:
        response.raise_for_status()

    data = response.json()
    pulls = []
    for pull in data:
        pulls.append(
            # title, number -> num, html_url -> link
            {
                "title": pull.get("title"),
                "num": pull.get("number"),
                "link": pull.get("html_url"),
            }
        )
    return pulls
