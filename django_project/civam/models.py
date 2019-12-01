from django.db import models
from django.contrib.auth.models import User, Group

# Civam models are defined here
# Some models have created_by, created_on, modified_by, and modified_on fields
# created_on and modied_on are set automatically

# A Collection of items
# Each Collection has a title, description, cover_image, public (collection displayed on site if true)
class Collection(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="cover_images/", blank=True)
    public = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="collections_created")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="collections_modified")
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# An Item belongs to a Collection
# Each Item has a name and description (and the collection it belongs to)
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="items")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="items_created")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="items_modified")
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Images are uploaded in a folder corresponding to the collection and item ids    
def image_upload_path(instance, filename):
    return '{}/{}/{}'.format(instance.item.collection.id, instance.item.id, filename)

# An Image of an Item
# content is the path to the image
# Has an item that it belongs to
class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")
    content = models.ImageField(upload_to=image_upload_path)

    def __str__(self):
        return "Image: {}".format(self.item.name)

# A Video of an Item (link to external streaming service)
# Has an Item that it belongs to
class Video(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="videos")
    link = models.URLField()

    def __str__(self):
        return "Video: {}".format(self.item.name)

# A Story of an Item
# Each story has content (the story text) and an author (and an item it belongs to)
class Story(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="stories")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories_created")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories_modified")
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "stories"

    def __str__(self):
        return "Story: {}".format(self.item.name)

# Each CollectionGroup has a corresponding Group (Django Auth) and Collection
# Permissions on the Items in the Collection are defined for the Group
# Each CollectionGroup has a name that is unique within a given Collection
# If default is true, new users should automatically be added to this Group

# TO DO: If a CollectionGroup is deleted, the corresponding Group should be deleted
class CollectionGroup(models.Model):
    name = models.CharField(max_length=125)
    default = models.BooleanField(default=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="groups")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="collections")

    class Meta:
        # Cannot CollectionGroups with the same name defined on the same Collection
        unique_together = ('name', 'collection')
    
    def __str__(self):
        return "CollectionGroup: {} {}".format(self.collection.title, self.group.name)
