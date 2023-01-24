from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    Campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=12, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):

        display_Campus = '{0.Campus_Name}: {0.State}'
        return display_Campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"