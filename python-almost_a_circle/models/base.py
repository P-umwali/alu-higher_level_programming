#!/usr/bin/python3
""" base class codes"""


import json


class Base:
    '''
      Attributes: id number
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returning JSON string of list_dictionaries
        '''

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''''Writing the JSON string  of list_objs to a file'''

        filename = cls.__name__ + ".json"
        list_dic = []

        if list_objs is not None:
            for obj in list_objs:
                list_dic.append(obj.to_dictionary())

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        '''Returning JSON string list representation of json_string'''

        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returning an instance with all the attributes  that are set'''

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file_csv(cls):
        '''Returning  a list of instances'''

        filename = cls.__name__ + ".json"
        list_instances = []

        try:
            with open(filename, 'r') as f:
                list_dic = cls.from_json_string(f.read())
                for dict in list_dic:
                    list_instances.append(cls.create(**dict))
                return list_instances
        except:
            return []
