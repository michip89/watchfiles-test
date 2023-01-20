
## watchfiles-test

Example project trying to integrate [watchfiles](https://github.com/samuelcolvin/watchfiles) Python library into Docker container.

Unfortunately until now I've been unsuccessful as the script isrunning inside of the container but changes are not detected.

To reproduce this issue run the script locally and the again inside the container.

### Run Locally

Install requirements () inside virtual environment (tested with Python 3.10):

```sh
pip install -r requirements.txt
```

Run script from project directory:

```sh
watchfiles "python test.py"
```

While the script is running change the code inside the `test.py` Python script, for example in line 44
from `print(i)` to `print(i*2)` and save the file.

In the output the change will be detected and the script starts auto reloading:

```
6
7
8
[15:39:08] 1 change detected
Shutdown
0
2
4
```

### Run inside container

Build and start the container with `docker-compose`:

```sh
docker-compose up
```

Now the script should be running inside the container log.

Unfortunately, changing the `test.py` Python script triggers no auto reload.