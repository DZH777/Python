import importlib.util
spec = importlib.util.spec_from_file_location("n2w", "C:/GitScripts/Python/Scripts/QuickPython_3rd/Task11/Module/n2w.py")
n2w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(n2w)

num = "99"
print(num, "=", n2w.num2words(num))