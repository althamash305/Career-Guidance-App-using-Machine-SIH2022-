from fastapi import FastAPI,Request,Depends,HTTPException,Form,Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


import crud,models,schemas
from database import SessionLocal,engine

#ML imports
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedShuffleSplit




models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally : 
        db.close()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
@app.get('/',response_class=HTMLResponse)
async def default():
    return RedirectResponse('index.html')

@app.get('/index.html',response_class=HTMLResponse)
async def load_index(request:Request):
    return templates.TemplateResponse('index.html',{'request':request})

@app.get('/about-us.html')
async def load_about_us(request:Request):
    return templates.TemplateResponse('about-us.html',{'request':request})

@app.get('/contact.html')
async def load_contact(request:Request):
    return templates.TemplateResponse('contact.html',{'request':request})

@app.get('/news.html',response_class=HTMLResponse)
async def load_news(request:Request):
    return templates.TemplateResponse('news.html',{'request':request})

@app.get('/rank-prediction.html',response_class=HTMLResponse)
async def load_rank_prediction(request:Request):
    return templates.TemplateResponse('college.html',{'request':request})
@app.get('/mentor.html',response_class=HTMLResponse)
async def load_mentor(request:Request):
    return templates.TemplateResponse('mentor.html',{'request':request})
@app.get('/mentorform.html')
async def load_mentor_form(request:Request):
    return templates.TemplateResponse('mentorform.html',{'request':request})

@app.get('/signin.html',response_class=HTMLResponse)
async def load_signin(request:Request):
    return templates.TemplateResponse('signin.html',{'request':request})

@app.get('/signup.html',response_class=HTMLResponse)
async def load_signup(request:Request):
    return templates.TemplateResponse('signup.html',{'request':request})

@app.get('/college.html',response_class=HTMLResponse)
async def load_rank_prediction(request:Request):
    return templates.TemplateResponse('college.html',{'request':request})

# @app.get('/chooseUser.html')
# async def load_choose_User(request:Request):
#     return templates.TemplateResponse('chooseUser.html',{'request':request})

@app.get('/college.html')
async def load_college(request:Request):
    return templates.TemplateResponse('college.html',{'request':request})

@app.get('/form.html')
async def load_college(request:Request):
    return templates.TemplateResponse('form.html',{'request':request})

@app.get('/fundHelp.html')
async def load_fund_Help(request:Request):
    return templates.TemplateResponse('fundHelp.html',{'request':request})

@app.post("/fundHelp", response_model=schemas.Donation)
async def create_fundHelp(request:Request, db: Session = Depends(get_db)):
    # print(request.json())
    # db_user = crud.get_user_by_email(db, email=user.email)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    form = await request.form()
    user = schemas.DonationCreate(aid=form['aid'],why=form['why'],driveLink=form['driveLink'])
    try :
        crud.create_donation(db=db, user=user)
    except :
        return templates.TemplateResponse('donation.html',{'request':request,'status':'Already Requested'})
    return templates.TemplateResponse('donation.html',{'request':request,'status':'Your Request will considered and we will contact you soon'})

@app.get('/mentor.html')
async def load_mentors(request:Request):
    return templates.TemplateResponse('donation.html',{'request':request})    




#Database Section 

@app.post("/student/create", response_model=schemas.Student)
def create_student(request:Request,user: schemas.StudentCreate, db: Session = Depends(get_db)):
    # print(request.json())
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_student(db=db, user=user)


@app.post("/mentor/create", response_model=schemas.Mentor)
def create_mentor(user: schemas.MentorCreate, db: Session = Depends(get_db)):
    db_user = crud.get_mentor_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_mentor(db=db, user=user)


#Post


@app.post('/signup')
async def read_signup_data(request:Request,db: Session = Depends(get_db)):
    form = await request.form()
    db_user = crud.get_student_by_email(db,email=form['email'])
    if db_user:
        return templates.TemplateResponse('signin.html',{'request':request})
    
    user = schemas.MentorCreate(name=form['name'],email=form['email'],password=form['password1'])
    crud.create_student(db=db,user=user)
    return templates.TemplateResponse('afterSignIn.html',{'request':request})

