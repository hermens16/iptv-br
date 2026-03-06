import urllib.request

url = "https://i.mjh.nz/Runtime/pl.m3u8"

urllib.request.urlretrieve(url, "../listas/runtime.m3u8")

print("Runtime OK")
