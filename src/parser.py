import argparse
import tomllib
import os

root_dir = os.getcwd()

with open(f'{root_dir}/configs/defaults.toml', 'rb') as f:
    config = tomllib.load(f)

parser = argparse.ArgumentParser(
    prog='mconverter',
    description='Media Converter that i use to create telegram stickers'
)

parser.add_argument('-sx', '--scale_x', type=int, default=config['scale_x'], help="changes width of the media")
parser.add_argument('-sy', '--scale_y', type=int, default=config['scale_y'], help="changes height of the media")
parser.add_argument('-vo', '--vertical_orientation', action='store_true', help="swaps width and height")
parser.add_argument('-os', '--original_scale', action='store_true', help="don't change scale")
parser.add_argument('-of', '--output_format', type=str, default=config['output_format'], help="changes output media format")
parser.add_argument('-c', '--codec', type=str, default=config['codec'], help="changes codec for encoding media")
parser.add_argument('-r', '--rate', type=int, default=config['rate'], help="changes framerate of media")
parser.add_argument('-vb', '--video_bitrate', type=str, default=config['video_bitrate'], help="changes bitrate of media video track")
parser.add_argument('-ss', '--seek_start', type=str, default=config['seek_start'], help="sets the time at which the output media will start")
parser.add_argument('-d', '--duration', type=str, default=config['duration'], help="sets the max duration of the video")

parser.add_argument('-t', '--text', type=str, default='', help="text to be added")
parser.add_argument('-tx', '--text_x', type=float, default=config['text_x'], help="text x position")
parser.add_argument('-ty', '--text_y', type=float, default=config['text_y'], help="text y position")
parser.add_argument('-fs', '--font_size', type=float, default=config['font_size'], help="size of font")
parser.add_argument('-fc', '--font_color', type=str, default=config['font_color'], help="color of font")
parser.add_argument('-ff', '--font_file', type=str, default=config['font_file'], help="path to font file")
