import dvc.api
import pandas as pd
import os
from mlflow import log_metric, log_param, log_artifact

if __name__ == "__main__":
    path='data/cars.csv'
    repo=r'C:\Users\lucia\Documents\Laburo\dvctesting'
    version='v2'
    

    log_param("data_version",version)
    # Log a parameter (key-value pair)
    log_param("param1", 5)

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", 1)
    log_metric("foo", 2)
    log_metric("foo", 3)

    # Log an artifact (output file)
    with open("output.txt", "w") as f:
        f.write("Hello world!")
    log_artifact("output.txt")
    resource_url = dvc.api.get_url(
    path,
    repo=repo,rev=version)
    print(resource_url)
    fd= dvc.api.read(path,repo=repo,rev=version)
    

    with open("file.txt", "w") as file:
        file.write(fd)
    log_artifact("file.txt")
    











# for element in fd:
#     if element=='"':
#         fd=fd.replace(element,"")

# print(fd)
# import io
# fd_csv =io.StringIO(fd)

# df=pd.read_csv(fd_csv,sep=',')
# df.head()
