def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)

fn = input("Enter your first name: ")
ln = input("Enter your last name: ")
ho = input("What you like to do during your leisure time? ")
jo = input("Your occupation is? ")
GP = input("Tell me your GPA: ")

my_profile = build_profile(fn, ln, hobby = ho, job = ho, GPA = GP)
print(my_profile)

############
def sandwiches(*items):
    sandwiches_items = []
    sandwiches_items.append(items)
    return sandwiches_items

sandwiches_items = sandwiches('cucumber', 'tomato')
print(sandwiches_items)

sandwiches_items = sandwiches('onion', 'lettuse', 'olive')
print(sandwiches_items)

sandwiches_items = sandwiches('jalapeno', 'capsicum')
print(sandwiches_items)

