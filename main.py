from core.engine import CoreEngine
from core.input import obtain_user_input
from core.output import clear_console

def modules():
  engine = CoreEngine()

  modules = engine.list_modules()

  # Display available modules
  print("Available Modules:")
  for i, module in enumerate(modules):
    print(f"{i + 1}. {module}")

  module_choice = obtain_user_input(["Select a module by number: ", int, False])
  module_choice = int(module_choice) - 1

  selected_module = modules[module_choice]
  module = engine.load_module(selected_module)

  clear_console()

  user_inputs = []

  if hasattr(module, "get_input_schema"):
    schema = module.get_input_schema()
    user_inputs = [obtain_user_input(field) for field in schema]
  else:
    print(f"No function named 'get_input_schema' in {module}")
    return

  engine.run_module(selected_module, user_inputs)

def clear_results():
  clear_console()

def settings():
  clear_console()

def main():
  clear_console()
  loop = True
  while loop:
    option = None
    print("Select an option:")
    print("1. Modules")
    print("2. Clear Results")
    print("3. Settings")
    print("4. Exit")
    option = input("Select an option: ")

    try:
      option = int(option)
    except:
      clear_console()
      print("Invalid Input!")

    clear_console()
    if option == 1:
      modules()
    elif option == 2:
      clear_results()
    elif option == 3:
      settings()
    elif option == 4:
      quit()
    else:
      print("Invalid Input!")

    _ = input("Enter to continue ")
    clear_console()
    

if __name__ == "__main__":
  main()