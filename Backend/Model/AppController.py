from distutils.log import debug
from flask_cors import CORS
import MySQLdb
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import json
from json import loads
from flask import request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'wealthmanagement'

mysql = MySQL(app)
secure = HTTPBasicAuth()


#implementation of HTTPBasicAuth
@secure.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'user' and password == 'admin':
            return True
    else:
      return False
    return False

#api1 - Get all result and display on the funds Page
@app.route('/funds/all', methods=['GET'])
def ViewFunds():
    cur =mysql.connection.cursor()
    funds=cur.execute("SELECT * FROM `funds`;")
    # fun=Funds.Funds
    if(funds>0):
        Result=cur.fetchall()
        res=[]
        for i in range(len(Result)):
            cur={}
            cur['fundId']=Result[i][0]
            cur['fundName']=Result[i][1]
            cur['fundAmc']=Result[i][2]
            cur['fundRisk']=Result[i][3]
            cur['fundType']=Result[i][4]
            cur['fundAum']=Result[i][5]
            cur['fundNav']=Result[i][6]
            cur['fundMgr']=Result[i][7]
            cur['fundDesc']=Result[i][8]
            cur['imgSrc']=Result[i][9]
            res.append(cur)
        return jsonify(res)

#api2 - get distinct amc names to display on filter
@app.route('/fundAmc', methods=['GET'])
def FundAmc():
    cur =mysql.connection.cursor()
    funds=cur.execute("SELECT distinct fund_amc FROM funds;")
    if(funds>0):
        Result=cur.fetchall()
        return jsonify(Result)

#api3 - Get, order fund names alphabetically and deiplay it on funds page.
@app.route('/fundsOrder', methods=['GET'])
def fundsOrder():
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds order by fund_name;")
    rv = cur.fetchall()
    Results=[]
    for entry in rv:
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )
    return resreturn

#get distinct fund risk and display on filter 
@app.route('/fundRisk', methods=['GET'])
def fundRisk():
    cur =mysql.connection.cursor()
    cur.execute("SELECT distinct fund_risk FROM funds;")
    rv = cur.fetchall() 
    Results=[]
    for row in rv: 
      Results.append(row[0])
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )
    return resreturn

#order fund by aum
@app.route('/fundsOrderByAum', methods=['GET'])
def fundsOrderByAum():
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds order by fund_aum;")
    rv = cur.fetchall() 
    Results=[]
    for entry in rv: 
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )
    return resreturn


#get funds by their name. used in filter
@app.route('/funds/<fundname>', methods=['GET'])
def fundsbyinput(fundname):
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds where fund_amc=%s",[fundname])
    rv = cur.fetchall() 
    Results=[]
    for entry in rv:      
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )
    return resreturn

#Search functionality, get result for search
@app.route('/search/<fundname>', methods=['GET'])
def fundsbysearch(fundname):
    cur =mysql.connection.cursor()
    cur.execute("SELECT * FROM funds where fund_amc like '%%%s%%'" %(fundname))
    rv = cur.fetchall() 
    Results=[]
    for entry in rv: 
      Result={}
      Result['fundId']=entry[0]
      Result['fundName']=entry[1]
      Result['fundAmc']=entry[2]
      Result['fundRisk']=entry[3]
      Result['fundType']=entry[4]
      Result['fundAum']=entry[5]
      Result['fundNav']=entry[6]
      Result['fundMgr']=entry[7]
      Result['fundDesc']=entry[8]
      Result['imgSrc']=entry[9]
      Results.append(Result)
    response=Results
    resreturn=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
    )
    return resreturn


#get fund by the fund id
@app.route('/fundsById/<id>', methods=['GET'])
def FundsByFundId(id):
    cur =mysql.connection.cursor()
    cur.execute("SELECT fund_name, fund_amc, fund_risk, fund_aum, fund_type, fund_nav, fund_mgr, fund_desc, img_src,fh1month, fh1year, fh_total, f.funds_id FROM funds f join fund_history h on f.funds_id = h.fund_id where f.funds_id=%s;",[int(id)])
    rv = cur.fetchall()
    rv=jsonify(rv)
    return rv

