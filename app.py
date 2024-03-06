import psycopg2
import datetime
from plyer import notification
import schedule
import time
import pandas as pd
from flask import Flask,render_template,url_for,request,redirect
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta

app=Flask(__name__)


hostname='localhost'
database='MOM'
username='postgres'
pwd='Achutham@123'
port_id=5432
df = pd.read_csv('C:\\Users\\drbin\\Desktop\\FLASK\\data\\tasks.csv')
now=datetime.now()

def db_conn():
    conn=psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    return conn

# scopes = ['https://www.googleapis.com/auth/calendar']
# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
# credentials = flow.run_local_server()
# service = build("calendar", "v3", credentials=credentials)
# result = service.calendarList().list().execute()
# calendar_id = result['items'][0]['id']

insert_script='INSERT INTO tasks(work_detail,user_name,intial_time,final_time) VALUES(%s,%s,%s,%s)'
prev=5
final=0
for index, row in df.iterrows():
    final=final+1
if final>prev:
    conn=db_conn()
    new=0
    curr=conn.cursor()
    for index, row in df.iterrows():
        insert_values=(row['work_detail'],row['user_name'],row['initial_time'],row['final_time'])
        curr.execute(insert_script,insert_values)
        # start_time = row['initial_time']
        # end_time = row['final_time']
        # timezone = 'Asia/Kolkata'
        # event = {
        # 'summary': f'{row['user_name']}',
        # 'location': 'Vellore',
        # 'description': f'{row['work_detail']}',
        # 'start': {
        #     'dateTime': start_time,
        #     'timeZone': timezone,
        # },
        # 'end': {
        #     'dateTime': end_time,
        #     'timeZone': timezone,
        # },
        # 'reminders': {
        #     'useDefault': False,
        #     'overrides': [
        #     {'method': 'email', 'minutes': 24 * 60},
        #     {'method': 'popup', 'minutes': 10},
        #     ],
        # },
        # }
        # service.events().insert(calendarId=calendar_id, body=event).execute()
        new=new+1
    prev=new
    conn.commit()

def checktasks():
    select_script='SELECT * FROM tasks'
    conn=db_conn()
    curr=conn.cursor()
    curr.execute(select_script)
    for record in curr.fetchall():
        if(now>record[4]):
            message = f"Deadline reached for tweet by {record[2]} at {record[4]}: {record[1]}"
            notification.notify(
                title="Deadline Reminder",
                message=message,
                app_name="Deadline Reminder",
                timeout=10
            )
    conn.commit()
schedule.every(5).minutes.do(checktasks)
# conn.commit()

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        conn=db_conn()
        curr=conn.cursor()
        task=request.form["newtask"]
        final=request.form["deadline"]
        new=final.split("T")
        new_insert_values=(task,"User4","2024-03-06 15:45:00",f"{new[0]} {new[1]+':00'}")
        curr.execute(insert_script,new_insert_values)
        conn.commit()
        taskList=[]
        select_script='SELECT * FROM tasks'
        curr.execute(select_script)
        for record in curr.fetchall():
            taskList.append(record)
        curr.close()
        conn.close()
        return render_template("home.html",ttasks=taskList)
    else:
        taskList=[]
        conn=db_conn()
        curr=conn.cursor()
        select_script='SELECT * FROM tasks'
        curr.execute(select_script)
        for record in curr.fetchall():
            taskList.append(record)
        curr.close()
        conn.close()
        return render_template("home.html",ttasks=taskList)


if __name__=="__main__":
    app.run(debug=True)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


