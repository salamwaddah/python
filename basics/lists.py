friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
lucky_numbers = [3, 5, 7, 13, 24, 39]

friends[1] = "Mike"
print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

friends.pop()
friends.insert(1, "Kelly")
friends.append("Creed")
friends.remove("Jim")
friends.sort()
print(friends)
friends.reverse()
print(friends)

print(friends.index("Kevin"))
print(friends.count("Jim"))

friends_copy = friends.copy()
friends.extend(lucky_numbers)
print(friends)

friends.clear()
print(friends)
print(friends_copy)

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)
