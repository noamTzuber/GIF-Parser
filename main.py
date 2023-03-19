from decoder import decode_gif


def main():
    with open("example.gif", "rb") as gif_file:
        decode_gif(gif_file)


if __name__ == '__main__':
    main()
