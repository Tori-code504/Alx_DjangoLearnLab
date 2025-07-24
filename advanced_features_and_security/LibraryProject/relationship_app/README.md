## Role-Based Permissions Setup

- Custom permissions were added to the `Book` model:
  - can_view, can_create, can_edit, can_delete

- Django Groups:
  - Viewers: has `can_view`
  - Editors: has `can_create`, `can_edit`
  - Admins: has all permissions

- Permissions are enforced in views using `@permission_required`.

- Use the admin panel to manage user group assignments.
