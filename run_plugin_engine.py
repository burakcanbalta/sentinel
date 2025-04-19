import importlib.util
import os

def run_plugin(name):
    path = f"plugins/{name}.py"
    if not os.path.exists(path):
        return {"error": "Plugin not found"}

    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        result = mod.run() if hasattr(mod, "run") else "No run() found"
        return {"result": str(result)}
    except Exception as e:
        return {"error": str(e)}
