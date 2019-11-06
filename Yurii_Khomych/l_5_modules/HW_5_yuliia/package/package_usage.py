import Yurii_Khomych.l_5_modules.HW_5_yuliia.package.yy_package.yy_function as func
import Yurii_Khomych.l_5_modules.HW_5_yuliia.package.yy_package.yy_collect_obj as roles
import Yurii_Khomych.l_5_modules.HW_5_yuliia.package.yy_package.yy_class as current_user

print('Who are you?')
if __name__ == "__main__":
    func.who_am_i(roles.user_roles, current_user.FindRole('admin').role)