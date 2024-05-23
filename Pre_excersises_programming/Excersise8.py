string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum."""

count = len(string)
count2 = 0
for x in string:
    if x.isalpha():
        count2 += 1
count3 = len(string.split())
print(f"Character count: {count}")
print(f"Character count wihtout spaces: {count2}")
print(f"Word count: {count3}")