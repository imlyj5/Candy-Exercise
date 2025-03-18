def get_friends_favorite_candy_count(favorites):
    frequency = {}
    for friend in favorites:
        for candy in friend[1]:
            if candy not in frequency:
                frequency[candy] = 1
            else:
                frequency[candy]+=1
    return frequency

def create_new_candy_data_structure(data):
    preference = {key: [] for key in get_friends_favorite_candy_count(data).keys()}
    for friend in data:
        for candy in friend[1]:
            if candy in preference:
                preference[candy].append(friend[0])
    return preference


def get_friends_who_like_specific_candy(data, candy_name):
    return tuple(create_new_candy_data_structure(data)[candy_name])

def create_candy_set(data):
    candy_set = set()
    for key in create_new_candy_data_structure(data).keys():
        candy_set.add(key)
    return candy_set


friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

favorite_candy_count = get_friends_favorite_candy_count(friend_favorites)
# print(favorite_candy_count)
# print(create_new_candy_data_structure(friend_favorites))
print(get_friends_who_like_specific_candy(friend_favorites, 'laffy taffy'))
# print(create_candy_set(friend_favorites))