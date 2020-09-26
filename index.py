from flask import Flask , render_template , request
from portScan import portScanner
app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ports', methods=["GET","POST"])
def ports():
    ip=request.form['ipaddress']
    res=portScanner(ip)
    return render_template("port.html", len=len(res) , pO=res)


app.run(debug= "true")