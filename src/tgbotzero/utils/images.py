import PIL.Image

import hashlib


def sha256(f):
    sha256_hash = hashlib.sha256()
    f.seek(0)
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


class Image:
    def __init__(self, filename: str = None, image: PIL.Image = None):
        self.filename = filename
        self.image = image
        if filename:
            self.io = open(filename, 'rb')


class _ImageManager:
    def __init__(self):
        self.images_tg_file_ids = {}

    def __setitem__(self, image: Image, file_id: int):
        hash = sha256(image.io)
        image.io.seek(0)
        self.images_tg_file_ids[hash] = file_id

    def __getitem__(self, image: Image):
        hash = sha256(image.io)
        image.io.seek(0)
        return self.images_tg_file_ids.get(hash, None)


_image_manager = _ImageManager()
