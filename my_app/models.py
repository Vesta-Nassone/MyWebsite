from django. \
    db import models


# Create your models here.
class Project(models.Model):
    # images
    image = models.ImageField(upload_to='images/')
    # summary
    description = models.CharField(max_length=200)
    # link to project
    project_url = models.CharField(max_length=2083)

    # String representation
    def __str__(self):
        return self.description
