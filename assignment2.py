import argparse
from os import name
import urllib.request
import urllib.error
import tempfile
import shutil
import logging
import datetime
import csv

url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'


def downloadData():
    """Downloads the data"""
    try:
        with urllib.request.urlopen(url) as response:
            res= response.read()
            data = res.decode('utf-8')
            
        return data
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
    pass


def processData(id,file_content):

    """ for lines in file_content.split('\n'):
        parts = lines.split(",")
        file_dict[parts[0]]= (parts[1], parts[2])
        file_dict.update(parts[0])
z=-
    print(file_dict)
    return file_dict[parts[0]]
   """
    file_dict = {'id': [], 'name': [], 'birthday':[]}
    file_id = id
    print(id)
    print(file_id)
    print(file_content)
    if file_id == id:
        file_dict.update(file_content)
        for lines in file_content.split('\n'):
            print("lines",lines)
            new_data = lines.split(" ,")
            print("From",new_data)
            file_dict["id"].append(lines[0])
            file_dict["name"].append(lines[1])
            file_dict["birthday"].append(lines[2])
            print("dict",file_dict)

        return file_dict
    else:
        print("unable to find")
        
    pass


def displayPerson(id, personData):
    print("person",personData)
    id2 = personData['id']
    name = personData['name']
    birthday = personData['birthday']
    if id == id2:
        print("Person # {id} is {name} with a birthday of {birthday}")
    else:
        print("No user found with that ID.")
    pass

def main(url):
    
    csvData = downloadData()
    id = int(input("Enter an ID number: "))
    personData = processData(id, csvData)
    displayPerson(id, personData)
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str,required=True )
    args = parser.parse_args()
    main(args.url)
