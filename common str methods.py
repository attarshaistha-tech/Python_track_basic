name="attar shaistha"
print(name[7]) #find character of index number #h
print(name.index('a')) #find index of character #0
print(len(name)) #find len of string # 14
print(len("name")) #4
print(name+'\tsujatha') # append/extend
#name.append("harsha") # attribute error
#name.extend("harsha") #attribute Error
#name.concat("harsha") #not possible in python

print(name.upper()) #convert str to upper
print(name.lower()) #convert str to lower

print(name.title()) #change first character of each word into uppercase
print(name.capitalize()) #captalze the first letter of each  string
location="      marathahalli                  "
print(location.strip()) #remove whitespaces
print(location.lstrip()) #remove left whitespaces
print(location.rstrip()) #remove right whitespaces

print(name.split()) #split the string into list of words using delemitor
print(name.replace("attar",'harsha')) #replace string perious to new value
print(name.find('i')) #to find string index
print(name.count('a')) #count no.of occurance
print(name.startswith('a')) #check whether a string starts with 'a' #true
print(name.startswith('s')) #false
print(name.endswith('a')) #check whether a string ends with 'a' #true
print(name.endswith('h'))  #false

skills=["python","java","sql","aws"]
skills.insert(2,"spark")
print(skills) #insert element at specific index


a=[1,2]
b=[3,4]
result=a+b
print(result)
#a.extend(b)
#print(a)
skills=["python","java","sql","aws"]
for skill in skills:
    print(skill)
    skills.pop(1)
print(skills)
 #remove element at specific index
del skills[0]
print(skills)
