""""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])
"""

# register
#login

#method1
"""
aSampleList = [1,2,3,4,5]
dictOne = {
  "key1" : "value1",
  "key2" : "value2",
  "key3" : "value3"

}

print (dictOne)
print (aSampleList)
"""

#method2
dictTwo = {}

dictTwo["key5"] = "value5"
dictTwo["key6"] = "value6"
dictTwo["key7"] = "value7"
print (dictTwo)
"""
del dictTwo["key6"]
print(dictTwo)

dictTwo.pop("key5")
print (dictTwo)
"""

#dictionaryLoop

for key,value in dictTwo.items():
  print ("I have " + key+ " relating with " + value )

