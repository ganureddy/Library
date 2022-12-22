import frappe

def create_custom_role(role_name, permissions):
    role = frappe.new_doc('Role')
    role.role_name = "Library Manager"
    role.permissions = permissions
    role.save()
    print("----------------------------------------------------")

# Example: create a role with the name "Custom Role" and permissions to access the "Customer" and "Supplier" doctypes
create_custom_role("Library Manager", [{"doctype": "Blogger"}])

