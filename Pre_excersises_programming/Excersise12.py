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
44: "to town.",
11: "in her bed.",
201: "in the livingroom.",
23: "up the mountain."
}

for name, ID in who.items():
    print(f"{name} {what[ID]} {where[ID]}")