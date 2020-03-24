items = [
    {'item': 1, 'weight': 2, 'value': 3},
    {'item': 2, 'weight': 3, 'value': 4},
    {'item': 3, 'weight': 4, 'value': 8},
    {'item': 4, 'weight': 5, 'value': 8},
    {'item': 5, 'weight': 9, 'value': 10}
]

def maximize_profit(w, items, current_weight=0):
    items = sorted(items, key=lambda x: (x['value'], -x['weight']))
    # print(items)
    for item in reversed(items):
        if current_weight + item['weight'] < w:
            items.remove(item)
            return [item] + maximize_profit(w, items, current_weight + item['weight'])
    return []

print(maximize_profit(20, items))