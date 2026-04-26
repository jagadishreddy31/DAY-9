import copy

def get_data():
    return [
        {"item": "Laptop", "details": {"price": 50000, "stock": 10, "supplier": {"rating": 4.5}}},
        {"item": "Phone", "details": {"price": 20000, "stock": 25, "supplier": {"rating": 4.2}}},
        {"item": "Tablet", "details": {"price": 35000, "stock": 15, "supplier": {"rating": 4.0}}}
    ]

def update_items(arr, r):
    pos = r % len(arr)
    for i in range(len(arr)):
        if i == pos:
            arr[i]["details"]["price"] = int(arr[i]["details"]["price"] * 0.9)
            arr[i]["details"]["stock"] += 5
    return arr

def check_diff(a, b):
    changed, unchanged = [], []
    for i in range(len(a)):
        if a[i] == b[i]:
            unchanged.append(a[i]["item"])
        else:
            changed.append(a[i]["item"])
    return changed, unchanged

roll = 24110011621

main_data = get_data()
shallow_copy = main_data.copy()
deep_copy = copy.deepcopy(main_data)

update_items(shallow_copy, roll)
update_items(deep_copy, roll)

print(main_data)
print(shallow_copy)
print(deep_copy)

c1, u1 = check_diff(main_data, shallow_copy)
c2, u2 = check_diff(main_data, deep_copy)

print(c1, u1)
print(c2, u2)
print((len(c1), len(u1)))
print((len(c2), len(u2)))
