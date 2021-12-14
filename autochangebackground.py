#!/usr/bin/env python
import os, glob, random
import _thread


def gen_random_num(start, end):
    return random.randrange(start, end)


def is_safe(number, without):
    for val in without:
        if val == number:
            return False

    return True


def get_lost_elem(count, val_list):
    ss_list = []
    for i in range(0, count):
        ss_list.append(i)

    for i in val_list:
        ss_list.remove(i)

    return ss_list[0]


def gen_random_list(count, without=None):
    if without is None:
        without = []
    while True:

        number = gen_random_num(0, count - 1)

        if len(without) + 1 == count:
            without.append(get_lost_elem(count, without))
            return without

        if not is_safe(number, without):
            continue

        without.append(number)


def change_background(PATH_TO_PICTURE):
    os.system('gsettings set org.gnome.desktop.background picture-uri file://' + PATH_TO_PICTURE)


paused = False


def thread_change_background():
    file_list = []

    for file in glob.glob("*.jpg"):
        file_list.append(os.environ['PWD'] + '/' + file)

    access_list = gen_random_list(len(file_list))

    while True:
        for i in access_list:
            print('\nchange background to file://' + file_list[i])
            change_background(file_list[i])
            os.system('sleep 10')

            while paused:
                os.system('sleep 1')


_thread.start_new_thread(thread_change_background, ())

while True:
    cmd = input("Pybkg> ")

    if cmd == 'exit':
        print('Exiting...')
        exit(0)

    elif cmd == 'pause':
        paused = True
        print('Thread paused')

    elif cmd == 'unpause':
        paused = False
        print('Thread un-paused')

    else:
        print('Unknown command!')

