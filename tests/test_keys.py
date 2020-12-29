import pytest

from data_store.data_store import DataStore, KeyInvalidException


def test_key_zero():
    with pytest.raises(KeyInvalidException):
        o = DataStore(key='')


def test_key_more_than_33_char():
    with pytest.raises(KeyInvalidException):
        o = DataStore(key='some_large_keysome_large_keysome_large_keysome_large_keysome_large_keysome_large_key')


# Value 0
# Value > 16KB
# Value = not JSON

# Call Create for same Key
# Delete not existent key
# Read Non existent key