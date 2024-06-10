from pydantic import BaseModel

class DonationBase(BaseModel):
    aid : str
    why : str
    driveLink : str
    
class DonationCreate(DonationBase):
    pass
class Donation(DonationBase):
    class Config:
        orm_mode = True
        
class StudentBase(BaseModel):

    name : str
    email : str
    
    
    

class StudentCreate(StudentBase):
    password : str


class Student(StudentBase):
    highestQualification:str
    strongestField:str
    commSkills:str
    
    selfLearningCapability:str
    memCapability:str
    goodAt:str
    
    typeWorker:str
    workStyle:str
    numOfWorkingHours:int
    
    underPressure:str
    choiceOrChance:str
    stressed:str
    
    happinessIndex:int

    

    


class MentorBase(BaseModel):
    
    name : str
    email : str
    


class MentorCreate(MentorBase):
    password: str


class Mentor(MentorBase):
    profession:str
    skills : str
    
    commSkills : str        
    numOfWorkingHours: int   
    typeWorker: str     
    
    goodAt: str     
    upiId: str      
    
    highestQualification:str
    class Config:
        orm_mode = True
        

    

