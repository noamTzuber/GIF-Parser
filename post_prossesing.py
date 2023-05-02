from typing import Any

from gif_objects import Gif, Image


def color_table_processes(gif: Gif):
    new_structure: list[Any] = []

    i = 0
    while i < len(gif.structure):
        block = gif.structure[i]
        if isinstance(block, Image):
            if block.local_color_table_flag:
                block.local_colo_table = gif.structure[i + 1]
                i += 1
            else:
                block.local_colo_table = gif.global_color_table
            new_structure.append(block)
        else:
            new_structure.append(block)
        i += 1

    gif.structure = new_structure
