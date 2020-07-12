import os
import eyed3


# ─── ALBUM ANALYZER ─────────────────────────────────────────────────────────────

class AlbumAnalyzer:

    artist_possibles = []
    album_possibles = []

    def __init__(self, path):
        self.path = path
        self.files = os.listdir(path)
        # add dirname as possible album and artist
        self.artist_possibles.append(os.path.basename(path))
        self.album_possibles.append(os.path.basename(path))

    def getData(self):
        header = ['NumTrack', 'title', 'filename']
        data = []
        for filename in self.files:
            audio = self.readID3(filename)
            if audio is not None:
                item = [
                    audio.tag.track_num, audio.tag.title,
                    filename
                ]
                data.append(item)
        return data, header

    def readID3(self, filename):
        file_path = os.path.join(self.path, filename)
        audio = eyed3.load(file_path)
        if audio is not None:
            self.artist_possibles.append(audio.tag.artist)
            self.album_possibles.append(audio.tag.album)
            return audio
        return None
# ────────────────────────────────────────────────────────────────────────────────
