import urllib.request

url = "https://i.mjh.nz/SamsungTVPlus/br.m3u8"

urllib.request.urlretrieve(url, "../listas/samsung.m3u8")

print("Samsung OK")
