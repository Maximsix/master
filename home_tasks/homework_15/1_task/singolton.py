from typing import Type


def singleton(_class: Type):
    def inner(*args,):
        if not hasattr(_class, "__instance"):
            setattr(_class, "__instance", _class(*args))
        return getattr(_class, "__instance")

    return inner


# well nice but instance not a private. All private attributes has name of class in names -3 points
