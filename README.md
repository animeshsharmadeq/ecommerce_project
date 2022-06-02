# E-Commerce Website

## Day-wise things to complete:

### **Day 1:**

### **Users can login:**

There will be three type of user Admin, Shopuser, and customer in web app, can login via email and password.

### Hints:

1. Create a django project with the name **“*ecommerce_project*”**.
2. You should use this lib [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
3. Extending the User model with custom fields(user_type) in [Django](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example)
4. Create github repo and push on master branch with commit name “Initial Commit”

### Tasks completed:

1. Created django project.
2. Installed django-allauth.
3. Created a separate Custom user model with user_type.
4. Pushed Initial Commit to github repository.

### Problems Faced / Blockers:

1. Unable to redirect the accounts/login to custom made html login template.(the signin is still happening from the allauth login UI)
2. Unable to modify the Add user screen in /admin/users/user/add.