def read_gf_file(filename):
    file = open(filename, "r")

    file_as_string = ""
    if file.mode == 'r':
        file_as_string = file.read()

    return file_as_string.split(" ")