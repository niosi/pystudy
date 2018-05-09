from flask import Flask, render_template, request, make_response, redirect,url_for
import json
app = Flask(__name__)


@app.route("/")
def index():
    return b"This is Flask TestDemo"


@app.route("/loginIndex")
def login():
    return render_template("login.html")


@app.route("/success", methods=['POST', 'GET'])
def loginSuccess():
    if request.method == 'POST':
        loginid = request.form["loginid"]
        loginpwd = request.form["loginpwd"]
        return render_template("success.html", loginid=loginid, loginpwd=loginpwd)
    else:
        paras = {}
        for i, j in request.args.items():
            paras[i] = j
        print(paras)
        return __name__


@app.route("/fileupload", methods=["POST"])
def fileupload():
    if request.method == 'POST':
        try:
            f = request.files['fieldNameHere']
            f.save(f.filename)
            return 'success'
        except Exception as e:
            return e
        finally:
            f.close()

@app.route("/setcookie", methods=['POST', 'GET'])
def setCookit():
   resp = make_response()
   resp.set_cookie('testcookie', 'testvalue')
   return resp

@app.route("/getcookie", methods=['POST', 'GET'])
def getCookie():
    cookies = request.cookies["name"]
    print(cookies)
    return cookies

@app.errorhandler(404)
def pagenotfound(error):
    print(error)
    return render_template('login.html')

@app.route("/redirect")
def redirecturl():
    return redirect(url_for('getCookie'))
# @app.before_request
# def beforeFun():
#     print("run before")
#
#
# @app.after_request
# def afterFun(param):
#     print("run after")
#     print(request.url)
#     wrappers.Response.data
#     print("after", param.data)
#     return param
#
#
# @app.teardown_request
# def teardFun(param):
#     print("run teardown")
#     print(request.url)
#     print(param)
#     return param


if __name__ == '__main__':
    app.run('', 9999, debug=True)
