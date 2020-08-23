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
