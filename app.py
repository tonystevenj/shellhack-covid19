from flask import Flask, render_template, request
import data_reader
app = Flask(__name__)

@app.route("/")
def index_m():
    return render_template("index.html")

@app.route("/data")
def data_m():
    return data_reader.return_tf()

# @app.route("/success")
# def success_m():
#     if request.method== "POST":
#         print(request.form)
#         email = request.form["email_name"]
#         height = request.form["height_name"]
#         print(db.session.query(moudels.User).filter(moudels.User.email==email))
#         if db.session.query(moudels.User).filter(moudels.User.email==email).count()==0:
#             data = moudels.User()
#             data.height=height
#             data.email=email
#             db.session.add(data)
#             db.session.commit()
#             return render_template("success.html")
#         else:
#             return "this email addr had submitted a record."
# print(__name__)
if __name__ == '__main__':
    app.debug = True
    app.run()


