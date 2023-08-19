rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915},
    {"name": "Mmazon", "length": 3915}
]

# for riv in rivers:
#     print(riv["name"])

# total_length = 0
# for len in rivers:
#     total_length += len["length"]
# print(f"Total Length of the Rivers = {total_length}mil")

for riv in rivers:
    name_river = riv["name"]
    if name_river.startswith("M"):
        print(name_river)