import gif_objects
from decoder import decode_gif, decode_image_data, decode_local_color_table


def main():
    with open("example.gif", "rb") as gif_file:
        gif = decode_gif(gif_file)

    print(gif)


if __name__ == '__main__':
    main()
