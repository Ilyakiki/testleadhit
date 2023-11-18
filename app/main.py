import uvicorn
from tinydb import TinyDB, Query
import fastapi
import datetime
import re

db = TinyDB('db.json')
#db.insert({'name':'phone_and_email','phone_field':'phone','email_field':'email'})
app=fastapi.FastAPI(
    title='Get Form'
)
if db.all()==[]:
    db.insert({'name':'MyForm','text_field':'text','data_field':'data'})
    db.insert({'name':'phone_and_email','phone_field':'phone','email_field':'email'})
def get_type(text:str) -> str:

    if re.fullmatch('\d{4}-\d{2}-\d{2}',text) or re.fullmatch('\d{2}\.\d{2}\.\d{4}',text):
        if '-' in text:
            full_date=list(map(int,text.split('-')))
            try:
                datetime.datetime(full_date[0],full_date[1],full_date[2])
                return 'data'
            except:
                    return 'text'
        else:
            full_date = list(map(int,text.split('.')))
            try:
                datetime.datetime(full_date[2],full_date[1],full_date[0])
                return 'data'
            except:
                    return 'text'


    if re.fullmatch('\+7\d{10}',text):
        return 'phone'

    if '@' in text:
        return 'email'

    return 'text'


@app.post('/get_form')
def get_form(request:fastapi.Request):
    z=db.all()
    x=request.url.components.query.split("&")
    dc=dict()
    for i in x:
        key,value=i.split('=')
        type=get_type(value)
        dc[key]=[value,type]
    ready_forms=[]
    for form in z:
        item=list(form.items())[1:]
        count=0
        for k,v in item:
            if count==0:
                if k in dc and dc[k][1]==v:
                    continue
                else:
                    count+=1
        if count==0:
            ready_forms.append(form['name'])

    if ready_forms:
        return ready_forms
    else:
        returned_dc = dict()
        for key, value in dc.items():
            returned_dc[key] = value[1]
        return returned_dc


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#db.insert({'name':'MyForm','text_field':'text','data_field':'data'})