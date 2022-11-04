import os


def relative_way_dataset(subdir:str, number:int)->str:
    """функция возвращая путь из dataset скаченной картинки

    Args:
        subdir (str): название подкаталога(класса)
        number (int): номер картинки

    Returns:
        str:  возвращает путь картинки из dataset 
    """
    return f"dataset/{subdir}/{str(number).zfill(4)}.jpg"


#относительный путь для 2 скрипта
def relative_way_changed(subdir:str, number:int)->str:
    """функция создает и возвращает относительный путь для новой директории картинки

    Args:
        subdir (str): название подкаталога(класса)
        number (int): новыц номер картинки

    Returns:
        str: возвращает новый относительный путь для новой директории картинки
    """
    return f"dataset/changed_dataset/{subdir}_{str(number).zfill(4)}.jpg"


#относительный путь для рандомного
def relative_way_random(number)->str:
    """функция создает и возвращает относительный путь для новой директории картинки

    Args:
        number (_type_): новый номер картинки

    Returns:
        str: возвращает новый относительный путь для новой директории картинки
    """
    return f"dataset/random_dataset/{str(number).zfill(4)}.jpg"


<<<<<<< HEAD
def get_absolute_way(subdir:str, number:int, function:str)->str:
    """функция возвращает абсолютный путь для картинки

    Args:
        subdir (str): название подкаталога(класса)
        number (int): новый номер
        function (str): название функции

    Returns:
        str: _description_
    """
=======
def get_absolute_way(subdir, number, function):
>>>>>>> 9d865f6748297b743a2f4bdb78f255f70a0caac8
    if function == "download":
        return os.path.abspath(relative_way_dataset(subdir, number))
    if function == "changed":
        return os.path.abspath(relative_way_changed(subdir, number))
    if function == "random":
        return os.path.abspath(relative_way_random(number))