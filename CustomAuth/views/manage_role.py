import json
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.db import transaction
from django.db.models import F, Max
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from CustomAuth.models import ProfessionalType
from CustomAuth.models_grp_role import MstGroup, MstGroupRole, MstRole, MstMenuItem, MstUserGroup, MstRoleMenuItem
from CustomAuth.models import ProfessionalType, User


def edit_group(request):
    if request.method == 'POST':
        group_id = request.POST.get('groupid')
        group_name = request.POST.get('GroupName')
        group_desc = request.POST.get('GroupDesc')
        group_status = request.POST.get('EditGroupstatus')
        selected_roles = set(map(int, request.POST.getlist('roles')))  # Convert to integers
        try:
            # Use get_object_or_404 to retrieve the group
            group = get_object_or_404(MstGroup, GroupId=group_id)

            # Update the group details
            group.GroupName = group_name
            group.GroupDesc = group_desc
            group.ActiveFlag = group_status
            group.save()

            # Use transaction.atomic to ensure all changes are made or none
            with transaction.atomic():
                # Update roles for the group
                group_roles = MstGroupRole.objects.filter(GroupIdFK=group)
                existing_roles = set(role.RoleIdFK.RoleId for role in group_roles)
                for selected_role_id in selected_roles:
                    # Check if the role is already associated with the group
                    if selected_role_id not in existing_roles:
                        print("Creating Role:", selected_role_id)
                        # Role is not associated, create a new MstGroupRole instance
                        role = MstRole.objects.get(RoleId=selected_role_id)
                        # Assuming 'now()' is the function to get the current date and time in your database
                        MstGroupRole.objects.create(
                            GroupIdFK=group,
                            RoleIdFK=role,
                            ClinicId=1,
                            ActiveFlag='A',
                            CreatedBy=1,
                            UpdatedBy=1,
                            CreationDateTime=timezone.now(),
                            UpdationDateTime=timezone.now(),
                        )
                    else:
                        print("Role already exists:", selected_role_id)

                # Deactivate roles that are not selected in the form
                group_roles.exclude(RoleIdFK__RoleId__in=selected_roles).update(ActiveFlag='I')

            messages.success(request, 'Group updated successfully.')
        except MstGroup.DoesNotExist:
            messages.error(request, 'Group not found.')

    return redirect('Group')


def delete_group(request, group_id):
    group = get_object_or_404(MstGroup, GroupId=group_id)

    # Soft-delete associated roles by setting DeleteFlag to 'I'
    MstGroupRole.objects.filter(GroupIdFK=group).update(DeleteFlag='I')

    # Soft-delete the group by setting DeleteFlag to 'I'
    group.DeleteFlag = 'I'
    group.save()

    messages.success(request, 'Group and associated roles soft-deleted successfully.')
    return redirect('Group')


