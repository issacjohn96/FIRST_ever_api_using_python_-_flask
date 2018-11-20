import flask
from flask import jsonify, request

app=flask.Flask(__name__)   # creating the web application 
app.config["DEBUG"]=True    #enabling the Debug helps to find Error and other stuff 

##################################################################################################################################
contacts=[					#creating a database contacts with appropriate items in in
{
	"name":"issac",
	"email":"issac.john96@yahoo.in",
	"number":"8867096609"

},
{
	"name":"immanuel",
	"email":"immanuel.john96@yahoo.in",
	"number":"8792341711"

}
]
##################################################################################################################################
#
@app.route("/all",methods=["GET"])
def show_all():
	return(jsonify(contacts))

##################################################################################################################################

@app.route("/all/certain",methods=["GET"])
def search():                               #Defining the search function to retrieve from databas  
	new_contact=[]
	
	name="no_name"
	number="none"
	email="no_mail"


	if "name" in request.args:
		name=request.args["name"]
	if "email" in request.args:
		email=request.args["email"]
	if "number" in request.args:
		number=request.args["number"]

	for contact in contacts:
		if contact["name"] == name or contact["email"] == email or contact["number"] == number:
			new_contact.append(contact)

	return(jsonify(new_contact))

##################################################################################################################################

@app.route("/add/intodatabas",methods=["POST"])
def add_data():                               #Defining the add function to add to  databas  
	request_data=request.get_json()
	new_db={
			"name":request_data["name"],
			"email":request_data["email"],
			"number":request_data["number"]

	}
	contacts.append(new_db)
	return jsonify(contacts)


##################################################################################################################################

@app.route("/remove_from_database",methods=["DELETE"])
def delete_data():
	counter=0									 #Defining the delete function to remove data from the databas  
	request_data=request.get_json()

	for contact in contacts:
		if request_data["name"] == contact["name"]: 
			del contacts[counter]
		counter+=1	


	return jsonify(contacts)

##################################################################################################################################


@app.route("/update_to_database",methods=["PUT"])
def update_data():
	counter=0									 #Defining the delete function to remove data from the databas  
	request_data=request.get_json()
	new_name=request_data["new_name"]
	name=request_data["name"]
	for contact in contacts:
		if contact["name"] == name:

			contact["name"]=new_name
			counter+=1

	return jsonify(contacts)

##################################################################################################################################


app.run()