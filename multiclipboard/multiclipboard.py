import sys
import clipboard
import json
import pandas as pd

saved_clipboard = "clipboard.json"

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)
        
def load_json(filename):
    try:
        with open(filename, 'r') as f:
            the_load = json.load(f)
            return the_load
    except:
        return print("Operation failed - check the code!")
    
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_json(saved_clipboard)
    
    if command == "save":
        key = input("Enter a key to proceed the save: ")
        data[key] = clipboard.paste()
        save_json(saved_clipboard, data)
        
    elif command == "load":
        key = input("Enter a key to proceed the load: ")
        if key in data:
            clipboard.copy(data[key])  
            print("Successfully loaded the data into the clipboard!")
        else:
            print("Operation failed - key does not exist!")
    elif command == "delete":
        key = input("Enter a key to proceed the delete process: ")
        if key in data:
            del json.loads(data[key])
            print("Successfully deleted the data")
        else:
            print("Operation failed - key does not exist!")
    
    elif command == "list":
        print(data)
    
    else:
        print("Type correct command [save/load/delete/list]")
        quit()
else:
    print("Type only one command after the filename!")
    quit()