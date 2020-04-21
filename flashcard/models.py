from django.db import models

class KanjiN2 (models.Model):
    week = models.IntegerField()
    unit = models.IntegerField()
    main_word = models.CharField(max_length=5, unique=True)
    meanning = models.CharField(max_length=15)
    kotoba = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.main_word