@app.post('/signin')
async def read_signup_data(request:Request,db: Session = Depends(get_db)):
    form = await request.form()
    print(form)
    db_user = crud.get_student_by_email(db,email=form['email'])
    try:
        if not db_user:
            # raise HTTPException(status_code=400, detail="Email already registered")
            return templates.TemplateResponse('signup.html',{'request':request})
        if form['password'] != db_user.password :
            return templates.TemplateResponse('signin.html',{'request':request})
        # user = schemas.MentorCreate(name=form['name'],email=form['email'],password=form['password1'])
        # return crud.create_student(db=db,user=user)
        return templates.TemplateResponse('form.html',{'request':request})
    except:
        return templates.TemplateResponse('signup.html',{'request':request})
    

# label_encoder = LabelEncoder()

@app.post('/form')
async def read_signup_dat(request:Request,db: Session = Depends(get_db)):
    form = await request.form()
    print(form)
    # db_user = crud.get_student_by_email(db,email=form['email'])
    
    # if form['goal'] == 'Not sure':
    data = pd.read_csv('cleaned.csv',index_col=False)
    columns = ['Highest Qualification', 
        'Which is/was your strongest field?',
        'How good is your communication skills?',
        'Self-learning capability',
        'Memory capability', 'Which one are you good at?',
        'Which one of these options would describe you?',
        'Which one do you prefer?', 'Undergoing peer pressure?',
        'Did you land into your current position by choice or by chance?',
        'Do you feel stressed?']

    label_encoders = {}
    for column in columns :
        label_encoder = LabelEncoder()
        data[column]= label_encoder.fit_transform(data[column])
        label_encoders.update({column:label_encoder})
        
    x_cols = list(data.columns )
    x_cols.remove('Current qualification')
    X = data[x_cols]
    y = data['Current qualification']

    
    scores = []
    sss = StratifiedShuffleSplit()

    # using regression to get predicted data
    rf = RandomForestClassifier(n_estimators=40, max_depth=7)
    for train_index, test_index in sss.split(X, y):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y[train_index], y[test_index]
        rf.fit(X_train, y_train)
        pred = rf.predict(X_test)
        scores.append(accuracy_score(y_test, pred))

    # get accuracy of each prediction
    print(scores)
    
    inp = {
    'Highest Qualification':[form['board']],
    'Which is/was your strongest field?':[form['subject']],
    'How good is your communication skills?':[form['communication']],
    
    'Number of working/studying hours per day':[form['hours']],        
    'Self-learning capability':[form['self']],
    'Memory capability':[form['memory']],
    'Which one are you good at?':[form['pt']],
    
    'Which one do you prefer?':[form['solo']],
    'Which one of these options would describe you?':[form['workStyle']],
    'Undergoing peer pressure?':[form['peer']],
    
    'Did you land into your current position by choice or by chance?':['Choice'],
    'Do you feel stressed?':[form['stressed']],
    
    'Happiness Index':[form['happy']],
    }
    print(len(inp))

    da = pd.DataFrame(inp)
    
    columns = ['Highest Qualification',
        'Which is/was your strongest field?',
        'How good is your communication skills?',
       
        'Self-learning capability',
        'Memory capability',
        'Which one are you good at?',
       
         'Which one of these options would describe you?',       
        'Which one do you prefer?',
        'Undergoing peer pressure?',
       
        'Did you land into your current position by choice or by chance?',       
        'Do you feel stressed?']
    for c in columns:
        da[c]=label_encoders[c].transform(da[c])
    
    # da['Which one of these options would describe you?'] = label_encoders['Which one of these options would describe you?'].transform(da['Which one of these options would describe you?'])
    pred = rf.predict(da)
    pred=str(pred)
    
    # return {'prediction':pred}
    return templates.TemplateResponse('careerPredictor.html',{'request':request,'Career':pred})

