
from flask import render_template,Flask,request 
app = Flask(__name__)  
  
# @app.route('/',methods = ['GET','POST'])  
# def main():
#     return "///"

@app.route('/user',methods = ['GET','POST'])  
def user():
        uname=request.form['empName']  
        uemail=request.form['empEmail']
        uloc=request.form['empPlace']
        udob=request.form['empDob']
        usal=request.form['empSal']
        ucomm=request.form['cmts']
        # if request.method=='POST':
        slist=["Name","Email","Location","Dateofbirth","Salary","Comments"]
        ulist=[uname,uemail,uloc,udob,usal,ucomm] 
        overall_list=[]
        overall_list.append(ulist)
        # print(overall_list)
        # return overall_list
        # return uname
        return render_template('edetails.html',s=slist,ol=overall_list)

        
   
if __name__ == '__main__':  
   app.run(port=50001,debug=True)  
