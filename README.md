# json_metadata_task
Imports a json file containing nested dictionaries and displays it in human readable version

There are two approaches implemented: uvicorn server serves the data to a webbrowser, read_print_json.py displays the data in a terminal

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
