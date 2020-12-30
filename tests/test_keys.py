import pytest

from data_store.data_store import DataStore, KeyInvalidException


def test_key_zero():
    with pytest.raises(KeyInvalidException):
        o = DataStore(key='')


def test_key_more_than_33_char():
    with pytest.raises(KeyInvalidException):
        o = DataStore(key='some_large_keysome_large_keysome_large_keysome_large_keysome_large_keysome_large_key')


def test_create_for_same_key():
    with pytest.raises(FileExistsError):
        # If same file executed twice raise File exists error.
        o = DataStore(key='test3')
        o.create(value={'1': 1})
        o = DataStore(key='test3')
        o.create(value={'1': 2})
    o.delete()



def test_read_non_existent_key():
    with pytest.raises(FileNotFoundError):
        # If the file does not exists.
        o = DataStore(key='test4')
        o.read()




def test_delete_not_existent_key():
    with pytest.raises(FileNotFoundError):
        # If the file does not exists.
        o = DataStore(key='test5')
        o.delete()


def test_key_not_string():
    with pytest.raises(KeyInvalidException):
        o = DataStore(key=1234)
import pytest

from data_store.data_store import DataStore, KeyInvalidException


def test_key_zero():
    with pytest.raises(KeyInvalidException):
        o = DataStore(key='')


def test_key_more_than_33_char():
    with pytest.raises(KeyInvalidException):
        o = DataStore(key='some_large_keysome_large_keysome_large_keysome_large_keysome_large_keysome_large_key')


def test_create_for_same_key():
    with pytest.raises(FileExistsError):
        # If same file executed twice raise File exists error.
        o = DataStore(key='test3')
        o.create(value={'1': 1})
        o = DataStore(key='test3')
        o.create(value={'1': 2})
    o.delete()



def test_read_non_existent_key():
    with pytest.raises(FileNotFoundError):
        # If the file does not exists.
        o = DataStore(key='test4')
        o.read()




def test_delete_not_existent_key():
    with pytest.raises(FileNotFoundError):
        # If the file does not exists.
        o = DataStore(key='test5')
        o.delete()


def test_key_not_string():
    with pytest.raises(KeyInvalidException):
        o = DataStore(key=1234)
