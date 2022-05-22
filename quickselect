import random


def quickselect(items, item_index):
    def select(lst, l, r, index):
        if r == l:
            return lst[l]

        # выбираем рандомный опорный элемент
        pivot_index = random.randint(l, r)

        # двигаем опорный элемент к началу списка
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        i = l
        for j in range(l + 1, r + 1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # двигаем опорный элемент чтобы исправить местоположение
        lst[i], lst[l] = lst[l], lst[i]

        # рекурсивное разбиение только на одну сторону
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i - 1, index)
        else:
            return select(lst, i + 1, r, index)

    if items is None or len(items) < 1:
        return None

    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()

    return select(items, 0, len(items) - 1, item_index)
