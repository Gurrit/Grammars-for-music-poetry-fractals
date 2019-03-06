import os


class config:

    step = 8
    gf_file_path = "gf_output.txt"
    PORT = os.environ.get('GRAMMAR_PORT', 8765)
