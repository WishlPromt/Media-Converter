import ffmpeg
import os

def main(scale: list = [512, 512],
         output_folder: str = "outputs",
         framerate: int = 30,
         codec: str = "libvpx-vp9",
         ss: str = "00:00:00",
         to: str = "00:00:03"):

    for file in os.listdir("media/inputs/"):
        if file == '.gitkeep': continue

        print(file.split('.')[0])
        try:
            input = ffmpeg.input(f"media/inputs/{file}",
                                 ss=ss,
                                 to=to,
                                 )

            output = (input
                      .filter("scale", scale[0], -1)
                      .output(f"media/{output_folder}/{file.split('.')[0]}.webm",
                              r=framerate,
                              vcodec=codec,
                              **{
                                  "b:v": "500K",
                                  "maxrate": "500K"
                              }
                              )
                      )

            output.run(overwrite_output=True)
        except ffmpeg.Error as e:
            print("STDOUT: ", e.stdout)
            print("STDERR: ", e.stderr)


def add_text(input, text: str):
    input.filter("drawtext",
          text=text,
          x=32,
          y=450,
          fontsize=48,
          fontcolor="white"
          )

    return input


if __name__ == "__main__":
    main()
    