from datetime import datetime
import csv
import os
from statistics import statistic5, statistic6

# Time Window (JT)
JT1 = {
    "since": datetime(year=2019, month=1, day=1),  # 2019-01-01
    "to": datetime(year=2019, month=6, day=30)  # 2019-06-30
}
JT2 = {
    "since": datetime(year=2019, month=7, day=1),  # 2019-07-01
    "to": datetime(year=2019, month=12, day=31)  # 2019-12-31
}
JT3 = {
    "since": datetime(year=2020, month=1, day=1),  # 2020-01-01
    "to": datetime(year=2020, month=6, day=30)  # 2020-06-30
}
JT4 = {
    "since": datetime(year=2020, month=7, day=1),  # 2020-07-01
    "to": datetime(year=2020, month=12, day=31)  # 2020-12-31
}
JT5 = {
    "since": datetime(year=2021, month=1, day=1),  # 2021-01-01
    "to": datetime(year=2021, month=6, day=30)  # 2021-06-30
}
time_window_list = [JT1, JT2, JT3, JT4, JT5]

# Repositories issue url
repo1 = "https://api.github.com/repos/OtacilioN/Brasilino/issues"
repo2 = "https://api.github.com/repos/dialetus/dialetus-service/issues"
repo3 = "https://api.github.com/repos/nullstack/nullstack/issues"
repo4 = "https://api.github.com/repos/potigol/Potigol/issues"
repo5 = "https://api.github.com/repos/GabrielRF/RastreioBot/issues"
repo6 = "https://api.github.com/repos/tainacan/tainacan/issues"
repo_list = [repo1, repo2, repo3, repo4, repo5, repo6]

print("Welcome!")
while True:

    print("0. Exit\n"
          "1. Count all opened issues on window time.\n"
          "2. Count all closed issues on window time.")

    op = int(input())

    if op == 0:
        exit(1)

    elif op == 1:
        if os.path.exists("./results/statistic5.csv"):
            os.remove("./results/statistic5.csv")

        with open("./results/statistic5.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Count all opened issues on window time"])
            writer.writerows([[], []])

            for url in repo_list:
                results = statistic5.main(url=url, time_window_list=time_window_list)

                writer.writerow([url.split('/')[5]])

                for JT in results:
                    writer.writerow([JT, results[JT]])

                writer.writerow("\n")

    elif op == 2:
        if os.path.exists("./results/statistic6.csv"):
            os.remove("./results/statistic6.csv")

        with open("./results/statistic6.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Count all closed issues on window time"])
            writer.writerows([[], []])
            for url in repo_list:
                results = statistic6.main(url=url, time_window_list=time_window_list)

                writer.writerow([url.split('/')[5]])

                for JT in results:
                    writer.writerow([JT, results[JT]])

                writer.writerow("\n")
