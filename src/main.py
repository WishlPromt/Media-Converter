import ffmpeg
import os

from parser import parser

def main(scale: list,
         output_folder: str,
         framerate: int,
         codec: str,
         ss: str,
         to: str):

    root_dir = os.getcwd()

    for file in os.listdir(f'{root_dir}/media/inputs'):
        if file == '.gitkeep': continue

        print(file.split('.')[0])
        try:
            input = ffmpeg.input(f'{root_dir}/media/inputs/{file}',
                                 ss=ss,
                                 to=to,
                                 )

            output = (input
                      .filter('scale', scale[0], -1)
                      .output(f'{root_dir}/media/{output_folder}/{file.split(".")[0]}.webm',
                              r=framerate,
                              vcodec=codec,
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
            args.scale_y],
         output_folder=args.output_folder,
         codec=args.codec,
         framerate=args.framerate,
         ss=args.start_from,
         to=args.end
         )
    