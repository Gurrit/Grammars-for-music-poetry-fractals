import os


class config:

    step = 4
    gf_file_path = "gf_output.txt"
    PORT = os.environ.get('GRAMMAR_PORT', 8765)
