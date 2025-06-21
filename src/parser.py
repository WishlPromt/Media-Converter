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

parser.add_argument('-sx', '--scale_x', type=int, default=config['scale_x'])
parser.add_argument('-sy', '--scale_y', type=int, default=config['scale_y'])
parser.add_argument('-vo', '--vertical_orientation', action='store_true')
parser.add_argument('-os', '--original_scale', action='store_true')
parser.add_argument('-of', '--output_format', type=str, default=config['output_format'])
parser.add_argument('-c', '--codec', type=str, default=config['codec'])
parser.add_argument('-r', '--rate', type=int, default=config['rate'])
parser.add_argument('-ss', '--seek_start', type=str, default=config['seek_start'])
parser.add_argument('-to', '--to', type=str, default=config['to'])

parser.add_argument('-t', '--text', type=str, default='')
parser.add_argument('-tx', '--text_x', type=float, default=config['text_x'])
parser.add_argument('-ty', '--text_y', type=float, default=config['text_y'])
parser.add_argument('-fs', '--font_size', type=float, default=config['font_size'])
parser.add_argument('-fc', '--font_color', type=str, default=config['font_color'])
parser.add_argument('-ff', '--font_file', type=str, default=config['font_file'])