def Group(request):
    menu_itemss = MstMenuItem.objects.filter(DeleteFlag='A').order_by('MenuItemId')
    submenu_items = MstMenuItem.objects.filter(DeleteFlag='A').exclude(MainMenuId=F('MenuItemId')).order_by \
        ('MenuItemName', 'MenuItemId').distinct('MenuItemName')
    roles = MstRole.objects.filter(DeleteFlag='A')
    all_groups = MstGroup.objects.filter(DeleteFlag='A')
    User_group = MstUserGroup.objects.filter(DeleteFlag='A').distinct('UserIdFK')
    All_user_group = MstUserGroup.objects.filter(DeleteFlag='A')
    Pro_Type = ProfessionalType.objects.filter(active=True)
    role_menu_items = []

    for role in roles:
        role_id = role.RoleId
        role_name = role.RoleName
        role_flag = role.ActiveFlag
        role_desc = role.RoleDesc

        # Find related menu items for the current role
        menu_items = MstRoleMenuItem.objects.filter(RoleIdFK=role_id, DeleteFlag='A' ,ActiveFlag='A').values \
            ('MenuItemIdFK')

        # Get the menu item names and IDs for the current role
        menu_item_names = MstMenuItem.objects.filter(MenuItemId__in=menu_items, DeleteFlag='A')

        # Separate menu items and submenus based on your condition
        menu_items_list = []
        submenus_list = []  # New list to store submenus

        for item in menu_item_names:
            if item.MainMenuId == item.MenuItemId:
                menu_items_list.append(item)
            else:
                submenus_list.append(item)
        # Append the role name, role ID, and menu items and submenus to the result list
        role_menu_items.append({
            'RoleName': role_name,
            'RoleId': role_id,
            'MenuItems': menu_items_list,
            'Submenus': submenus_list,  # Include the list of submenus
            'ActiveFlag': role_flag,
            'RoleDesc': role_desc
        })

    group_menu_items = []

    for group in all_groups:
        group_id = group.GroupId
        group_name = group.GroupName
        group_desc = group.GroupDesc
        group_flag = group.ActiveFlag

        # Fetch roles related to the group
        group_roles = MstRole.objects.filter(mstgrouprole__GroupIdFK=group_id, DeleteFlag='A')

        roles_list = []

        for role in group_roles:
            role_id = role.RoleId
            role_name = role.RoleName
            role_flag = role.ActiveFlag
            role_desc = role.RoleDesc

            # Find related menu items for the current role
            menu_items = MstRoleMenuItem.objects.filter(RoleIdFK=role_id, DeleteFlag='A' ,ActiveFlag='A').values \
                ('MenuItemIdFK')

            # Get the menu item names and IDs for the current role
            menu_item_names = MstMenuItem.objects.filter(MenuItemId__in=menu_items, DeleteFlag='A')

            # Separate menu items and submenus based on your condition
            role_menu_items_list = []
            role_submenus_list = []


            for item in menu_item_names:
                if item.MainMenuId == item.MenuItemId:
                    role_menu_items_list.append(item)
                else:
                    role_submenus_list.append(item)

            # Append the role information to the roles_list
            roles_list.append({
                'RoleName': role_name,
                'RoleId': role_id,
                'MenuItems': role_menu_items_list,
                'Submenus': role_submenus_list,  # Include the list of submenus
                'ActiveFlag': role_flag,
                'RoleDesc': role_desc
            })

        # Append the group information along with its roles to the group_menu_items list
        group_menu_items.append({
            'GroupName': group_name,
            'GroupId': group_id,
            'GroupDesc': group_desc,
            'GroupFlag': group_flag,
            'Roles': roles_list
        })

    return render(request, 'group.html', {'menu_items': menu_itemss, 'submenu_items': submenu_items, 'role_menu_items': role_menu_items, 'group_data': group_menu_items ,'User_group' :User_group ,'Pro_Type' :Pro_Type
                   ,'all_groups' :all_groups ,'All_user_group' :All_user_group})


class MenuItemEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, MstMenuItem):
            return {
                'MenuItemId': obj.MenuItemId,
                'MenuName': obj.MenuItemName,
                'MainMenuId': obj.MainMenuId,
                # Add other fields as needed
            }
        return super().default(obj)


def get_group_info(request, group_id):
    if request.method == 'POST':
        group_id = group_id
        # Retrieve the group information based on the group_id
        group = get_object_or_404(MstGroup, GroupId=group_id)
        # Retrieve roles related to the group
        group_roles = MstRole.objects.filter(mstgrouprole__GroupIdFK=group_id, DeleteFlag='A')
        roles_data = []
        for role in group_roles:
            role_id = role.RoleId
            role_name = role.RoleName
            role_flag = role.ActiveFlag
            role_desc = role.RoleDesc

            # Find related menu items for the current role
            menu_items = MstRoleMenuItem.objects.filter(RoleIdFK=role_id, DeleteFlag='A').values('MenuItemIdFK')

            # Get the menu item names and IDs for the current role
            menu_item_names = MstMenuItem.objects.filter(MenuItemId__in=menu_items)

            # Convert menu_item_names to a list using the custom encoder
            menu_items_serialized = json.loads(json.dumps(list(menu_item_names), cls=MenuItemEncoder))
            role_menu_items_list = []
            role_submenus_list = []

            for item in menu_items_serialized:
                if item['MainMenuId'] == item['MenuItemId']:
                    role_menu_items_list.append(item)
                else:
                    role_submenus_list.append(item)

            # Append the role information to the roles_data list
            roles_data.append({
                'RoleName': role_name,
                'RoleId': role_id,
                'MenuItems': [menu_item['MenuName'] for menu_item in role_menu_items_list],
                'Submenus': [submenu['MenuName'] for submenu in role_submenus_list],
                'ActiveFlag': role_flag,
                'RoleDesc': role_desc
            })




        # Return the data as JSON response
        group_data = {
            'GroupName': group.GroupName,
            'GroupFlag': group.ActiveFlag,
            'GroupDesc': group.GroupDesc,
            'Roles': roles_data,
        }

        return JsonResponse({'group_data': group_data}, encoder=MenuItemEncoder)
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid request method'})


