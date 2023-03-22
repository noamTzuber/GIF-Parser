import gif_objects
from decoder import decode_gif, decode_image_data, decode_local_color_table


def main():
    with open("example.gif", "rb") as gif_file:
        decode_gif(gif_file)


if __name__ == '__main__':
    # main()
    gif = gif_objects.Gif()
    with open("example.gif", "rb") as file:
        # testing for image descriptor
        file.read(34)
        decode_image_data(file, gif)

        # testing for read image data
        file.read(43)
        decode_image_data(file, gif)

        # tests for local color table
        # file.read(13)
        # decode_local_color_table(file, gif)
    pass