"""utility module for the CIFAR-10 dataset
   Brian Lawrence"""

import numpy as np


class CiFar10Classes:
    """Class of the 10 classes of CIFAR-10"""
    AIRPLANE = "Airplane"
    AUTOMOBILE = "Automobile"
    BIRD = "Bird"
    CAT = "Cat"
    DEER = "Deer"
    DOG = "Dog"
    FROG = "Frog"
    HORSE = "Horse"
    SHIP = "Ship"
    TRUCK = "Truck"


class CiFarClassTracker:
    """ Thread safe way to track if we have generated all the cifar10 classes
     - optimize the creation!"""

    def __init__(self):
        # define a 2d array containing the classtype and boolean value
        self.data = np.array([class_type_values_in_array(), [False]*10])

    # method on the class
    def state(self):
        """the current state of this class tracker"""
        print(self.data)
        print(self.found_all())

    def found_all(self):
        """returns true if all class types have been found (by using addClass)"""
        for i in range(len(self.data[0])):
            if self.data[1][i] == "False":
                return False
        return True

    def add_class(self, class_name):
        """passes the name of a class and if found, makes corresponding boolean value true & returns value"""
        for i in range(len(self.data[0])):
            if self.data[0][i] == class_name:
                if self.data[1][i] != "True":
                    self.data[1][i] = True
                    return True
        return False


def class_type_values_in_array():
    """return CIFAR-10 class types in a string array"""
    return [
        CiFar10Classes.AIRPLANE,
        CiFar10Classes.AUTOMOBILE,
        CiFar10Classes.BIRD,
        CiFar10Classes.CAT,
        CiFar10Classes.DEER,
        CiFar10Classes.DOG,
        CiFar10Classes.FROG,
        CiFar10Classes.HORSE,
        CiFar10Classes.SHIP,
        CiFar10Classes.TRUCK
    ]


def human_readable_result(result):
    """returns human readable CIFAR-10 classname"""
    if result[0][0]:
        return CiFar10Classes.AIRPLANE
    elif result[0][1]:
        return CiFar10Classes.AUTOMOBILE
    elif result[0][2]:
        return CiFar10Classes.BIRD
    elif result[0][3]:
        return CiFar10Classes.CAT
    elif result[0][4]:
        return CiFar10Classes.DEER
    elif result[0][5]:
        return CiFar10Classes.DOG
    elif result[0][6]:
        return CiFar10Classes.FROG
    elif result[0][7]:
        return CiFar10Classes.HORSE
    elif result[0][8]:
        return CiFar10Classes.SHIP
    elif result[0][9]:
        return CiFar10Classes.TRUCK
    else:
        return 'Error'
