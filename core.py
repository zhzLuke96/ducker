from random import choice

__all__ = ("reply",)

lang_collection = []
with open("./dict.txt", "r", encoding="utf-8") as f:
    lang_collection = f.read().split("\n")


def reply(input=""):
    return choice(lang_collection)


def read_oneLine(prompt="  >> "):
    try:
        exp = input(prompt)
        print("$ >>", reply(exp))
    except KeyboardInterrupt as e:
        if isinstance(e, KeyboardInterrupt):
            exit()
    finally:
        pass


def repl():
    while True:
        read_oneLine()


if __name__ == '__main__':
    repl()
