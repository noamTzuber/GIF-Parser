# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import classes
from decoder import decode_image_descriptor, decode_image_data


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gif = classes.Gif()
    with open("example.gif", "rb") as file:
        # testing for read image data
        # file.read(43)
        # decode_image_data(file, gif)

        # testing for image descriptor
        # file.read(34)
        # decode_image_descriptor(file, gif)

        pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
