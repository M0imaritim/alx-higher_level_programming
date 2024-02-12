#!/usr/bin/python3
"""Module contains class Base"""

import json
import csv


class Base:
    """This is the base for all classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        em_lst = []
        if not list_objs:
            pass
        else:
            em_lst = [obj.to_dictionary() for obj in list_objs]
            with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as f:
                f.write(cls.to_json_string(em_lst))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(15, 15)
        else:
            dummy = cls(15)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                list_inst = cls.from_json_string(f.read())
                return [cls.create(**kwas) for kwas in list_inst]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method saves csv into a file"""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']

        with open(filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """method loads from file to csv"""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                read = csv.DictReader(f)
                inst = []
                for row in read:
                    for key, value in row.items():
                        if key != 'id':
                            row[key] = int(value)
                    inst.append(cls.create(**row))
            return inst
        except FileNotFoundError:
            return []
