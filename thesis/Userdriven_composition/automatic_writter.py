def actuator_function_writter(function_name,url):
	file = open("test_file.py","a+")

	code = """
	def""" + function_name+"""(motor_status):
	url = '"""+url+"""'

	data = {

		"topic": "mc101",
		"value": motor_status,
		"time": "2019-01-24T13:35:24.246226Z",
		"name": "1"
	        }

	

	#Call REST API
	response = requests.put(url, data=data)

	#Print Response
	print(response.text)

	"""

	file.write(code)

	file.close()







def sensor_function_writter(function_name,url):
	file = open("test_file.py","a+")

	code = """
	def """+function_name+"""():
		data = requests.get('"""+url+"""').json()
		data = int(data['value'])
		return(data)

	"""

	file.write(code)

	file.close()
