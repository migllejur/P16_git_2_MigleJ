def kaupk_aritmetika(*args, operacija="suma"):
    if len(args) < 2:
        return args
    if operacija == "daugyba":
        rezultatas = 1
        for nr in args:
            rezultatas *= nr
    elif operacija == "dalyba":
        rezultatas = args[0]
        for nr in args[1:]:
            if nr == 0:
                return False
            rezultatas /= nr
    elif operacija == "suma":
        rezultatas = sum(args)
    elif operacija == "atimtis":
        rezultatas = args[0]
        for nr in args[1:]:
            rezultatas -= nr
    else:
        return None
    return rezultatas