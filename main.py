import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

os.chdir(os.path.dirname(__file__))

def read_print_pretty_json(file_path):
    """
    Reads a JSON file, outputs error message
    """
    try:
        with open(file_path, 'r') as file:
            pretty_json = json.load(file)   
    except Exception as e:
        print(f"An error occurred: {e}")
    return pretty_json

app = FastAPI(title="Display json file")

templates = Jinja2Templates(directory="templates")

# get python dictionary from json 
pretty_json = read_print_pretty_json('testDataset.json')

# Custom filter to check if a value is a list of dictionaries
def is_list_of_dicts(value):
    if isinstance(value, list):
        return all(isinstance(item, dict) for item in value)
    return False

# Register the custom filter with the Jinja2 environment
jinja_env = templates.env
jinja_env.filters['is_list_of_dicts'] = is_list_of_dicts

@app.get("/", response_class=HTMLResponse)
async def read_json(request: Request):
    # Ensure that data is a dictionary
    if not isinstance(pretty_json, dict):
        raise ValueError("Parsed JSON data is not a dictionary")
    return templates.TemplateResponse("display_json.html", {"request": request, "json_data": pretty_json})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)