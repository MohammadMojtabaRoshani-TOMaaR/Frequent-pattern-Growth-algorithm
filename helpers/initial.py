import sys
from collections import Counter
from termcolor import colored
from tabulate import tabulate


def initial_program():
    n = len(sys.argv)
    if n < 3:
        print(colored("ERROR> missing value, support and confident are required", "red"))
        exit(-1)


def supp_and_conf():
    _support = int(sys.argv[1])
    _confidence = int(sys.argv[2])
    print(colored("Info> support: {} and confidence: {} are defined".format(_support, _confidence), "blue"))
    return _support, _confidence


def input_by_user():
    print(colored("Pattern> M O N K E Y", "yellow"))
    print(colored("Pattern> D O N K E Y", "yellow"))
    print(colored("Pattern> M A K E", "yellow"))
    print(colored("Pattern> *", "yellow"))
    print(colored("Info> Input the sets like the upper patter and at the end enter *", "blue"))

    _flag = True
    _item_sets = []

    while (_flag):
        user_input = input()
        if user_input == '*':
            _flag = False
            break
        _item_sets.append(
            [x for x in user_input.split(" ") if x != ""]
        )

    return _item_sets


def frequent_item_sets_by_length_one(_items, _support):
    _one_length_items = []
    _one_length_result = []
    _one_length_frequent = []

    for i_item in _items:
        for j_item in i_item:
            _one_length_items.append(j_item)

    for item in _one_length_items:
        if _one_length_items.count(item) >= _support:
            _one_length_result.append(item)

    counter = Counter(_one_length_result)
    _one_length_result = [x for x in counter.keys()]
    _one_length_frequent = [x for x in counter.values()]

    print(colored("Info> Your first item set: {} frequency is: {}".format(_one_length_result, _one_length_frequent),
                  "blue"))

    return _one_length_result,_one_length_frequent

def remove_non_frequent_items(_item_set,_frequent_item):

    _final_result = []

    for i_item in _item_set:
        _temp_values = []
        for j_item in i_item:
            if j_item in _frequent_item:
                _temp_values.append(j_item)
        _final_result.append(_temp_values)

    _table = tabulate({"Item": _final_result}, headers="keys", showindex="always",tablefmt="simple")

    print(colored(
        "Info> Table of frequents set:\n","blue"
        ),
        _table
    )

    return _final_result
