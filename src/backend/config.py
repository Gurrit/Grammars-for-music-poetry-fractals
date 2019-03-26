import os


class config:

    step = 2
    gf_output_path = "fractals/"
    gf_script_path = "create_fractal.gfs"
    gf_file_path = "/app/te/"
    PORT = os.environ.get('GRAMMAR_PORT', 8765)
