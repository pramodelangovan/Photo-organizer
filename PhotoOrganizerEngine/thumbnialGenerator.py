import os
import sys
from PIL import Image


def find_dest_path(src_dir, dest_dir, src_path):
    full_src_path = os.path.realpath(src_path)
    full_src_dir = os.path.realpath(src_dir)
    rel_src_path = full_src_path[len(full_src_dir):]
    return dest_dir + rel_src_path

def create_thumbnail(src_path, dest_path, thumbnail_width, thumbnail_height):
    try:
        image = Image.open(src_path)
        image.thumbnail((thumbnail_width, thumbnail_height))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        image.save(dest_path)
    except OSError as err:
        pass
