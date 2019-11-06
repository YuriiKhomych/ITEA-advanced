def who_am_i(collection_obj, arg2):
    if arg2 not in collection_obj:
        print("Our system doesn't have such user")
    else:
        print("You are "+arg2)
