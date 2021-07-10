import json
f = open('comments.json',) #open the json file containing the test sentences
# returns JSON object as  
# a dictionary 
data = json.load(f) #load the data of the json file into data 
racial_slurs = ["ass-hole","browny","ape","snowflake","nigger","fuck","negro","cracker"] #specify which racial slurs to look for
# Iterating through the json 
# list 
for i in data['comments']:
    comment = i["comment"]
    name = i["name"]
    comment_token = list(comment.split())
    count = 0
    profanity_degree = 0
    for word in comment_token:
    	if word.lower() in racial_slurs:
    		count = count + 1    
	# Rate: number of occurrences normalized by total number
    profanity_degree = profanity_degree + count/len(comment_token)
    print("Comment:  "+ comment + ", By: " + name+ ", profanity_degree: " + str(profanity_degree)) 
# Closing file 
f.close() 