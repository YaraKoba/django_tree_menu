from django.db import models
from django.dispatch import receiver
from django.urls import reverse


class MenuGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class MenuItem(models.Model):
    text = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=55, unique=True, db_index=True, verbose_name='URL')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    url = models.CharField(max_length=100)
    group = models.ForeignKey(MenuGroup, related_name='menuitem', on_delete=models.CASCADE)

    def __str__(self):
        return f'text: {self.text}, group: {self.group}'

    def get_children(self):
        return ", ".join([child.text for child in self.children.all()])

    get_children.short_description = "Children"

    class Meta:
        verbose_name_plural = "Menu Items"

    def get_url(self):
        return reverse('menu', kwargs={'menu_id': self.group.pk, 'menu_item_id': self.pk})




# class MenuGroup(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f'{self.name}'
# class MenuItem(models.Model):
#     text = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=55, unique=True, db_index=True, verbose_name='URL')
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
#     url = models.CharField(max_length=100)
#     group = models.ForeignKey(MenuGroup, related_name='menuitem', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'text: {self.text}, group: {self.group}'
#
#     def get_url(self):
#         return reverse('menu', kwargs={'menu_id': self.group.pk, 'menu_item_id': self.pk})
