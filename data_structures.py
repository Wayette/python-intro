#data structures
#collection
#list, dictionary, set

scores = [78, 43, 67, 89, 45, 76, 99, 90, 56, 43, 65, 55, 61, 23, 54, 89, 90, 49, 69]

#access a score
print(scores[0])
print(scores[1])

#add a score
scores.append(51)
print(scores)

#remove
scores.remove(43)
print(scores)

print(len(scores))

print(scores.count(45))

scores.sort()  #ascending
print(scores)

scores.sort(reverse=True)   #descending
print(scores)

#slice a list
top_five = scores[-5:]   #cutting a list
print(top_five)

#slicing list in python

#dictionary

person = {"name": "Halima", "age": 19, "weight": 58, "county": "Nairobi"}
print(person["name"])
print(person["age"])

#set
days = {"mon", "tues", "wed", "thu", "fri", "sat", "sun", "mon"}
print(days)

for s in scores: #for each score in scores
    if s < 50:
        pass
    print(s)

for d in days: #for each day in days
    print(d)










