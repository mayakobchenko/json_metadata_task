# json_metadata_task
import json and display in human readable version

$ cd deliver_maya

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
source myenv/bin/activate
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
