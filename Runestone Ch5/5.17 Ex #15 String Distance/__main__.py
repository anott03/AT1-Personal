

# def string_distance(initial, final, i=0):
#     if len(initial) < len(final):
#         initial += "*" * (len(final) - len(initial))
    
#     if final[i] in initial[i:]:
#         index = initial.find(final[i])
#         tmp = initial[index]
#         initial[index] = initial[i]
#         initial[i] = tmp
#         return 5 + art_thief(initial, final, i+1)

def string_distance(initial, final, i=0, char_counts=[]):
    nums = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'
    nums = nums.split(" ")
    
    chars = []
    for char in 'abcdefghijklmnopqrstuvwxyz':
        chars.append(char)
        char_counts.append(initial.count(char))

    if char_counts[chars.index(final[i])] > 0:
        char_counts[chars.index(final[i])] -= 1
        if i < len(final)-1:
            return 5 + string_distance(initial, final, i+1, char_counts)
        else:
            return 5

    if i < len(final)-1:
        return 5 + string_distance(initial, final, i+1, char_counts)
    else:
        return 20

print(string_distance("algorithm", "alligator"))
