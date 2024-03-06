# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# import pickle
# from datetime import datetime, timedelta
# scopes = ['https://www.googleapis.com/auth/calendar']
# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
# credentials = flow.run_local_server()
# pickle.dump(credentials, open("token.pkl", "wb"))
# credentials = pickle.load(open("token.pkl", "rb"))
# service = build("calendar", "v3", credentials=credentials)
# result = service.calendarList().list().execute()
# calendar_id = result['items'][0]['id']
# result = service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()
# start_time = datetime(2024, 5, 6, 22, 30, 0)
# end_time = start_time + timedelta(hours=4)
# timezone = 'Asia/Kolkata'
# event = {
#   'summary': 'Tweet 5',
#   'location': 'Vellore',
#   'description': 'I beg u to please work',
#   'start': {
#     'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#     'timeZone': timezone,
#   },
#   'end': {
#     'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#     'timeZone': timezone,
#   },
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }
# service.events().insert(calendarId=calendar_id, body=event).execute()

# matches = datefinder.find_dates("5 may 9 PM")
# list(matches)
# def create_event(start_time_str, summary, duration=1, description=None, location=None):
#     matches = list(datefinder.find_dates(start_time_str))
#     if len(matches):
#         start_time = matches[0]
#         end_time = start_time + timedelta(hours=duration)
    
#     event = {
#         'summary': summary,
#         'location': location,
#         'description': description,
#         'start': {
#             'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#             'timeZone': 'Asia/Kolkata',
#         },
#         'end': {
#             'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#             'timeZone': 'Asia/Kolkata',
#         },
#         'reminders': {
#             'useDefault': False,
#             'overrides': [
#                 {'method': 'email', 'minutes': 24 * 60},
#                 {'method': 'popup', 'minutes': 10},
#             ],
#         },
#     }
#     return service.events().insert(calendarId='primary', body=event).execute()
# create_event("15 may 9 PM", "Meeting")