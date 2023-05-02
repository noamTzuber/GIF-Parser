from typing import Any

from gif_objects import Gif, Image


def color_table_processes(gif: Gif):
    new_structure: list[Any] = []

    for i in range(len(gif.structure)):
        block = gif.structure[i]
        if isinstance(block, Image):
            if block.local_color_table_flag:
                new_structure.append(gif.structure[i + 1])
            else:
                new_structure.append(gif.global_color_table)
            new_structure.append(block)
        else:
            new_structure.append(block)

    gif.structure = new_structure
