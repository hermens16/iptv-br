import os

listas = [
    "../listas/pluto.m3u8"
]

saida = "../listas/lista_completa.m3u8"

with open(saida, "w", encoding="utf-8") as final:
    final.write("#EXTM3U\n")

    for lista in listas:
        if os.path.exists(lista):
            with open(lista, "r", encoding="utf-8") as f:
                for linha in f:
                    if linha.startswith("#EXTM3U"):
                        continue
                    final.write(linha)

print("Lista completa criada")
