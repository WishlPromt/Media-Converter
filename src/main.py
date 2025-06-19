import ffmpeg
import os
import filetype

from parser import parser
from media import MediaParams, Media

def check_filetype(file_path: str):
    ext = filetype.guess(file_path)

    if ext is None:
        return False
    elif ext.mime.startswith('video/'):
        return 'video'
    elif ext.mime.startswith('image/'):
        return 'image'
    else:
        return False

def main(params: MediaParams):
    root_dir = os.getcwd()

    for file in os.listdir(f'{root_dir}/media/inputs'):
        if file == '.gitkeep': continue

        filepath = f'{root_dir}/media/inputs/{file}'

        print(file.split('.')[0])

        type_of_file = check_filetype(filepath)
        if type_of_file:
            media = Media(params, file, filepath, root_dir)
            match type_of_file:
                case 'video':
                    convert_media(media, ffmpeg.input(media.filepath,
                                                      ss=media.params.ss,
                                                      to=media.params.to))
                case 'image':
                    convert_media(media, ffmpeg.input(media.filepath))


def convert_media(media: Media, input: ffmpeg.nodes.FilterableStream):
    try:
        if media.params.text != None:
            input = media.params.text.add_text(input, media.root_dir)

        output = (input
                  .filter('scale', media.params.scale[0], media.params.scale[1])
                  .output(f'{media.root_dir}/media/outputs/{media.filename.split(".")[0]}.{media.params.output_format}',
                          **{
                              'q:v': '5'
                          })
                  )

        output.run(overwrite_output=True)
    except ffmpeg.Error as e:
        print('STDOUT: ', e.stdout)
        print('STDERR: ', e.stderr)


def add_text(input, text: str, root_dir: str):
    return input.filter('drawtext',
                        text=text,
                        x=200,
                        y=200,
                        fontsize=48,
                        fontcolor='white',
                        fontfile=f'{root_dir}/fonts/NotoSans-Regular.ttf'
                        )


if __name__ == '__main__':
    args = parser.parse_args()

    main(MediaParams(args))
    