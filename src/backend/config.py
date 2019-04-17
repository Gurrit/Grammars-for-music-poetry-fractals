import os


class config:

    step = 7
    gf_output_path = "fractals/"
    gf_script_path = "create_fractal.gfs"
    gf_file_path = "./app/te/"
    midi_path = "./midi-files/"
    wav_path = "./wav-files/"
    PORT = os.environ.get('GRAMMAR_PORT', 8765)
