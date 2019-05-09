import os


class Config:

    step = 7
    gf_output_path = "files/fractals/"
    gf_script_path = "files/fractals/create_fractal.gfs"
    gf_file_path = "./files/gf/"
    midi_path = "./files/midi-files/"
    wav_path = "./files/wav-files/"
    PORT = os.environ.get('GRAMMAR_PORT', 8765)
