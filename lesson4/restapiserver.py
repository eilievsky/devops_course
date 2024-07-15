from  flask import Flask, request

app= Flask("evgeny" )

@app.route('/')
def hello():
    return "Hello, world !!!"

@app.route('/cars', methods=['GET','POST'])
def cars():
    if request.method == 'GET':
        return "Mazda , chevrilte , citroen "
    else:
        return "creating new car"

@app.route('/motors',methods=['GET','POST'])
def motors():
    if request.method == 'GET':
        return "Yamaha , hyundai"
    else:
        return "Creating new motor"

app.run(debug=True)