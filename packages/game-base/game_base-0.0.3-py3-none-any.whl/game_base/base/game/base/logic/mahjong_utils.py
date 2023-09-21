def get_card_value(card):
    r"""
     获取牌的值
    :param card:牌
    :return:
    """
    return card % 10


def get_card_color(card):
    r"""
     获取牌的花色
    :param card:牌
    :return:
    """
    return card / 10


def is_same_color(cards):
    r"""
    :是否有相同花色的牌
    :param cards: 所有牌
    :return bool
    """
    _values = []
    for _card in cards:
        _values.append(get_card_color(_card))
    _values = sorted(_values)
    return _values[0] == _values[len(_values) - 1]


def possible(handlist, degree):
    """
    :可能的牌
    :param handlist:
    :param degree:
    :return:
    """
    possible_list = set()
    for s in handlist:
        possible_list.add(s)
        for i in range(0, degree):
            if (s % 10) + i + 1 < 10:
                possible_list.add(s + i + 1)
            if (s % 10) - i - 1 > 0:
                possible_list.add(s - i - 1)
    return possible_list


def has_same_cards(cards, count):
    r"""
    :是否有相同值的牌
    :param cards: 所有牌
    :param count: 要找的个数 > 1
    :return bool
    """
    _values = sorted(cards)
    for i in range(len(cards) - count):
        if _values[i] == _values[i + count]:
            return True
    return False


def find_same_cards(cards, card, count):
    r"""
    :是否有相同值的牌
    :param cards: 所有牌
    :param card: 要找的牌
    :param count: 要找的个数 > 1
    :return bool
    """
    _values = sorted(cards)
    for i in range(len(cards) - count):
        if _values[i] == card and _values[i] == _values[i + count]:
            return _values[i:i + count]
    return None


def contain_size(cardlist, card):
    """
    :包含数量
    :param cardlist:
    :param card:
    :return:
    """
    size = 0
    for c in cardlist:
        if c == card:
            size += 1
    return size


def get_cards_by_count(cards, count):
    r"""
    :是否有相同值的牌
    :param cards: 所有牌
    :param count: 要找的个数 > 1
    :return bool
    """
    count_cards = set()
    _values = sorted(cards)
    for i in range(len(cards) - count):
        if _values[i] == _values[i + count - 1]:
            count_cards.add(_values[i])
            i += count - 1
    return list(count_cards)


def check_lug(handlist):
    """
    :胡牌规则
    :param handlist:
    :return:
    """
    if 0 == len(handlist):
        return True
    temp = list()
    temp.extend(handlist)
    md_val = temp[0]
    temp.remove(md_val)
    if 2 == contain_size(temp, md_val):
        temp_same = list()
        temp_same.extend(temp)
        temp_same.remove(md_val)
        temp_same.remove(md_val)
        if check_lug(temp_same):
            return True
    if md_val + 1 in temp and md_val + 2 in temp:
        temp_shun = list()
        temp_shun.extend(temp)
        temp_shun.remove(md_val + 1)
        temp_shun.remove(md_val + 2)
        if check_lug(temp_shun):
            return True
    return False


def check_lug_rogue(handlist, rogue_count):
    """
    :胡牌规则
    :param handlist:
    :param rogue_count:
    :return:
    """
    if 0 == len(handlist):
        return True
    if 0 == rogue_count:
        return check_lug(handlist)
    temp = list()
    temp.extend(handlist)
    md_val = temp[0]
    temp.remove(md_val)
    if 2 == contain_size(temp, md_val):
        temp_same = list()
        temp_same.extend(temp)
        temp_same.remove(md_val)
        temp_same.remove(md_val)
        if check_lug_rogue(temp_same, rogue_count):
            return True
    if md_val + 1 in temp and md_val + 2 in temp:
        temp_shun = list()
        temp_shun.extend(temp)
        temp_shun.remove(md_val + 1)
        temp_shun.remove(md_val + 2)
        if check_lug_rogue(temp_shun, rogue_count):
            return True
    if rogue_count > 0:
        if 1 == contain_size(temp, md_val):
            temp_same = list()
            temp_same.extend(temp)
            temp_same.remove(md_val)
            if check_lug_rogue(temp_same, rogue_count - 1):
                return True
        if md_val + 1 in temp:
            temp_same = list()
            temp_same.extend(temp)
            temp_same.remove(md_val + 1)
            if check_lug_rogue(temp_same, rogue_count - 1):
                return True
        if md_val + 2 in temp and md_val % 10 != 9:
            temp_same = list()
            temp_same.extend(temp)
            temp_same.remove(md_val + 2)
            if check_lug_rogue(temp_same, rogue_count - 1):
                return True
        if 1 < rogue_count:
            if check_lug_rogue(temp, rogue_count - 2):
                return True
    return False


def get_hu(handlist, rogue):
    """
    :胡牌规则
    :param handlist:
    :param rogue:
    :return:
    """
    hu = set()
    rogue_size = contain_size(handlist, rogue)

    if rogue_size > 0:
        temp = list()
        temp.extend(handlist)
        temp.append(-1)
        if -1 != double7(temp, rogue):
            hu.add(-1)
            return hu
        temp.remove(-1)
        temp.remove(rogue)
        for i in range(0, rogue_size - 1):
            temp.remove(rogue)
        temp = sorted(temp)
        if check_lug_rogue(temp, rogue_size - 1):
            hu.add(-1)
            return hu
    possible_cards = possible(handlist, rogue_size + 1)
    for p in possible_cards:
        temp = list()
        temp.extend(handlist)
        temp.append(p)
        if -1 != double7(temp, rogue):
            hu.add(p)
        for i in range(0, rogue_size):
            temp.remove(rogue)
        tempset = set(temp)
        for s in tempset:
            if 1 != contain_size(temp, s):
                hutemp = list()
                hutemp.extend(temp)
                hutemp.remove(s)
                hutemp.remove(s)
                hutemp = sorted(hutemp)
                if check_lug_rogue(hutemp, rogue_size):
                    hu.add(p)
                    break
            if rogue_size > 0:
                hutemp = list()
                hutemp.extend(temp)
                hutemp.remove(s)
                hutemp = sorted(hutemp)
                if check_lug_rogue(hutemp, rogue_size - 1):
                    hu.add(p)
                    break
        temp.remove(p)
    return hu


def double7(handlist, rogue):
    """
    :七对
    :param handlist: 手牌
    :param rogue: 癞子牌
    :return: -1 不是7对 7对的跟数
    """
    temp = list()
    temp.extend(handlist)
    rogue_size = contain_size(handlist, rogue)
    for i in range(0, rogue_size):
        temp.remove(rogue)
    si = get_cards_by_count(temp, 4)
    dui = get_cards_by_count(temp, 2)
    if 14 == len(handlist) and 14 - (2 * (len(dui) + len(si))) <= 2 * rogue_size:
        si_count = 0
        temp1 = list()
        temp1.extend(temp)
        for i in range(0, 4):
            for s in si:
                temp1.remove(s)
        si_count += len(si)
        san = get_cards_by_count(temp1, 3)
        for i in range(0, 3):
            for s in san:
                temp1.remove(s)
        si_count += len(san)
        rogue_size -= len(san)
        dui = get_cards_by_count(temp1, 2)
        for i in range(0, 2):
            for s in dui:
                temp1.remove(s)
        rogue_size -= len(temp1)
        if rogue_size / 2 > len(dui):
            si_count += len(dui)
            rogue_size -= 2 * len(dui)
            si_count += rogue_size / 4
        else:
            si_count += rogue_size / 2
        return si_count
    return -1
