import argparse
import ffmpeg

class Text:
    text: str
    pos_x: float
    pos_y: float
    font_size: float
    font_color: str
    font_file: str

    def __init__(self, text: str, pos_x: float, pos_y: float, font_size: float, font_color: str, font_file: str):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.font_size = font_size
        self.font_color = font_color
        self.font_file = font_file

    def add_text(self, media_input: ffmpeg.nodes.FilterableStream, root_dir: str):
        print('create text')
        return media_input.filter('drawtext',
                                  text=self.text,
                                  x=self.pos_x,
                                  y=self.pos_y,
                                  fontsize=self.font_size,
                                  fontcolor=self.font_color,
                                  fontfile=f'{root_dir}/fonts/{self.font_file}'
                                  )


class MediaParams:
    scale: list[int]
    output_format: str
    rate: int
    codec: str
    ss: str
    to: str

    text: Text = None

    def __init__(self, args: argparse.Namespace):
        self.scale = ([args.scale_x, args.scale_y] if not args.vertical_orientation
                      else [args.scale_y, args.scale_x])\
            if not args.original_scale else [-1, -1]
        print(self.scale)
        self.output_format = args.output_format
        self.codec = args.codec
        self.rate = args.rate
        self.ss = args.seek_start
        self.to = args.to

        if args.text != '':
            print('text added')
            self.text = Text(
                args.text,
                args.text_x,
                args.text_y,
                args.font_size,
                args.font_color,
                args.font_file
            )


class Media:
    params: MediaParams
    filename: str
    filepath: str
    root_dir: str

    def __init__(self, params: MediaParams, filename: str, filepath: str, root_dir: str):
        self.params = params
        self.filename = filename
        self.filepath = filepath
        self.root_dir = root_dir