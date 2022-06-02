# utility module for the CIFAR-10 dataset
# Brian Lawrence

class CiFar10Classes:
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
