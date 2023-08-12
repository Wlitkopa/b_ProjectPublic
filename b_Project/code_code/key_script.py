
from abc import ABC, abstractmethod
import functools
import operator
import random


# Code extracting key from text file using mask. Mask elements indicate indexes of letters in relative words, which are key letters


# Function extracting given letter out of specific word
def pick_up(tuple_w: tuple):  
    if tuple_w[0] is None:
        return ""
    else:
        return tuple_w[1][tuple_w[0]].lower()


 # Function generating random masks
def random_int(word: str):
    wl = len(word)
    ran = random.randint(0, (wl - 1))
    op = random.randint(0, 100)
    if op <= 70:  # "70" value indicates the percentage of None values in mask, that indicates that given word should not be taken into
        ran = None # consideration in key letters extracting process
    return ran


class Key_plan(ABC):

    @staticmethod
    @abstractmethod
    def mapping(file: str, map_list: list) -> str:
        pass


class Key(Key_plan):

    # Method mapping mask on a text file given as an input
    @staticmethod
    def mapping(file: str, map_list: list) -> str:  
        if file != "empty_file.txt":
            print("This file doesn't exist")
            exit()
        try:
            output = str(functools.reduce(operator.concat, list(
                pick_up(tuple_z) for tuple_z in zip(map_list, filter(
                    lambda x: x, functools.reduce(
                        operator.concat, (line.split(" ") for line in functools.reduce(operator.concat,
                                                                                       (line2.split('\n') for line2 in
                                                                                        open(f"{file}", "r")))
                                          )
                    )
                )
                )
            )
            )
            )

        except TypeError:
            output = ""

        print(f'Mapping:\n\n{output}\n')
        return


    # Method generating sample masks
    @staticmethod
    def generate_mask(file: str) -> list:
        some_mask = list(
            random_int(word) for word in filter(
                lambda x: x, functools.reduce(
                    operator.concat, (line.split(" ") for line in functools.reduce(operator.concat,
                                                                                   (line2.split('\n') for line2 in
                                                                                    open(f"{file}", "r")))
                                      )
                )
            )
        )
        return some_mask

