$ cd deliver_maya

create a virtual environment
$ python -m venv myenv

activate the virtual environment
on windows PowerShell
$ .\myenv\Scripts\Activate.ps1

on Mac and Linux
source myenv/bin/activate

$ python -m pip install --upgrade pip

$ pip install -r requirements.txt

$ uvicorn main:app --reload

