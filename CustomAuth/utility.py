import math


def gen_user_unique_code(number):
    rounded = 10 ** (math.floor(math.log(number, 10) - math.log(0.5, 10)))
    return "{number:06}".format(number=int(rounded))


def custom_validator(params):
    error_message = None
    if not params.first_name:
        if params.profession.name == 'Patient':
            pass
        else:
            error_message = "First Name Required !!"
    # elif len(params.first_name) < 5:
    #     error_message = 'First Name must be at least 5 char long'
    # elif not params.last_name:
    #     error_message = 'Last Name Required'
    # elif len(params.last_name) < 4:
    #     error_message = 'Last Name must be 4 char long or more'
    elif not params.phone:
        error_message = 'Phone Number required.'
    elif len(params.phone) != 10:
        error_message = 'Phone Number must be in 10 digits.'
    elif len(params.password) < 8:
        error_message = 'Password must be 8 char long'
    elif not params.email:
        error_message = 'Email is required.'
    elif params.isExistsPhone(params.phone):
        error_message = 'Phone Number Already Registered..'
    elif params.isExistsEmail():
        error_message = 'Email Address Already Registered..'
    # saving
    return error_message
