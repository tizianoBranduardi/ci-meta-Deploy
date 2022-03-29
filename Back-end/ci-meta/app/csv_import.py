import re
import os
import csv
import sys
from models import *
from flask import Flask
from flask_appbuilder import SQLA


#Usage : 
    #       ° file name is used as table name
    #       ° the first row is used to find the fields on wich insert data

sys.path.append('../')
app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)

def dateCheck( input ) :
    pattern_4digits = re.compile("^[0-9]{4}$")

    #Case NULL
    if input=="NULL" : 
        return None
    #Case only year
    elif pattern_4digits.match( str(input) ) :
        return "1-1"+input
    else :
        year=input.split('-')[0]
        month=input.split('-')[1]
        day=input.split('-')[2]
        if day=="00" :
            day="01"
        if month=="00" :
            month="01"
        return year+"-"+month+"-"+day


def main():
    
    file_path=sys.argv[1]
    table_name= os.path.splitext(os.path.basename(file_path))[0]

    with open(file_path) as csv_file:
        file= csv.reader(csv_file , delimiter=";")
        columns=next(file)
        size=len(columns)
        record_list=[]
        for row in file :
            record=[]
            for index in range(size) :
                value=row[index]
                if not value :
                    value=None
                #value="'{}'".format(value)
                record.append(value)
            record_list.append(record)

    if table_name == 'document' :
        for parameter in record_list :
            parameter[0]=dateCheck(parameter[0])
            new=Document(gregorian_date=parameter[0],type=parameter[1],incipit=parameter[2],transcription=parameter[3],collection=parameter[4],folder=parameter[5],folder_number=parameter[6],shelfmark=parameter[7],note=parameter[8])
            db.session.add(new)
        db.session.commit()

    if table_name == 'place' :
        for parameter in record_list :
            new=Place(city=parameter[0], description=parameter[1], is_validated=True)
            db.session.add(new)
        db.session.commit()

if __name__ == "__main__":
    main()