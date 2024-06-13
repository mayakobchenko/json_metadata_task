# json_metadata_task
Import json and display in human readable version
There are two approaches implemented, one serves the data to a webrowser, another one displays the data in a terminal
```
$ cd deliver_maya
```
create a virtual environment
``` sh
$ python -m venv myenv
```
activate the virtual environment
on windows PowerShell
```
$ .\myenv\Scripts\Activate.ps1
```
on Mac and Linux
```
$ source myenv/bin/activate
```
```
$ python -m pip install --upgrade pip
```
install dependencies
```
$ pip install -r requirements.txt
```
run the uvicorn server
```
$ uvicorn main:app --reload
```
Open the frontend in you browser http://127.0.0.1:8000 or http://localhost:8000
