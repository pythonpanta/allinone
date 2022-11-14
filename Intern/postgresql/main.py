import psycopg2
import psycopg2.extras

hostname='localhost'
database='student'
username='postgres'
pwd='panta'
pord_id=5432
conn=None
cur=None


def create_table(conn,cur):
    cur.execute('DROP TABLE IF EXISTS teacher')
    create_script='''
    CREATE TABLE IF NOT EXISTS teacher(
        id int PRIMARY KEY,
        name  VARCHAR(40) NOT NULL,
        salary  int,
        dept_id VARCHAR(30)
    )
    '''
    cur.execute(create_script)
    conn.commit()
    print('created successfully')


def insert_data(conn,cur):
    insert_script='INSERT INTO teacher(id,name,salary,dept_id) VALUES(%s,%s,%s,%s)'
    # insert_value=(1,'amrit',5000,'D1')
    # if you want ot insert many data then you can used list of multiple tuples concept
    insert_values=[
        (1,'amrit',5000,'D1'),
        (2,'ram',5000,'D1'),
        (3,'shyam',6000,'D1'),
        (4,'hari',7000,'D1'),
        (5,'sita',5000,'D1'),
        ]
    for insert_value in insert_values:
        cur.execute(insert_script,insert_value)
    conn.commit()
    print('data is successfully inserted...')

def fetch_all_data(cur):
    cur.execute('SELECT * FROM teacher')
    # it fetch all the data and store in cur pointer 
    for data in cur.fetchall():
        # print(data)
        print(data['name'],data['salary'])
        # print(data[1],data[2])
def update_data(conn,cur):
    # update_script='UPDATE teacher SET salary=salary+(salary*0.5)'
    update_script='UPDATE teacher SET salary=salary+(salary*0.5) WHERE id=1'
    cur.execute(update_script)
    conn.commit()
def delete_data(conn,cur):
    # delete_query='DELETE FROM teacher where id=2'
    delete_query='DELETE FROM teacher where name=%s'
    delete_record=('sita',)
    cur.execute(delete_query,delete_record)
    conn.commit()
    print('deleted successfully')
    
try:
    conn=psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=pord_id
    )
    print('successfully connected')
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #by putting psychopg2.extras fetchall data is now in the form of dictionay
    # create_table(conn,cur)
    # insert_data(conn,cur)
    # update_data(conn,cur)
    fetch_all_data(cur)
    delete_data(conn,cur)
    fetch_all_data(cur)
    

    
except Exception as e:
    print('connection failed to connect')
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()




