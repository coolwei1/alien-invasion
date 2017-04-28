import user
import admin_pri

admin = admin_pri.Admin('chek wei', 'tan')

user.User.describe_user(admin)

print("\nAdmin privileges: ")
admin_pri.Privilages.show_privileges('can eat', 'can play', 'can edits');