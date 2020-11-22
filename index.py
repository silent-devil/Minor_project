from flask import Flask , render_template , request
import portScan
from portScan import portScanner2
import xssscan
from xssscan import check_xss
import subdomain
from subdomain import subfinder

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ports', methods=["GET","POST"])
def ports():
    ip=request.form['ipaddress']
    res=portScanner2(ip)
    return render_template("port.html", len=len(res) , pO=res)

@app.route('/xss', methods=["GET","POST"])    
def xss():
    url=request.form['ipaddress']
    result=check_xss(url)
    return render_template("xss_scn.html",le=len(result),ur=url,p=result)
@app.route('/subdomain', methods=["GET","POST"])    
def subdomain():
    url=request.form['ipaddress']
    result=subfinder(url)
    return render_template("subdomain.html",le=len(result),sublist=result)

app.run(debug= True)
