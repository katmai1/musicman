import os
import eyed3


# ─── ALBUM ANALYZER ─────────────────────────────────────────────────────────────

class AlbumAnalyzer:

    def __init__(self, path):
        self.artist_possibles = []
        self.album_possibles = []
        self.genre_possibles = []
        self.path = path
        files = os.listdir(path)
        self.files = [i for i in files if i.endswith(".mp3")]

        # add dirname as possible album and artist
        self.artist_possibles.append(os.path.basename(path))
        self.album_possibles.append(os.path.basename(path))

    def most_common(self, lista):
        return max(set(lista), key=lista.count)

    @property
    def isAlbumFolder(self):
        if len(self.files) > 0:
            return True
        return False

    @property
    def artists(self):
        """ Return possibles artists name without duplicates"""
        return list(set(self.artist_possibles))

    @property
    def albums(self):
        """ Return possibles albums name without duplicates"""
        return list(set(self.album_possibles))
    
    @property
    def genres(self):
        """ Return possibles albums name without duplicates"""
        return list(set(self.genre_possibles))

    def getData(self):
        """ Returns data and headers for tracks model """
        header = ['NumTrack', 'title', 'filename', 'absolutePath']
        data = []
        for filename in self.files:
            audio = self.readID3(filename)
            if audio is not None:
                item = [
                    audio.tag.track_num[0], audio.tag.title,
                    filename, os.path.join(self.path, filename)
                ]
                data.append(item)
        return data, header

    def readID3(self, filename):
        """ Returns id3 object if filename is audio """
        if filename.endswith("mp3"):
            file_path = os.path.join(self.path, filename)
            audio = eyed3.load(file_path)
            self.artist_possibles.append(audio.tag.artist)
            self.album_possibles.append(audio.tag.album)
            self.genre_possibles.append(str(audio.tag.non_std_genre))
            return audio
        return None
# ────────────────────────────────────────────────────────────────────────────────