def create_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('User_Id')
        professional_type_id = request.POST.get('CreateUserptid')
        user_desc = request.POST.get('User_desc')
        is_active = request.POST.get('is_active')
        User_number = request.POST.get('User_number')
        user_groups = request.POST.getlist('User_groups')
        new_group_descs = request.POST.getlist('newGroupDesc[]')

        if is_active == 'A':
            is_active = True
        else:
            is_active = False

        user_profession = ProfessionalType.get_profession_by_id(professional_type_id)

        # Assuming you need to create a new user first
        new_user = User.objects.create(
            username=user_profession.name[0] + str(User.objects.all().count() + 1).zfill(6),
            email=user_id,
            profession=user_profession,
            # UserDesc=user_desc,
            phone=User_number,
            is_active=is_active,
        )

        # Assuming you want to associate the user with multiple groups
        for group_id, group_desc in zip(user_groups, new_group_descs):
            MstUserGroup.objects.create(
                UserIdFK=request.user,
                GroupIdFK=MstGroup.get_group_id_by_id(group_id),
                ClinicId=1,  # Replace with your actual ClinicId value
                ActiveFlag='A',  # Replace with your actual value
                CreatedBy='1',  # Replace with your actual user ID
                UpdatedBy='1',  # Replace with your actual user ID
                CreationDateTime=timezone.now(),
                UpdationDateTime=timezone.now(),
            )


        return redirect('Group')

def edit_user(request):
    if request.method == 'POST':

        return redirect('Group')

