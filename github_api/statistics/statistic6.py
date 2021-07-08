import requests
from datetime import datetime


def main(url: str, time_window_list: list) -> dict:
    """
    Get all closed issues on window time.
    :param url: url or repository.
    :param time_window_list: list of time windows.
    :return: data: a dict that contains the count of opened issues on window time.
    """
    page = 1
    data = {"JT1": 0, "JT2": 0, "JT3": 0, "JT4": 0, "JT5": 0}

    print(f"Mining on {url.split('/')[5]}")
    while True:

        response = requests.get(f"{url}?page={page}&state=closed&access_token=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")

        if response.status_code == 403:
            print(f"Error: {response.json()['message']}")
            exit(1)

        if len(response.json()) == 0:
            break

        if response.status_code == 200:
            # print(f"{response.json()=}")
            # print(f"{len(response.json())}")
            for issue in response.json():

                # if issues is not a pull request
                if 'pull_request' not in issue:
                    closed_at = datetime.strptime(issue['closed_at'].split("T")[0], "%Y-%m-%d")

                    # JT1
                    if time_window_list[0]['since'] <= closed_at <= time_window_list[0]['to']:
                        data['JT1'] = data['JT1'] + 1

                    # JT2
                    elif time_window_list[1]['since'] <= closed_at <= time_window_list[1]['to']:
                        data['JT2'] = data['JT2'] + 1

                    # JT3
                    elif time_window_list[2]['since'] <= closed_at <= time_window_list[2]['to']:
                        data['JT3'] = data['JT3'] + 1

                    # JT4
                    elif time_window_list[3]['since'] <= closed_at <= time_window_list[3]['to']:
                        data['JT4'] = data['JT4'] + 1

                    # JT5
                    elif time_window_list[4]['since'] <= closed_at <= time_window_list[4]['to']:
                        data['JT5'] = data['JT5'] + 1
            page += 1
    print(f"Closed: {data=}")
    print(f"Done!")
    return data
