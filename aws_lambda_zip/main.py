# A lambda function to interact with AWS RDS MySQL

import pymysql
import sys

event = {
  "vehichleID": 2,
  "make": "Ferrari",
  "model": "Mclaren",
  "derivative":"1.5 TSI EVO Match Edition 5dr"
}
context = ""

REGION = 'ap-northeast-1a'

rds_host  = "database-4.c0793bdrqx2d.ap-northeast-1.rds.amazonaws.com"
name = "admin"
password = "Rohit1997"
db_name = "local"

def save_events(event):
    """
    This function fetches content from mysql RDS instance
    """
    result = []
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        # cur.execute("""insert into test (id, name) values( %s, '%s')""" % (event['id'], event['name']))
        # INSERT INTO vehicle VALUES(1000,'Volkswagen','Golf','1.5 TSI EVO Match Edition 5dr');
        # cur.execute(f"insert into vehicle VALUES ({event['vehichleID']}, {event['make']}, {event['model']}, {event['derivative']} )")
        print("*"*50)
        # print((event['vehichleID'], event['make'], event['model'], event['derivative']))
        # print("insert into vehicle VALUES ({}, '{}', '{}', '{}')".format(event['vehichleID'], event['make'], event['model'], event['derivative']))
        # print("*"*50)
        # # cur.execute("""insert into vehicle VALUES ({}, '{}', '{}', '{}')""".format(event['vehichleID'], event['make'], event['model'], event['derivative']))
        cur.execute("insert into vehicle VALUES (2001,'Volkswagen','Golf','1.5 TSI EVO Match Edition 5dr');")
        cur.execute("""select * from vehicle""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print("Data from RDS...")
        print(result)

def main(event, context):
    save_events(event)



# main(event, context)
