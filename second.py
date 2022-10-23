import os
import get_way
import shutil

#копирование в другую директорию
def copy_to_another(class_name):
    for i in range(1020):
        if (os.path.isfile(get_way.get_absolute_way(class_name, i, "download")) == True ):
            shutil.copyfile(get_way.get_absolute_way(class_name, i, "download"), get_way.get_absolute_way(class_name, i, "changed"))



def main():
        print("Начало")
        if not os.path.isdir("dataset/changed_dataset"):
            os.makedirs("dataset/changed_dataset")
        class_name = "cat"
        copy_to_another(class_name)
        class_name = "dog"
        copy_to_another(class_name)
        print("Конец")
    
if __name__ == "__main__":
        main()