# Django-tree-menu
Test assignment for an interview. Conditions for passing:
1) the menu is implemented through TemPlate Tag
2) everything that is on the dedicated point is deployed. The first level of investment under the highlighted point is also deployed.****
3) stored in the database.
4) is edited in the standard Django admin panel
5) the active menu item is determined based on the URL of the current page
6) There can be several menu on one page. They are determined by name.
7) When clicking on the menu, there is a transition at the URL specified in it. The URL can be set both in a clear way and through Named URL.
8) for the drawing of each menu, exactly 1 request to the database is required

## Show how it works
### Everything that is on the dedicated point is deployed
![sow.gif](media%2Fsow.gif)

### When clicking on the menu, there is a transition at the URL specified in it.
![sow2.gif](media%2Fsow2.gif)

### Is edited in the standard Django admin panel
![admin_panel.gif](media%2Fadmin_panel.gif)


![update.gif](media%2Fupdate.gif)

## Solutions
1) To implement the menu using Template Tags in Django, I create
a custom template tag that fetches 
the menu items from the database and renders 
them in the HTML template. This can be done 
using the `inclusion_tag` decorator provided by Django.

![inclusion_tag.png](media%2Finclusion_tag.png)
2) to deploy everything on a dedicated point and 
the first level of investment under it, 
I use recursion to traverse the tree 
structure in templates.

![create_children.png](media%2Fcreate_children.png)
3) To store data in the database, I define Django 
models and use Django's ORM to interact with the database. Also
To determine the active menu item based on the URL of the current page,
I used the `get_url` function in the model and then compare it with 
the URLs of your menu items.

![models.png](media%2Fmodels.png)

## Installation
```commandline
git clone git@github.com:YaraKoba/django_tree_menu.git
```
### install requirements
```commandline
pip install -r requirements.txt
```

### make migration
Change directory to `TestTask`
```commandline
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```