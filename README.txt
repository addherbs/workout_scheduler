This is a guide on how to create the tables dynamically from sqlalchemy using the classes that has been created:

step 1:
use powershell or any other console UI

step 2:
change directory to the project folder 

step 3:
open python interpretor(python3 for linux or mac/ Python3 exe location for windows if default is python 2.7 installed)

step4:
type the commands:

from flask_sqlalchemy import SQLAlchemy
from model import *
de.create_all()


==> if no errors