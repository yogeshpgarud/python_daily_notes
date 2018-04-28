# define and access the list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print "last element of the list is "
print(bicycles[-1])

# friends list creation and access test case
names = ['pankaj', 'pushpendra', 'arihant', 'dhananjay', 'yugain']
print names
print names[0]
print names[1]
print names[2]
print names[3]
print names[4]

# adding a message in front of each friend name
message = "Hi "
print message + names[0]
print message + names[1]
print message + names[2]
print message + names[3]
print message + names[4]
print names

# adding friend to list
names.append("nitikesh")
print names

# add friend in location/order
print "add test in the list at position 2 i.e python index 3"
names.insert(3, "sushant")
print names

# remove a friend from list
print "removed one friend from list !!!"
del names[3]
print names

# remove friend name and store its value
remove_item = names.pop(3)
print remove_item
print names

# remove friend using value in the list
names.remove('yugain')
print names

# sort the list
names.sort()
print names

# sort the list in reverse order
names.sort(reverse=True)
print names

# sort the list temporarily
test_name = ["a", "A", "B", "b"]
print sorted(test_name)


# reverse the order of list
test_name.reverse()
print test_name

# get length of the list
print len(test_name)