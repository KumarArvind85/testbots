import sys
sys.path.append('/Users/arvindk/projects/DecisionTree/src')
import DecisionTree

def main():
    #Insert input file
    """
    IMPORTANT: Change this file path to change training data 
    """
    file = open('HtmlTagsTrainingDataSet.csv')
    """
    IMPORTANT: Change this variable too change target attribute 
    """
    target = "AutomationDecision"
    data = [[]]
    for line in file:
        line = line.strip("\r\n")
        data.append(line.split(','))
    data.remove([])
    attributes = data[0]
    data.remove(attributes)
    #Run ID3
    tree = DecisionTree.makeTree(data, attributes, target, 0)
    print "generated decision tree"
    #Generate program
    file = open('program.py', 'w')
    
    file.write("import Node\n\n")
    #open input file
    file.write("data = [[]]\n")
    """
    IMPORTANT: Change this file path to change testing data 
    """
    file.write("f = open('HTMLTagTestDataSet.csv')\n")
    file.write("fileOutput = open('TestDataOutput.csv', 'w')\n")
    #gather data
    file.write("for line in f:\n\tline = line.strip(\"\\r\\n\")\n\tdata.append(line.split(','))\n")
    file.write("data.remove([])\n")
    #input dictionary tree
    file.write("tree = %s\n" % str(tree))
    file.write("attributes = %s\n" % str(attributes))
    file.write("count = 0\n")
    file.write("for entry in data:\n")
    file.write("\tcount += 1\n")
    #copy dictionary
    file.write("\ttempDict = tree.copy()\n")
    file.write("\tresult = \"\"\n")
    #generate actual tree
    file.write("\twhile(isinstance(tempDict, dict)):\n")
    file.write("\t\troot = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])\n")
    file.write("\t\ttempDict = tempDict[tempDict.keys()[0]]\n")
    #this must be attribute
    file.write("\t\tindex = attributes.index(root.value)\n")
    file.write("\t\tvalue = entry[index]\n")
    #ensure that key exists
    file.write("\t\tif(value in tempDict.keys()):\n")
    file.write("\t\t\tchild = Node.Node(value, tempDict[value])\n")
    file.write("\t\t\tresult = tempDict[value]\n")
    file.write("\t\t\ttempDict = tempDict[value]\n")
    #otherwise, break
    file.write("\t\telse:\n")
    file.write("\t\t\tprint \"can't process input %s\" % count\n")
    file.write("\t\t\tresult = \"?\"\n")
    file.write("\t\t\tbreak\n")
    
    file.write("\tfileOutput.write(result+'\\n')\r\n")
    
    #print solutions 
    file.write("\tprint (\"entry%s = %s\" % (count, result))\n")
    file.write("fileOutput.write(\"Done\")\n")
    print "written program"
    
    
if __name__ == '__main__':
    main()