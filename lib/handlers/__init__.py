import os

base = os.path.dirname(__file__).replace(os.getcwd(), "")[1:]
module = base.replace("/", ".")

for filename in os.listdir(base):
    if filename.endswith(".py") and os.path.basename(__file__) != filename:
        mod = f"{module}.{filename[:-3]}"
        __import__(mod, globals(), locals())
