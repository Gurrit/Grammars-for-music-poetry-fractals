import json


def serialize_coords(coordinate):
    return {'x': coordinate.x, 'y': coordinate.y}


def create_draw_json(lines, canvas, fractal, iteration, modified):
    ser_val = json.dumps({'mode': "draw",
                          'lines': [{'coordinate1': serialize_coords(line.coordinate_1),
                                     'coordinate2': serialize_coords(line.coordinate_2),
                                     'color': line.color
                                     } for line in lines],
                          'canvas': canvas,
                          'type': fractal,
                          'modified': modified,
                          'iteration': iteration}, sort_keys=True, indent=2, separators=(',', ': '))
    # List comprehension, effective way of getting all coords and color in one loop.

    return ser_val


def create_music_json(file):
    ser_val = json.dumps({'mode': "music", 'content': file}, sort_keys=True, indent=2, separators=(',', ': '))
    return ser_val


def create_translation_json(lines, canvas):
    ser_val = json.dumps({'mode': "translation",
                          'canvas': canvas,
                          'lines': [{'coordinate1': serialize_coords(line.coordinate_1),
                                     'coordinate2': serialize_coords(line.coordinate_2),
                                     'color': line.color
                                     } for line in lines]}, sort_keys=True, indent=2, separators=(',', ': '))
    return ser_val
