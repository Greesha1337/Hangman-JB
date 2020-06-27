def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    return 5 + 5 * (x // 5)
