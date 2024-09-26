def sartorial_splendor_default(creature='cat', clothing='hat'):
    return f"the {creature} in the {clothing}"

# after supplying a default value, all remaining parameters must also have defaults
# def sartorial_splendor_error(creature='cat', clothing):
#     return f"the {creature} in the {clothing}"

# default params are evaluated ONLY ONCE
def add_to_list_surprise(word, word_list=[]):
    word_list.append(word)
    return word_list

def add_to_list_ok(word, word_list=None):
    word_list = [] if word_list is None else word_list
    word_list.append(word)
    return word_list
