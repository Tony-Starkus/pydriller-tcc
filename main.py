from pydriller_tcc import Repository
from datetime import datetime

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
_path1 = "./repositories/Brasilino"  # repo1
_path2 = "./repositories/dialetus-service"  # repo2
_path3 = "./repositories/nullstack"  # repo3
_path4 = "./repositories/Potigol"  # repo4
_path5 = "./repositories/RastreioBot"  # repo5
_path6 = "./repositories/tainacan"  # repo6

_path_list = [_path1, _path2, _path3, _path4, _path5, _path6]

# Repositories
for path in _path_list:

    # time window
    for time_window in time_window_list:
        repo = Repository(path, since=time_window['since'], to=time_window['to'])
        print(f"{repo=}")

