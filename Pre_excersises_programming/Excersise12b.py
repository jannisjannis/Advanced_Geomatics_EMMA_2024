who = {
"Daisy": 11,
"Joe": 201,
"Will": 23,
"Hanna": 44
}
what = {
44: "runs",
11: "dreams",
201: "plays",
23: "walks"
}
where = {
"runs": "to town.",
"dreams": "in her bed.",
"plays": "in the livingroom.",
"walks": "up the mountain."
}

for name, ID in who.items():
    action = what[ID]
    place = where[action]
    print(f"{name} {action} {place}")
