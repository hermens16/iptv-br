arquivos = [
"../listas/pluto.m3u8",
"../listas/plex.m3u8",
"../listas/samsung.m3u8",
"../listas/runtime.m3u8"
]

saida = "../lista_completa.m3u8"

with open(saida,"w",encoding="utf-8") as out:

    out.write("#EXTM3U\n")

    for arquivo in arquivos:

        try:
            with open(arquivo,"r",encoding="utf-8") as f:

                for linha in f:

                    if linha.startswith("#EXTM3U"):
                        continue

                    out.write(linha)

        except:
            print("Erro em",arquivo)

print("Lista completa criada")
