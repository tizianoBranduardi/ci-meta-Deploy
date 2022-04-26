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
    if input is None :
        return None
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
            parameter[1]=dateCheck(parameter[1])
            new=Document(id=parameter[0], gregorian_date=parameter[1],type=parameter[2],title=parameter[3],incipit=parameter[4],transcription=parameter[5],archive=parameter[6],collection=parameter[7],folder=parameter[8],folder_number=parameter[9],shelfmark=parameter[10],publication=parameter[11],note=parameter[12])
            db.session.add(new)
        db.session.commit()

    if table_name == 'place' :
        for parameter in record_list :
            new=Place(city=parameter[0], description=parameter[1], is_validated=True)
            db.session.add(new)
        db.session.commit()

    if table_name == 'person' :
        for parameter in record_list :
            new=Person(name=parameter[0], name_latin=parameter[1], alias=parameter[2], birth=parameter[3], death=parameter[4], reference=parameter[5], notes=parameter[6], wikidata=parameter[7], links=parameter[8])
            db.session.add(new)
        db.session.commit()

    if table_name == 'institution' :
        for parameter in record_list :
            new=Institution(name=parameter[0], visibility=parameter[1], type=parameter[2], year=parameter[3], place=parameter[4], notes=parameter[5])
            db.session.add(new)
        db.session.commit()

if __name__ == "__main__":
    main()
