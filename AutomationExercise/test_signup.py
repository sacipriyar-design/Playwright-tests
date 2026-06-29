from pages.SignUp_Page import signup
import csv
import pytest

users =[
["Test1","Test3@email.com","Mr. ","password123","1","1","2000","Test1","Testlastname","Testcompany","p.no1, test street","address2","India","TN","Chennai","600121","9985344222"],
["Test2","Test4@email.com","Mr. ","password123","12","12","1990","Test2","Testlastname","Testcompany","p.no1, test street","address2","Singapore","ss","ddd","600121","9985344222"],
["Test3","Test5@email.com","Mrs. ","password123","21","5","2006","Test3","Testlastname","Testcompany","p.no1, test street","address2","Australia","sydney","adfa","600121","9985344222"],
]

@pytest.mark.parametrize("name,email,title,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobilenumber",users)
def test_signup(test_goto_page,name,email,title,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobilenumber):
    sign_up= signup(test_goto_page)
    sign_up.goto_page()
    sign_up.signup(name,email,title,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobilenumber)
    assert sign_up.is_signup_successful()
    with open("users.csv","a",newline='') as file:
        writer=csv.writer(file)
        writer.writerow([name,email,title,password,day,month,year,firstname,lastname,company,address,address2,country,state,city,zipcode,mobilenumber])