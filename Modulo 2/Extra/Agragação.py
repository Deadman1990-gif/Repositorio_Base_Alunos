class Mídia:
    def __init__(self, video):
        self.video=video
    def aparecer_na_tela(self):
        print(f"{self.video} esta sendo exibido")
        

class Música(Mídia):
    def __repr__(self):
        return f"'{self.titulo}' por {self.artista}"
class Playlist:
    def __init__(self, nome: str, musica: list[Música], artista: str, titulo: str):
       self.nome=nome
       self.musicas=musica
       self.artista=artista
       self.titulo=titulo
    def tocar_todas(self):
        print(f"\n▶️ Tocando a Playlist '{self.nome}':")
        for musica in self.musicas:
            print(f" - Tocando agora: {musica}")
musica1=Música("Fear of The Dark", "Iron Maiden")
musica2=Música("Rock And Roll All Nite", "KISS")
musica3=Música("Sweet Child O' Mine", "Guns n' Roses")

daylist= Playlist("Sua Playlist Diária",
                  [musica1, musica2, musica3])
daylist.tocar_todas()