#get fund by risk. used in filter
@app.route('/fundsRisk/<fundrisk>', methods=['GET'])
def fundsRisk(fundrisk):
  cur =mysql.connection.cursor()
  cur.execute("SELECT * from funds where fund_risk=%s",[fundrisk])
  rv = cur.fetchall()
  Results=[]
  for entry in rv:      
    Result={}
    Result['fundId']=entry[0]
    Result['fundName']=entry[1]
    Result['fundAmc']=entry[2]
    Result['fundRisk']=entry[3]
    Result['fundType']=entry[4]
    Result['fundAum']=entry[5]
    Result['fundNav']=entry[6]
    Result['fundMgr']=entry[7]
    Result['fundDesc']=entry[8]
    Result['imgSrc']=entry[9]
    Results.append(Result)
  response=Results
  return jsonify(response)

#get fund by aum. used in filter
@app.route('/fundsAum/<fundAums>',methods=['GET'])
def fundsAum(fundAums):
    fundAums=int(fundAums)
    cur =mysql.connection.cursor()
  #cur.execute("SELECT * from funds where fund_aum<%s",[fundAum])
    if fundAums == 10: 
        # print(fundAums)
        cur.execute("SELECT * from funds where fund_aum<100000000")
        rv = cur.fetchall()  
    elif fundAums == 20:
        
        cur.execute("SELECT * from funds where fund_aum<200000000")
        rv = cur.fetchall()
    elif fundAums == 30:
        
        cur.execute("SELECT * from funds where fund_aum<300000000")
        rv = cur.fetchall()
    Results=[]
    for entry in rv:
              
        Result={}
        Result['fundId']=entry[0]
        Result['fundName']=entry[1]
        Result['fundAmc']=entry[2]
        Result['fundRisk']=entry[3]
        Result['fundType']=entry[4]
        Result['fundAum']=entry[5]
        Result['fundNav']=entry[6]
        Result['fundMgr']=entry[7]
        Result['fundDesc']=entry[8]
        Result['imgSrc']=entry[9]
        Results.append(Result)
    response=Results
    return jsonify(response)

#get funds by their return. used in filter
@app.route('/fundsReturn/<fhtotal>',methods=['GET'])
def fundsNav(fhtotal):
  cur =mysql.connection.cursor()
  Results=[]
  #cur.execute("SELECT * from funds where fund_nav<%s",[fundnav])
  cur.execute("SELECT f.funds_id,fund_name, fund_amc, fund_risk, fund_type,fund_aum,fund_nav, fund_mgr, fund_desc, img_src,fh1month, fh1year, fh_total FROM funds f ,fund_history h where f.funds_id = h.fund_id and fh_total<%s",[fhtotal])
  rv = cur.fetchall()
  for entry in rv:      
    Result={}
    Result['fundId']=entry[0]
    Result['fundName']=entry[1]
    Result['fundAmc']=entry[2]
    Result['fundRisk']=entry[3]
    Result['fundType']=entry[4]
    Result['fundAum']=entry[5]
    Result['fundNav']=entry[6]
    Result['fundMgr']=entry[7]
    Result['fundDesc']=entry[8]
    Result['imgSrc']=entry[9]
    Results.append(Result)
  response=Results
  return jsonify(response)

#data fetched for showing fund details with thie returns
@app.route('/funds/join', methods=['GET'])
def fundsalljoin():
  cur =mysql.connection.cursor()
  Results=[]
  cur.execute("SELECT fund_name, fund_amc, fund_risk, fund_aum, fund_type, fund_nav, fund_mgr, fund_desc, img_src,fh1month, fh1year, fh_total FROM funds f ,fund_history h where f.fund_id = h.fund_id")
  rv = cur.fetchall()
  for entry in rv:      
    Result={}
    Result['fundId']=entry[0]
    Result['fundName']=entry[1]
    Result['fundAmc']=entry[2]
    Result['fundRisk']=entry[3]
    Result['fundType']=entry[4]
    Result['fundAum']=entry[5]
    Result['fundNav']=entry[6]
    Result['fundMgr']=entry[7]
    Result['fundDesc']=entry[8]
    Result['imgSrc']=entry[9]
    Results.append(Result)
  response=Results
  return jsonify(response)


