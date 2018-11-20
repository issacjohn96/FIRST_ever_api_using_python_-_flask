DB=[
	{
	
		"id":10,
		"name":"book1"
	},

	{
		"id":2,
		"name":"book2"
	}

	] 


for book in DB:
	if book["id"]==10:
		book["id"]=11

print(DB)
