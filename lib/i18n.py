import os
import yaml


fallback = "en"
locales: list[str] = []
messages_cache: dict = {}
messages: dict = {}

for locale in os.listdir("locales"):
    code: str = locale.split(".yaml")[0]
    locales.append(code)
    with open(os.path.join("locales", locale), "r", encoding="utf-8") as file:
        messages[code] = yaml.safe_load(file)
        messages_cache[code] = {}


def t(code: str):
    if not code in locales:
        code = fallback
    cache_code: dict = messages_cache[code]

    def wrapper(key: str, opt: dict = {}) -> str:
        cache = cache_code.get(key)
        if type(cache) is str:
            return cache

        def deep(ms=messages[code], ks=key.split(".")) -> str:
            m = ms[ks[0]]
            if len(ks) < 1 or m is None:
                return key
            elif type(m) is str:
                for k in opt.keys():
                    m = m.replace("{{" + k + "}}", opt[k])
                messages_cache[code][key] = m
                return m
            else:
                return deep(m, ks[1:])

        return deep()

    return wrapper
