import math

from CustomAuth.models_grp_role import MstUserGroup, MstGroupRole, MstRoleMenuItem, MstMenuItem
# from Staff.models.menu_items import Menu, SubMenu


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
    elif not params.phone+params.phone == 2*params.phone:
        error_message = 'Phone number should be in number'
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


def get_user_menu(request):
    # user_grp = MstUserGroup.get_user_group_by_user_id(request)
    # # print(user_grp)
    # # print("user_grp.GroupIdFK", user_grp.GroupIdFK)
    #
    # grp_role = MstGroupRole.get_grp_rol_by_grp_id(user_grp.GroupIdFK)
    # for i in grp_role:
    #     pass
        # print("grp_role", i.GroupIdFK)
        # print("grp_role", i.GrouproleId)

    grp_role2 = MstGroupRole.get_gro_role_by_profession(request)
    data = []
    menu_menu = []
    for i in grp_role2:
        # print("Profession Grp role > RoleIdFK", i.RoleIdFK)
        role_menu = MstRoleMenuItem.get_role_menu_by_group_role_id(i.RoleIdFK)
        list = []
        main_menu = []
        for j in role_menu:
            # print("-----Main Menu", j.MenuItemIdFK.MenuItemName)
            main_menu.append(j.MenuItemIdFK.MenuItemName)
            list.append(main_menu)
            # menu = Menu.objects.get(name=j.MenuItemIdFK.MenuItemName)
            # sub_menu = SubMenu.objects.filter(menu=menu)
            # menu_menu.append(sub_menu)
            # print(menu)
            # print(sub_menu)
            menu_records = MstMenuItem.objects.filter(MainMenuId=j.MenuItemIdFK.MenuItemId)
            sub_menu = []
            for k in menu_records:
                sub_menu.append(k.MenuItemName)
            list.append(sub_menu)
        data.append(list)
        # print("list: ", list)
    print("data", data)
    menu_dict = {}
    for i in data:
        menu_dict[i[0][0]] = i[1]
    print(menu_dict)
    return menu_dict
