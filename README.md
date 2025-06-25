![GitHub last commit](https://img.shields.io/github/last-commit/WishlPromt/Media-Converter)

# Media Converter

**Python** project that helps convert media for **Telegram stickers**.<br />
It's use ffmpeg for convert

## How to use
1. Put files that need to convert in /inputs directory
2. Run main.py from /src directory

> [!WARNING]
> Install libraries from requirements.txt for converter to work

## Optional parameters
> [!NOTE]
> By default parameters correspond to the requirements of Telegram stickers (they are described in /configs/defaults.toml, you can change it), but if you need, you can to specify them while running the main file.

### 1. Scale
- `--scale_x` `-sx` - changes width of the media (512 by default) 
- `--scale_y` `-sy` - changes height of the media (-1(auto) by default)
- `--vertical_orientation` `-vo` - swaps width and height
- `--original_scale` `-os` - don't change scale (don't need in value)
### 2. Output
- `--output_format` `-of` - changes output media format (.webm by default)
- `--codec` `-c` - changes codec for encoding media (libvpx-vp9 by default)
- `--rate` `-r` - changes framerate of media (30 by default)
### 3. Duration (for videos)
- `--seek_start` `-ss` - sets the time at which the output media will start (00:00:00 by default)
- `--to` `-t` - sets the time at which the output media will end (00:00:03 by default)

### 4. Text
- `--text` `-t` - text to be added (none by default)
- `--text_x` `-tx` - text x position (256 by default)
- `--text_y` `-ty` - text y position (256 by default)
- `--font_size` `-fs` - size of font (36 by default)
- `--font_color` `-fc` - color of font (white by default)
- `--font_file` `-ff` - path to font file (NotoSans-Regular.ttf by default)

> [!NOTE]
> Program gets fonts from /fonts directory

## Tasks
- [x] - Convertation
- [ ] - Edit optional parameters
- [ ] - building .exe file script
- [ ] - Add GUI ?
