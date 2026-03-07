import urllib.request

url = "https://iptv-org.github.io/iptv/countries/br.m3u"
arquivo_temp = "../listas/_temp_br.m3u"

urllib.request.urlretrieve(url, arquivo_temp)

with open(arquivo_temp, "r", encoding="utf-8") as f:
    linhas = f.readlines()

saida = []

for linha in linhas:
    if "#EXTINF" in linha or linha.startswith("http"):
        saida.append(linha)

with open("../listas/plex.m3u8", "w", encoding="utf-8") as f:
    f.writelines(saida)

print("Lista Plex Brasil atualizada!")
