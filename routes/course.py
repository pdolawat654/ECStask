"""Routes for the course resource.
"""

from run import app
from flask import request
from http import HTTPStatus
import data
import json,jsonify


@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    json_file = open('json/course.json',)
    course_objects = json.load(json_file)
    if id >0 and id <= course_objects[-1]['id']:
        flag = 1
        for i in course_objects:
            if i["id"] == id:
                flag = 0
                break
        if flag == 0:
            return {"data":i}
        else:        
            return {"message":"Course "+str(id)+" does not exists"}
    else:
        return {"message":"Course "+str(id)+" does not exists"}


    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -----------------------------   --------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE


@app.route("/course", methods=['GET'])
def get_courses():
    json_file = open('json/course.json',)
    course_objects = json.load(json_file)
    try:
        title_words = request.args.get('title-words')
        title_words = title_words.split(',')
        final = []
        for i in data:
            for j in title_words:
                if j in i['title']:
                    if i not in final:
                        final.append(i)
    except:
        final = course_objects
    try:
        page_number = int(request.args.get('page-number'))
    except:
        page_number = 1
    try:
        page_size = int(request.args.get('page-size'))
    except:
        page_size = 10
    if len(final) >= page_size:
        low = ((page_number-1) * (page_size))
        high = low + page_size 
        return {"data":final[low:high],"metadata":{"page_count":len(final)//page_size,"page_number":page_number,"page_size":page_size,"record_count":len(course_objects)}}
    else:
        return {"data":final,"metadata":{"page_count":len(final)//page_size,"page_number":page_number,"page_size":page_size,"record_count":len(course_objects)}}

    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE


@app.route("/course", methods=['POST'])
def create_course():
    input_data = request.json
    json_file = open("./json/course.json",'r+')
    course_objects = json.load(json_file)
    json_file.close()
    new_id = course_objects[-1]["id"] + 1
    input_data['id'] = new_id
    course_objects.append(input_data)
    course_objects = json.dumps(course_objects)
    json_file = open("./json/course.json",'w+')
    json_file.write(course_objects)
    json_file.close()
    return {"data":input_data}
    
    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE
    input_data = request.json
    json_file = open("./json/course.json",'r+')
    course_objects = json.load(json_file)
    json_file.close()
    object_count = 0
    for i in course_objects:
        if i['id'] == id:
            course_objects[object_count]=input_data
        object_count+=1    
    course_objects = json.dumps(course_objects)
    json_file = open("./json/course.json",'w+')
    json_file.write(course_objects)
    json_file.close()
    return {"data":input_data}


@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE
    json_file = open("./json/course.json",'r+')
    course_objects = json.load(json_file)
    json_file.close()
    flag = 0
    for i in course_objects:
        if i['id'] == id:
            course_objects.remove(i)
            flag = 1
    course_objects = json.dumps(course_objects)
    json_file = open("./json/course.json",'w+')
    json_file.write(course_objects)
    json_file.close()
    if flag ==1:
        return {"message":"Object deleted successfully"}
    else:
        return {"message":"Object not found"}