from pydriller import Repository
from datetime import datetime
from statistics import statistic2
import os
import csv

# Global configurations for all repositories.
global_configurations = {
    "since": ""  # (datetime): only commits after this date will be analyzed
}

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

# Repositories
_path1 = "../repositories/Brasilino"  # repo1
_path2 = "../repositories/dialetus-service"  # repo2
_path3 = "../repositories/nullstack"  # repo3
_path4 = "../repositories/Potigol"  # repo4
_path5 = "../repositories/RastreioBot"  # repo5
_path6 = "../repositories/tainacan"  # repo6

_path_list = [_path1, _path2, _path3, _path4, _path5, _path6]

aux = 0

print(f"Welcome!")
while True:

    op = int(input("0. Exit\n"
                   "1. Show repositories list.\n"
                   "2. Count LOC per author on Repositories on Time Window.\n"
                   "3. Count commits on Repositories on Time Window.\n"))

    if op == 0:
        exit(1)

    # 1
    elif op == 1:
        for index, repo in enumerate(_path_list):
            print(f"Repository {index + 1}: {repo}")

    # 2
    elif op == 2:
        if os.path.exists("./results/statistic2.csv"):
            os.remove("./results/statistic2.csv")

        with open("./results/statistic2.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["This file count the modified lines per author in the Repository.\n"
                             "The count is the total number of added + deleted lines."])
            for path in _path_list:

                # Repository name
                writer.writerow([path.split("/")[2]])
                print(f"Mining on {path.split('/')[2]}")

                # time window
                for time_window in time_window_list:
                    writer.writerow([time_window['since'].date(), time_window['to'].date()])
                    repo = Repository(path, since=time_window['since'], to=time_window['to'])
                    results = statistic2.main(repo)
                    for author, count in results.items():
                        writer.writerow([author, count])

                    writer.writerow(["Total modified lines", sum(results.values())])
                    writer.writerow("")

                writer.writerow("\n")
                writer.writerow("\n")
        print("Done!", end="\n\n")
    # 3
    elif op == 3:
        if os.path.exists("./results/statistic3.csv"):
            os.remove("./results/statistic3.csv")

        with open("./results/statistic3.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["This file count the total commits in the Repository.\n"
                             "The count is the total number of added + deleted lines."])
            for path in _path_list:

                # Repository name
                writer.writerow([path.split("/")[2]])

                # time window
                for time_window in time_window_list:
                    writer.writerow([time_window['since'].date(), time_window['to'].date()])
                    repo = Repository(path, since=time_window['since'], to=time_window['to'])
                    result = len(list(repo.traverse_commits()))
                    writer.writerow(["Total commits", result])

                writer.writerow("\n")
                writer.writerow("\n")
