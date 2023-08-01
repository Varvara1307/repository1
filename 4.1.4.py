def palindrom(s):
    counter_for_ops = 0
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
        counter_for_ops += 1
    counter2 = 0
    for sym in s:
        if syms_counter[sym] == 2:
            counter2 += 1
    if syms_counter == counter2:
        print('True')
    else:
        print('False')

palindrom('abllba')