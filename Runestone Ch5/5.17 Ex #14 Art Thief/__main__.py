items = [
    # {'item': 1, 'weight': 2, 'value': 3},
    # {'item': 2, 'weight': 3, 'value': 4},
    # {'item': 3, 'weight': 4, 'value': 8},
    # {'item': 4, 'weight': 5, 'value': 8},
    # {'item': 5, 'weight': 9, 'value': 10}
    {'item': 1, 'weight': 200, 'value': 200},
    {'item': 2, 'weight': 100, 'value': 150},
    {'item': 3, 'weight': 100, 'value': 150},
]

def maximize_profit(w, items, current_weight=0):
    items = sorted(items, key=lambda x: (-x['weight'], x['value']))
    # print(items)
    for item in reversed(items):
        if current_weight + item['weight'] <= w:
            tmp = item
            items.remove(item)
            return [tmp] + maximize_profit(w, items, current_weight + item['weight'])
    return []

print(maximize_profit(200, items))
