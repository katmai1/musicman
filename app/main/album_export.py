import os
from slugify import slugify
import shutil
import eyed3


# ─── EXPORT ALBUM ───────────────────────────────────────────────────────────────

class AlbumExport:

    def __init__(self, data):
        self.artist = data['artist']
        self.album = data['album']
        self.genre = data['genre']
        self.tracks = data['tracks']
        self.output_folder = data['output_folder']
        # define album folder
        self.artist_basename = f"{self.convString2File(self.artist)}"
        self.artist_abspath = os.path.join(self.output_folder, self.artist_basename)
        if not os.path.exists(self.artist_abspath):
            os.mkdir(self.artist_abspath)
        self.album_basename = f"{self.convString2File(self.artist)}-{self.convString2File(self.album)}"
        self.album_abspath = os.path.join(self.artist_abspath, self.album_basename)

    def export(self):
        os.mkdir(self.album_abspath)
        for data in self.tracks:
            orig_abspath = data[3]
            new_filename = f"{self.convString2File(self.artist)}-{self.convString2File(data[1])}.mp3"
            dest_abspath = os.path.join(self.album_abspath, new_filename)
            shutil.copyfile(orig_abspath, dest_abspath)
            #
            self.clearTags(dest_abspath)
            #
            a = eyed3.load(dest_abspath)
            a.tag.album = self.album
            a.tag.artist = self.artist
            a.tag.non_std_genre = self.genre
            a.tag.track_num = data[0]
            a.tag.title = data[1]
            a.tag.save()

    def clearTags(self, file):
        audio = eyed3.load(file)
        audio.tag.clear()
        audio.tag.remove(filename=file)
        audio.tag.save(filename=file)

    # ─── PROPERTIES ─────────────────────────────────────────────────────────────────

    @property
    def alreadyExists(self):
        if os.path.exists(self.album_abspath):
            return True
        return False

    # ─── INTERNAL ───────────────────────────────────────────────────────────────────
        
    def convString2File(self, text):
        """ Clean string and replace spaces to use as filenames """
        return slugify(text, lowercase=True, separator="_")
# ────────────────────────────────────────────────────────────────────────────────
