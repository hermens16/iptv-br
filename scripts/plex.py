import urllib.request

url = "https://i.mjh.nz/Plex/pl.m3u8"

urllib.request.urlretrieve(url, "../listas/plex.m3u8")

print("Plex OK")
