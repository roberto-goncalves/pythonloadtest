from bottle import route, run, template
import mysql.connector

cnx = mysql.connector.connect(user='root', password='fartoysoldiers',
                              host='cloud-db.cu0ddpcggpfz.sa-east-1.rds.amazonaws.com',
                              database='mes')
cursor = cnx.cursor()


drop_table = "DROP TABLE IF EXISTS tp1"

cursor.execute(drop_table)
cnx.commit()

create_table = "CREATE TABLE tp1(id int auto_increment, request int, PRIMARY KEY(id))"

cursor.execute(create_table)
cnx.commit()

@route('/insert/<requestId>')
def index(requestId):
    
    add_request = ("INSERT INTO tp1(request) VALUES(%s)" % requestId)

    cursor.execute(add_request)
    cnx.commit()

    
    return "route accepted"

@route('/select')
def select():
    from json import dumps
    result = []
    select_request = ("SELECT * FROM tp1")

    cursor.execute(select_request)
    
    for(id, request) in cursor:
        result.append(id)
        result.append(request)
    return dumps(result)

run(host='0.0.0.0', port=80)

cursor.close()
cnx.close()
