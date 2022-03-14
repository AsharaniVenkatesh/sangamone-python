from flask import Flask,render_template
factorial1=Flask(__name__)
@factorial1.route("/",methods=["POST","GET"])
def fact2():   
    num1=5
    fact1=1
    for i in range(1,num1+1):
        fact1=fact1*i
    print(fact1)
    return render_template("factorial1.html",message1=fact1)
if __name__=="__main__":
    factorial1.run(debug=True)
    
