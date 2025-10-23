import json
import os

def save_to_file(data, filename):
  try:
    dir_path = os.path.dirname(filename)
    if dir_path:
      os.makedirs(dir_path, exist_ok=True)

    with open(filename, 'w') as f:
      json.dump(data, f, indent=2)
    print(f"Saved results to: {filename}")
  except Exception as e:
    print(f"Error saving results to file: {e}")

def clear_console():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")