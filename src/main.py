import ffmpeg
import os
import filetype

from parser import parser

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

def main(scale,
         output_format: str,
         framerate: int,
         codec: str,
         ss: str,
         to: str):

    if not scale:
        scale = [-1, -1]
    root_dir = os.getcwd()

    for file in os.listdir(f'{root_dir}/media/inputs'):
        if file == '.gitkeep': continue

        filepath = f'{root_dir}/media/inputs/{file}'

        print(file.split('.')[0])

        type_of_file = check_filetype(filepath)
        if type_of_file:
            match type_of_file:
                case 'video':
                    convert_video(
                        filepath=filepath,
                        ss=ss,
                        to=to,
                        scale_x=scale[0],
                        scale_y=scale[1],
                        root_dir=root_dir,
                        file=file,
                        output_format=output_format,
                        framerate=framerate,
                        codec=codec
                    )
                case 'image':
                    convert_image(filepath=filepath,
                                  scale_x=scale[0],
                                  scale_y=scale[1],
                                  output_format=output_format,
                                  file=file,
                                  root_dir=root_dir
                                  )




def convert_video(**params):

    try:
        input = ffmpeg.input(params['filepath'],
                             ss=params['ss'],
                             to=params['to'],
                             )

        output = (input
                  .filter('scale', params['scale_x'], params['scale_y'])
                  .output(f'{params['root_dir']}/media/outputs/{params['file'].split(".")[0]}.{params['output_format']}',
                          r=params['framerate'],
                          vcodec=params['codec'],
                          **{
                              'b:v': '500K',
                              'maxrate': '500K'
                          }
                          )
                  )

        output.run(overwrite_output=True)
    except ffmpeg.Error as e:
        print('STDOUT: ', e.stdout)
        print('STDERR: ', e.stderr)


def convert_image(**params):
    try:
        input = ffmpeg.input(params['filepath'])

        output = (input
                  .filter('scale', params['scale_x'], params['scale_y'])
                  .output(f'{params['root_dir']}/media/outputs/{params['file'].split(".")[0]}.{params['output_format']}',
                          **{
                              'q:v': '5'
                          })
                  )

        output.run(overwrite_output=True)
    except ffmpeg.Error as e:
        print('STDOUT: ', e.stdout)
        print('STDERR: ', e.stderr)


def add_text(input, text: str):
    input.filter('drawtext',
          text=text,
          x=32,
          y=450,
          fontsize=48,
          fontcolor='white'
          )

    return input


if __name__ == '__main__':
    args = parser.parse_args()
    main(
        scale=[
            args.scale_x,
            args.scale_y] if not args.original_scale else False,
         output_format=args.output_format,
         codec=args.codec,
         framerate=args.framerate,
         ss=args.start_from,
         to=args.end
         )
    