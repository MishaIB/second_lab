import csv


class iterator:
<<<<<<< HEAD
    def __init__(self, file_name, mark)->None:
=======
    def __init__(self, file_name, mark):
>>>>>>> 9d865f6748297b743a2f4bdb78f255f70a0caac8
        self.limit = -1
        self.counter = -1
        self.file_name = file_name
        self.subdir = mark
        self.mass = []
        with open(file_name, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if row[2] == mark:
                    self.mass.append(row[0] + ';' + row[2])
                    self.limit += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.mass[self.counter]
        else:
            print('Нет')
            raise StopIteration
