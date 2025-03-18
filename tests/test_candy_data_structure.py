import pytest
from candy_problem.candy_problem import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8
    '''
    Add your assertions here!
    '''
    assert new_candy_data["lollipop"] == ["Sally", "Bob"]
    assert new_candy_data["bubble gum"] == ["Sally"]
    assert new_candy_data["laffy taffy"] == ["Sally", "Arlene","Carlie"]

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''
def test_get_friends_who_like_specific_candy():
     # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    friend_candy_data = get_friends_who_like_specific_candy(friend_favorites, "lollipop")
    assert friend_candy_data == ("Sally", "Bob")

def test_create_candy_set():
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    candy_set = {"lollipop","bubble gum","laffy taffy","milky way","licorice","chocolate bar","nerds","sour patch kids"}
    assert create_candy_set(friend_favorites) == candy_set
    assert len(create_candy_set(friend_favorites)) == 8