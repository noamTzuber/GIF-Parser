from decoder import decode


def main():
    with open("example.gif", "rb") as gif_file:
        decode(gif_file)


if __name__ == '__main__':
    main()
