from sqlalchemy import String,Integer,Column,Boolean
from database import Base


class Student(Base):
    __tablename__ = 'students'
    
    # id = Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email = Column(String,index=True,primary_key=True,unique=True)                   #3
    
    password = Column(String)
    highestQualification = Column(String)#Highest Qualification
    strongestField = Column(String)#Strongest Field                  3
    
    commSkills = Column(String)#Communication Skills
    selfLearningCapability = Column(String)#Self Learning Capability
    memCapability = Column(String)#Memory Capability                    #3
    
    goodAt = Column(String)#Practical or Theory Oriented
    typeWorker = Column(String)#SmartWorkder or HardWorker
    workStyle = Column(String)#Solo/Team                                #3
    
    numOfWorkingHours = Column(Integer)#0-10
    underPressure = Column(String)#Yes or No
    choiceOrChance = Column(String)#Choice or Chance                    #3
    stressed = Column(String)#Yes or No
    happinessIndex = Column(Integer)#1-5

    
    
    
    
class Mentor(Base):
    __tablename__ = 'mentors'
    
    # id = Column(Integer,primary_key = True,index=True)
    name = Column(String)
    email = Column(String,primary_key=True,unique=True)
    
    
    password = Column(String)
    profession = Column(String)
    skills = Column(String)#Designing
    
    
    commSkills = Column(String)
    numOfWorkingHours = Column(Integer)
    typeWorker = Column(String)
    
    
    goodAt = Column(String)
    upiId = Column(String)
    
    highestQualification=Column(String)
    
    
    
class Donations(Base):
    __tablename__ = 'donate'
    
    aid = Column(String)
    why = Column(String)
    driveLink = Column(String,primary_key=True)