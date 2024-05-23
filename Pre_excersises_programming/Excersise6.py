list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
counter = 0

while counter < 5:
    print (f"Number {list[counter]}")
    counter += 1

for index, item in enumerate(list):
    if index <= 5:
        print(f"Index: {index}; Number:{item}")