import Node

data = [[]]
f = open('HTMLTagTestDataSet.csv')
fileOutput = open('TestDataOutput.csv', 'w')
for line in f:
	line = line.strip("\r\n")
	data.append(line.split(','))
data.remove([])
tree = {'Id': {'1': 'Y', '3': 'N', '2': 'Y', '5': 'N', '4': 'Y', '7': 'Y', '6': 'Y'}}
attributes = ['Id', 'ElementType', 'PrimaryAttributes', 'SecondaryAttributes', 'AutomationDecision']
count = 0
for entry in data:
	count += 1
	tempDict = tree.copy()
	result = ""
	while(isinstance(tempDict, dict)):
		root = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
		tempDict = tempDict[tempDict.keys()[0]]
		index = attributes.index(root.value)
		value = entry[index]
		if(value in tempDict.keys()):
			child = Node.Node(value, tempDict[value])
			result = tempDict[value]
			tempDict = tempDict[value]
		else:
			print "can't process input %s" % count
			result = "?"
			break
	fileOutput.write(result+'\n')
	print ("entry%s = %s" % (count, result))
fileOutput.write("Done")
