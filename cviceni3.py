def my_range(start,stop, step=1):

    #nbase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range

    result = []
    hodnota = start
    while hodnota < stop:
        result.append(hodnota)
        hodnota += step
    return result    

def for_emurate(iterable, start=0):

    #nase vlastni implementace enumerate()

    result = []

    index = start
    for prvek in iterable:
        result.append((index, prvek))
        index += 1


    return result

def while_enumerate(iterable, start=0 ):
    result = []
    index = 0
    while index < len(iterable):
        result.append((index, iterable[index]))
        index += 1 
        start += 1

    return result

if __name__ == "__main__":

    print(list(enumerate(["Alice", "Bob", "Eva"], 100)))
    print(for_emurate(["Alice", "Bob", "Eva"], 100))
    print(while_enumerate(["Alice", "Bob", "Eva"], 100))