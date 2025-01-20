def doTask(task, value):
    task(value)


def print5(value):
    for i in range(5):
        print(value)


doTask(print, 100)
doTask(print5, 'Hello')


