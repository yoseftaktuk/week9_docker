from fastapi import FastAPI
from pathlib import Path
import json
from pydantic import BaseModel
import uvicorn

app = FastAPI()

DB_PATH = Path('db/shopping_list.json')



class Item(BaseModel):

    id: int = None
    name: str 
    quantity: int

def add_id():
    data = load_database()
    if  len(data) == 0:
        return 1
    item = data[-1]
    return item['id'] + 1

def check_database_exists() -> None:
    if not DB_PATH.exists():
        print('database file is missing')
        raise FileNotFoundError

def save_database_path(file_path: None ,data: dict) -> None:
    """Save dictionary data to JSON file"""
    if file_path: #בדיקה אם הכניסו מיקום קובץ(למפתח)
         with open(file_path, "w") as f:
            json.dump(save_data, f, indent=2) 

def load_database_path(file_paph) -> dict:
    if file_path: #בדיקה אם הכניסו מיקום קובץ(למפתח)
         with open(file_paph, "r") as f:
            return json.load(f)               

def save_database(data: dict) -> None:
    """Save dictionary data to JSON file"""
    save_data = load_database()
    save_data.append(data)
    with open(DB_PATH, "w") as f:
        json.dump(save_data, f, indent=2)   
      

def load_database() -> dict:
    """Load data from JSON file and return as dictionary"""
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


def check_json_exists():
    if len(load_database()): 
        save_database([])   

@app.get('/item')
def get_items():
    check_json_exists()
    return load_database()

file_path_local = "./data/backup_shopping_list.json"
file_path = '/app/data/backup_shopping_list.json'



@app.get('/backup')
def get_items_from_mount():
    return load_database_path(file_path_local)



@app.post('/item')
def add_new_item(item: Item):
    try:
        check_database_exists()
        item.id = add_id()
        data = {'id':item.id,
                'name': item.name,
                'quantity': item.quantity}
        save_database(data=data)
        return {"The sending was successful."}
    except:
        return{'The sending was unsuccessful.'}

@app.post('/backup/save')  
def save_to_bind_mount():
    try:    
        data = load_database(file_path_local)
        save_database_path(file_path=file_path, data=data)
        return {"The sending was successful."}
    except:
        return{'The sending was unsuccessful.'}

if not load_database():
        save_database([])

if __name__ == "__main__":
    if not load_database_path(file_path_local):
        save_database([])
    uvicorn.run(app, host="0.0.0.0", port=8000)