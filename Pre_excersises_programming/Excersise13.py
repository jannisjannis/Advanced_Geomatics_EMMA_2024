list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]

lists = [list1, list2, list3, list4]
char_dict = {}
for list in lists:
    for character in list:
        count = char_dict.get(character,0)
        count += 1
        char_dict[character] = count

for character, count in char_dict.items():
    print(f"count of {character} = {count}")