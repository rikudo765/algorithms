"""
Реалізуйте інтерфейс для роботи з англійсько-українським словником та швидким пошуком перекладу.
"""

lst = []


def addTranslation(eng, translation):
    """ Додає до словника англійське слово та його переклад.
    Пари (eng, translation) приходяться у порядку, що відповідає лексикографічному порядку.
    :param eng: англійське слово
    :param translation: переклад
    """
    lst.append((eng, translation))


def find(eng):
    """ Повертає переклад слова зі словника.
    :param eng: англійське слово
    :return: переклад слова, якщо воно міститься у словнику, або порожній рядок у іншому разі.
    """
    l = 0
    r = len(lst)
    while r != l + 1:
        t = l + (r - l) // 2
        if lst[t][0].strip().lower() >= eng.strip().lower():
            r = t
        else:
            l = t
    trans = ""
    # if r!=len(lst):
    #     if lst[r][0]==eng:
    #         trans=lst[r][1]
    try:
        if lst[r][0] == eng:
            trans = lst[r][1]
    except IndexError:
        pass
    if lst[l][0] == eng:
        trans = lst[l][1]

    return trans
