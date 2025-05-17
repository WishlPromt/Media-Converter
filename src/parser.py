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
parser.add_argument('-os', '--original_scale', action='store_true')
parser.add_argument('-of', '--output_format', type=str, default=config['output_format'])
parser.add_argument('-c', '--codec', type=str, default=config['codec'])
parser.add_argument('-fr', '--framerate', type=int, default=config['framerate'])
parser.add_argument('-sf', '--start_from', type=str, default=config['start_from'])
parser.add_argument('-e', '--end', type=str, default=config['end'])
