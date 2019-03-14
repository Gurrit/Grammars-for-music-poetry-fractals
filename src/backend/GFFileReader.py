from config import *


class GFFileReader:

    def __init__(self):
        self._gf_file_path = ""

    def read_gf_file(self, filename):
        file = open(filename, "r")

        file_as_string = ""
        if file.mode == 'r':
            file_as_string = file.read()

        return file_as_string.split(" ")