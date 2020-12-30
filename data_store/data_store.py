import json
import os


class ValueInvalidException(Exception):
    """
    raise a custom value Exception.
    """
    pass


class KeyInvalidException(Exception):
    """
    raise a custom key Exception.
    """
    pass


class DataInvalidException(Exception):
    """
    raise data more than 10KB Exception.
    """
    pass


DATASTORE_LOCATION = '{}/data'.format(os.getcwd())


class DataStore:

    def __init__(self, key):
        self.key = key
        self.validate_key()

    def validate_data(self):
        """
        Validate the size of the data in the data folder that must be
        less than 10KB.
        This can also be changed to less than 1GB.
        :return: error if data is more than 10KB
        """
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(DATASTORE_LOCATION):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)

        if total_size > 10*1024:
            raise DataInvalidException("The Size of the data must be less than 10KB")

    def validate_key(self):
        """
        Validate the length of the key is less than 16 KB
        :return: type:str
        """
        if type(self.key) != str:
            raise KeyInvalidException("The Key was not of type str")
        if not 0 < len(self.key) <= 32:
            raise KeyInvalidException("The Length of the key must be less than 32 characters")

    def validate_value(self, value):

        """
        Validate the length of the value is less than 32 character
        :param value: type: JSON value
        :return: type:JSON value
        """
        if type(value) != dict:
            raise ValueInvalidException("The value was not of type JSON value")
        if not 0 < len(value) <= 16 * 1024:
            raise ValueInvalidException("The Length of the value must be less than 16KB")

    def create(self, value):

        """
        Create a file which will create a JSON value for the corresponding key.
         If the key already exist return error, else create a JSON value
        :param value: type:JSON value.
        :return: type:None.
        """
        self.validate_data()
        self.validate_value(value)
        print("Create function called with key={}, value={}".format(self.key, value))
        file = open("{}/{}.json".format(DATASTORE_LOCATION, self.key), "x")
        file.write(json.dumps(value))
        file.close()
        print("File Created Successfully")

    def read(self):

        """
        Read the file which contains JSON value and return the value corresponding to the key.
         If the key exist return JSON value, else return an error
        :return: type:JSON value.
        """

        print("Read function called with key {}".format(self.key))
        file = open("{}/{}.json".format(DATASTORE_LOCATION, self.key), "r")
        value = json.loads(file.read())
        file.close()
        return value

    def delete(self):

        """
        Delete the JSON value in the file corresponding to the key.
        If the key does not exist then return an error, else delete a JSON value
        :return: type:None.
        """

        print("Delete function called with key {}".format(self.key))
        os.remove("{}/{}.json".format(DATASTORE_LOCATION, self.key))
        print("File Deleted Successfully")