#api to add user
@app.route('/user/add', methods=['POST'])           #method post
@secure.login_required                              #simpleauth  param
def newusr():
    cur =mysql.connection.cursor()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        usrEmail = json["userEmail"]
        usrPassword = json["userPassword"]
        usrName = json["userName"]
        usrPhoneNumber = json["userPhoneNumber"]
        usrAge = json["userAge"]
        imgsrc = json["imgSrc"]
        cur.execute(
    """INSERT INTO
        users (
            img_src,
            user_age,
            user_email,
            user_name,
            user_password,
            user_phone_number)
    VALUES (%s,%s,%s,%s,%s,%s)""", (imgsrc, usrAge, usrEmail, usrName, usrPassword, usrPhoneNumber))
        mysql.connection.commit()
        cur.execute("""SELECT * FROM users WHERE user_email=%s and user_password=%s""", (usrEmail, usrPassword))
        rv = cur.fetchall()
        for entry in rv:
            Result={}
            Result['userId']=entry[0]
            Result['userName']=entry[4]
            Result['userEmail']=entry[3]
            Result['userPassword']=entry[5]
            Result['userPhoneNumber']=entry[6]
            Result['userAge']=entry[2]
            Result['imgSrc']=entry[1]
            response=Result
        return jsonify(response)
    else:
        return 'Request not valid!'

 #api to sign in existing user
@app.route('/signin', methods=['POST'])      #method post
@secure.login_required                      #simple auth param
def signIn():
    cur =mysql.connection.cursor()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        usrEmail = json["userEmail"]
        usrPassword = json["userPassword"]
        cur.execute("""SELECT * FROM users WHERE user_email=%s and user_password=%s""", (usrEmail, usrPassword))
        rv = cur.fetchall()
        for entry in rv:
            Result={}
            Result['userId']=entry[0]
            Result['userName']=entry[4]
            Result['userEmail']=entry[3]
            Result['userPassword']=entry[5]
            Result['userPhoneNumber']=entry[6]
            Result['userAge']=entry[2]
            Result['imgSrc']=entry[1]
            response=Result
        return jsonify(response)
    else:
        return 'Request not valid!'

#add user fund 
@app.route('/userfund/add', methods=['POST'])  #post method
@secure.login_required                         #simple auth param
def userFundAdd():
    cur =mysql.connection.cursor()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        userid = json["userId"]
        ufid = json["ufId"]
        fndid = json["fundId"]
        uftype = json["ufType"]
        ufdate = json["ufDate"]
        ufamount = json["ufAmount"]
        fundname = json["fundName"]
        #fundamc = json["fundAmc"]
        #totalfund = json["totalFund"]
        cur.execute(
    """INSERT INTO
        user_fund (fund_id,
            uf_amount,
            uf_date,
            uf_type,
            user_id)
    VALUES (%s,%s,%s,%s,%s)""", (fndid,ufamount, ufdate, uftype, userid))
        mysql.connection.commit()
        return jsonify(json)
    else:
        return 'Request not valid!'

#get funds by user id. displays the user fund
@app.route('/fundsHistoryById/<id>', methods=['GET'])
def FundHistoryById(id):
    cur =mysql.connection.cursor()
    cur.execute("SELECT fund_name, fund_amc, uf_type, uf_amount, uf_date FROM funds f join user_fund u on f.fund_id = u.fund_id WHERE user_id=%s;",[int(id)])
    rv = cur.fetchall()
    rv=jsonify(rv)
    return rv

#shows total fund that a user purchased
@app.route('/fundtotal/<id>', methods=['GET'])
def FundTotal(id):
    cur =mysql.connection.cursor()
    cur.execute("SELECT sum(uf_amount) FROM funds f join user_fund u on f.fund_id = u.fund_id WHERE user_id=%s;",[int(id)])
    rv = cur.fetchall()
    rv=jsonify(rv)
    return rv

#delete the user funds
@app.route('/funddelete', methods=['DELETE'])   #method delete
@secure.login_required                          #basicauth
def funddelete():
    cur =mysql.connection.cursor()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        uf_id = json["ufId"]
        userid = json["userid"]
        cur.execute(
    """DELETE from user_fund where uf_id=%s and user_id=%s""", (uf_id,userid))
        mysql.connection.commit()
        return jsonify(json)
    else:
        return 'Request not valid!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')

