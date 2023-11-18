from fastapi.testclient import TestClient
from app.main import app



client=TestClient(app)

def test_main():
    response=client.post("/get_form?f1=v1")
    assert response.json()=={"f1":"text"}

def test_myform_passed():
    response = client.post("/get_form?text_field=sdhfghjkgsdkfgkjsd&data_field=11.11.2003")
    assert response.json() == ['MyForm']

def test_myform_error():
    response = client.post("/get_form?text_field=sdhfghjkgsdkfgkjsd&data_field=11.hh")
    assert response.json() == {"text_field":"text",'data_field':'text'}

def test_phone_and_email_passed():
    response = client.post("/get_form?phone_field=+79217552682&email_field=ilya765toolkiy@gmail.com")
    assert response.json() == ['phone_and_email']

def test_phone_and_email_error():
    response = client.post("/get_form?phone_field=+79217552682&email_field=ilya765toolkiy")
    assert response.json() == {"phone_field":"phone",'email_field':'text'}

def test_multi_form_passed():
    response = client.post("/get_form?phone_field=+79217552682&email_field=ilya765toolkiy@gmail.com&data_field=11.11.2003&text_field=v1dsfsdf")
    assert response.json() == ['MyForm','phone_and_email']

