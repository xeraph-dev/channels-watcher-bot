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
    """
    ## Example usage

    #### English translations
    ```yaml
    # /locale/en.yaml
    title: Title
    help:
        title: Help title
    var: 'The variable is: {{var}}'
    ```

    #### Spanish translations
    ```yaml
    # /locale/es.yaml
    title: Título
    help:
        title: Título de ayuda
    var: 'La variable es: {{var}}'
    ```

    #### Usages
    ```python
    # Direct access
    t('en')('title')    # Title
    t('es')('title')    # Título

    # Nested
    t('en')('help.title')   # Help title
    t('es')('help.title')   # Título de ayuda

    # Dynamic translation
    t('en')('var', {"var": "this"}) # The variable is: this
    t('es')('var', {"var": "this"}) # La variable es: this
    ```
    """
    if not code in locales:
        code = fallback
    cache_code: dict = messages_cache[code]

    def wrapper(key: str, opt: dict = {}) -> str:
        cache_key = key + str(opt)
        cache = cache_code.get(cache_key)
        if type(cache) is str:
            return cache

        def deep(ms=messages[code], ks=key.split(".")) -> str:
            m = ms[ks[0]]
            if len(ks) < 1 or m is None:
                return key
            elif type(m) is str:
                for k in opt.keys():
                    m = m.replace("{{" + k + "}}", opt[k])
                messages_cache[code][cache_key] = m
                return m
            else:
                return deep(m, ks[1:])

        return deep()

    return wrapper
