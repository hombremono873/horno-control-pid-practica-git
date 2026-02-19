import winsound
def alarma_impulso(hay_impulso):
    if hay_impulso:
        winsound.Beep(1000, 300)  # 1000 Hz durante 300 ms