def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, UserId=user_id)

        # Perform the deletion logic here
        user.DeleteFlag = 'I'
        user.save()

        # Additionally, if you want to set DeleteFlag='I' for associated user groups:
        user_groups = MstUserGroup.objects.filter(UserIdFK=user)
        user_groups.update(DeleteFlag='I')

        return JsonResponse({'message': 'User deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def get_user_info(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')

        try:
            user_groups = MstUserGroup.objects.filter(UserIdFK=user_id)
            group_list = []

            for user_group in user_groups:
                group_data = {
                    'GroupIdFk': user_group.GroupIdFK,
                    'GroupName': user_group.GroupIdFk.GroupName,
                }
                group_list.append(group_data)

            return JsonResponse(group_list, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_desc = request.POST.get('group_desc')
        is_active = request.POST.get('is_active')
        selected_roles = request.POST.getlist('selected_roles')
        # Step 1: Create a new group
        group = MstGroup.objects.create(
            GroupName=group_name,
            GroupDesc=group_desc,
            ClinicId=1,  # Replace with the actual ClinicId
            ActiveFlag=is_active,
            CreatedBy=1,  # Replace with the actual CreatedBy
            UpdatedBy=1,  # Replace with the actual UpdatedBy
            CreationDateTime=timezone.now(),
            UpdationDateTime=timezone.now()
        )

        # Step 2: Add selected roles to the MstGroupRole table
        for role_id in selected_roles:
            MstGroupRole.objects.create(
                GroupIdFK=group,
                RoleIdFK=MstRole.get_role_id_by_id(role_id),
                ClinicId=1,
                ActiveFlag=is_active,
                CreatedBy=1,
                UpdatedBy=1,
                CreationDateTime=timezone.now(),
                UpdationDateTime=timezone.now()
            )

        return redirect('Group')


def edit_role(request):
    if request.method == 'POST':
        role_id = request.POST.get('roleid')
        role_name = request.POST.get('roleName')
        role_description = request.POST.get('roleesc')
        is_active = request.POST.get('Editrolestatus')
        selected_menu_items = set(request.POST.getlist('menu_item'))
        print(selected_menu_items)
        role = get_object_or_404(MstRole, RoleId=role_id)

        # Step 2: Update the fields
        role.RoleName = role_name
        role.RoleDesc = role_description
        role.ActiveFlag = is_active
        role.UpdationDateTime = timezone.now()

        # Step 3: Save the object
        role.save()

        # Get all role menu items for the given role_id
        role_menu_items = MstRoleMenuItem.objects.filter(RoleIdFK=role_id)

        # Iterate over existing menu items and update ActiveFlag
        for role_menu_item in role_menu_items:
            menu_item_id = str(role_menu_item.MenuItemIdFK)
            if menu_item_id not in selected_menu_items:
                # If menu_item_id is not in selected_menu_items, set ActiveFlag to 'I'
                role_menu_item.ActiveFlag = 'I'
                role_menu_item.save()
            else:
                # If menu_item_id is not in selected_menu_items, set ActiveFlag to 'I'
                role_menu_item.ActiveFlag = 'A'
                role_menu_item.save()

        # Add new menu items if any
        existing_menu_item_ids = {str(item.MenuItemIdFK) for item in role_menu_items}
        new_menu_item_ids = selected_menu_items - existing_menu_item_ids

        for new_menu_item_id in new_menu_item_ids:
            # Create new MstRoleMenuItem entries for new_menu_item_ids
            MstRoleMenuItem.objects.create(
                RoleIdFK=role,
                MenuItemIdFK=new_menu_item_id,
                ClinicId=1,
                ActiveFlag='A',
                CreatedBy=1,
                UpdatedBy=1,
                CreationDateTime=timezone.now(),
                UpdationDateTime=timezone.now()
            )

        return redirect('Group')


# Retrieve role menu items based on role_id from your database
def get_role_menu_items(role_id):
    role_menu_items = MstRoleMenuItem.objects.filter(RoleIdFK=role_id, ActiveFlag='A')
    main_menu_items = []
    submenu_items = []

    # Separate main menu items and submenu items
    for role_menu_item in role_menu_items:
        if role_menu_item.MenuItemIdFK.MainMenuId == role_menu_item.MenuItemIdFK.MenuItemId:
            main_menu_items.append({
                'MenuItemId': role_menu_item.MenuItemIdFK.MenuItemId,
                'MenuItemName': role_menu_item.MenuItemIdFK.MenuItemName
            })
        else:
            submenu_items.append({
                'MenuItemId': role_menu_item.MenuItemIdFK.MenuItemId,
                'MenuItemName': role_menu_item.MenuItemIdFK.MenuItemName
            })

    # Create a dictionary containing main menu items and their submenus
    menu_items = {}
    for main_menu in main_menu_items:
        menu_items[main_menu['MenuItemId']] = {
            'MainMenuId': main_menu['MenuItemId'],
            'MenuItemName': main_menu['MenuItemName'],
            'Submenus': []
        }

    # Retrieve all submenus associated with the main menu items
    all_submenus = MstMenuItem.objects.filter(MainMenuId__in=menu_items.keys()).exclude(MainMenuId=F('MenuItemId'))

    for submenu in all_submenus:
        main_menu_id = submenu.MainMenuId
        if main_menu_id in menu_items:
            menu_items[main_menu_id]['Submenus'].append({
                'MenuItemId': submenu.MenuItemId,
                'MenuItemName': submenu.MenuItemName,
            })

    return JsonResponse(menu_items, safe=False)

def create_role(request):
    if request.method == 'POST':
        role_name = request.POST.get('RoleName')
        role_description = request.POST.get('Role_Description')
        is_active = request.POST.get('Role_status')  # Assuming this is a hidden input with the active state

        # Create a new role record
        new_role = MstRole(RoleName=role_name, RoleDesc=role_description, ClinicId=12, ActiveFlag=is_active
                           ,CreatedBy=1,
                           UpdatedBy=1,
                           CreationDateTime=timezone.now(),
                           UpdationDateTime=timezone.now(),
                           )
        new_role.save()

        # Extract the selected menu items from the form
        selected_menu_items = request.POST.getlist('selected_menu_items')


        # Create Role-Menu mappings
        for menu_item_id in selected_menu_items:
            menu_item = MstMenuItem.objects.get(pk=menu_item_id)
            role_menu_mapping = MstRoleMenuItem(RoleIdFK=new_role, MenuItemIdFK=menu_item ,ClinicId=12, CreatedBy=1, UpdatedBy=1, CreationDateTime=timezone.now() ,UpdationDateTime=timezone.now())
            role_menu_mapping.save()

        return redirect('Group')

def delete_role(request, role_id):
    role = get_object_or_404(MstRole, RoleId=role_id)
    role_menu_items = MstRoleMenuItem.objects.filter(RoleIdFK=role_id)

    # Update delete flag for MstRole
    role.DeleteFlag = 'I'
    role.save()

    # Update delete flag for related MstRoleMenuItem records
    for role_menu_item in role_menu_items:
        role_menu_item.ActiveFlag = 'I'
        role_menu_item.save()

    return JsonResponse({'message': 'Role deleted successfully'})

# this function belongs to main menu
def delete_menu_item(request):
    if request.method == 'POST':
        menu_item_id = request.POST.get('menu_item_id')
        try:
            menu_item = MstMenuItem.objects.get(MenuItemId=menu_item_id)
            menu_item.DeleteFlag = 'I'
            menu_item.save()
            return JsonResponse({'message': 'Item deleted successfully'})
        except MstMenuItem.DoesNotExist:
            return JsonResponse({'message': 'Item not found'}, status=404)

# this function belongs to main menu
@csrf_exempt  # Apply the CSRF exemption if needed
def update_menu_item(request):
    if request.method == 'POST':
        menu_id = request.POST.get('menuId')
        menu_name = request.POST.get('menuName')
        SubMenu = request.POST.get('SubMenu')
        menu_description = request.POST.get('menuDescription')
        menu_status = request.POST.get('menuStatus')

        try:
            # Retrieve the menu item by its primary key (MenuItemId)
            menu_item = MstMenuItem.objects.get(MenuItemId=menu_id)
            # Update the menu item's attributes
            if SubMenu == '0':
                menu_item.MenuItemName = menu_name
            else:
                menu_item.MenuItemName = SubMenu
            menu_item.MenuItemDesc = menu_description
            menu_item.ActiveFlag = menu_status

            # Save the changes to the database
            menu_item.save()

            response_data = {'message': 'Update successful'}
        except MstMenuItem.DoesNotExist:
            response_data = {'error': 'Menu item does not exist.'}
        except Exception as e:
            response_data = {'error': f'Error updating menu item: {str(e)}'}
    else:
        response_data = {'error': 'Invalid request method.'}

    return JsonResponse(response_data)

# this function belongs to main menu
def submit_form(request):
    if request.method == 'POST':

        main_menu_name = request.POST.get('main_menu_name')
        main_menu_desc = request.POST.get('main_menu_desc')
        main_menu_flg = request.POST.get('main_menu_flg')
        sub_menu_name = request.POST.getlist('sub_menu_name')
        sub_menu_flg = request.POST.getlist('sub_menu_flg')
        sub_menu_link = request.POST.getlist('sub_menu_link')

        # Find the max MenuItemId
        max_menu_item_id = MstMenuItem.objects.aggregate(Max('MenuItemId'))['MenuItemId__max'] or 0

        with transaction.atomic():
            # Create the main menu item
            main_menu_item = MstMenuItem(
                MenuItemId=max_menu_item_id + 1,
                MenuItemName=main_menu_name,
                MenuItemDesc=main_menu_desc,
                MainMenuId=max_menu_item_id + 1,
                WebpageLink=' ',
                ClinicId=12,
                ActiveFlag=main_menu_flg ,
                CreatedBy=1,
                UpdatedBy=1,
                CreationDateTime=timezone.now(),
                UpdationDateTime=timezone.now(),
            )

            main_menu_item.save()

            # Create the sub-menu items
            for idx, sub_name in enumerate(sub_menu_name):
                sub_menu_item = MstMenuItem(
                    MenuItemId=max_menu_item_id + idx + 2,
                    MenuItemName=sub_name,
                    MenuItemDesc='',
                    MainMenuId=max_menu_item_id + 1,
                    WebpageLink=sub_menu_link[idx],
                    ClinicId=12,
                    ActiveFlag=sub_menu_flg[idx],
                    CreatedBy=1,
                    UpdatedBy=1,
                    CreationDateTime=timezone.now(),
                    UpdationDateTime=timezone.now()
                )

                sub_menu_item.save()

        request.session['alert-success'] = 'Menu items updated successfully. Please manage roles to see changes.'
        return redirect('Group')