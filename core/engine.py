import importlib
import os

class CoreEngine:
  def __init__(self):
    self.modules_dir = "modules"  # Directory containing modules

  def list_modules(self):
    modules = []
    for root, _, files in os.walk(self.modules_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_path = os.path.join(root, file)
                modules.append(module_path.replace("\\", ".")[:-3])  # Convert to importable path
    return modules

  def load_module(self, module_name):
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError as e:
        return None

  def run_module(self, module_name, target):
    module = self.load_module(module_name)
    if module and hasattr(module, "run"):
      module.run(target)