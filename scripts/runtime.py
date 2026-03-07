import urllib.request

url = "https://iptv-org.github.io/iptv/categories/movies.m3u"
urllib.request.urlretrieve(url, "../listas/runtime.m3u8")

print("Runtime atualizado")
