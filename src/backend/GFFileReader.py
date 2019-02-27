class GFFileReader:

    def __init__(self):
        self._gf_file_path = ""

    def read_gf_file(self):
        file = open("Sierpinski.txt", "r")      #TODO Exchange for the path to the file

        if file.mode == 'r':
            file_as_string = file.read()

        return file_as_string.split(" ")