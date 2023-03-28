[![](https://img.shields.io/pypi/pyversions/django-admin-interface.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)

# Django-tree-menu
1
Test assignment for an interview. Conditions for passing:

1) the menu is implemented through TemPlate Tag
2) everything that is on the dedicated point is deployed. The first level of investment under the highlighted point is
   also deployed.****
3) stored in the database.
4) is edited in the standard Django admin panel
5) the active menu item is determined based on the URL of the current page
6) There can be several menu on one page. They are determined by name.
7) When clicking on the menu, there is a transition at the URL specified in it. The URL can be set both in a clear way
   and through Named URL.
8) for the drawing of each menu, exactly 1 request to the database is required

## Show how it works

### Everything that is on the dedicated point is deployed

![sow.gif](media%2Fsow.gif)

### When clicking on the menu, there is a transition at the URL specified in it.

![sow2.gif](media%2Fsow2.gif)

### Is edited in the standard Django admin panel

![admin_panel.gif](media%2Fadmin_panel.gif)

![update.gif](media%2Fupdate.gif)

## Installation

```commandline
git clone git@github.com:YaraKoba/django_tree_menu.git
cd django_tree_menu
python -m venv venv
source venv/bin/activate
```

### Install requirements

```commandline
make install_requirements
```

### Run migrations

```commandline
make migrate
```

### Run server

```commandline
make runserver
```

## Usage

### Fronted available at

```commandline
http://127.0.0.1:8000/
```

### Admin panel available at

```commandline
http://127.0.0.1:8000/admin
```

### Admin panel login/password

```commandline
login: adminadmin
password: admin
```
