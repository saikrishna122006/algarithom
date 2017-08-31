def linearsearch(item,list):
	found = False
	pos = 0
	while pos < len(list) and not found:
		if list[pos] == item:
			found = True
		pos = pos+1
	return found
if __name__ == "__main__":
	list = [3,5,79,2,1,5,7,9,12,23,6,8]
	item = int(input("Enter your number:"))
	isitfound = linearsearch(item,list)
	if isitfound:
		print("your item is in the list")
	else:
		print("your item is not in the list please check")
