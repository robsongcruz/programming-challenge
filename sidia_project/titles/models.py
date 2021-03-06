from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Title(models.Model):
    title_id = models.AutoField(primary_key=True)
    tconst = models.CharField(max_length=20)
    title_type = models.CharField(max_length=20)
    primary_title = models.CharField(max_length=450)
    original_title = models.CharField(max_length=450)
    is_adult = models.BooleanField()
    start_year = models.IntegerField(validators=[MinValueValidator(1, message='The year must be at least 1'), 
                                                MaxValueValidator(9999, message='The year must be up to 9999')], 
                                    null=True)
    end_year = models.IntegerField(validators=[MinValueValidator(1, message='The year must be at least 1'), 
                                                MaxValueValidator(9999, message='The year must be up to 9999')], 
                                  null=True)
    runtime_minutes = models.IntegerField(validators=[MinValueValidator(1, message='The runtime of title must be at least 1')], null=True)
    genres = ArrayField(models.CharField(max_length=40), size=3, null=True)
    
    def __str__(self):
        return self.original_title + '\nDuration - ' + str(self.runtime_minutes) + '\n' + str(self.start_year)
    
    class Meta:
        db_table = 'tbl_title'

class Rating(models.Model):
    title_id = models.OneToOneField('Title', on_delete=models.CASCADE, to_field='title_id', primary_key=True, related_name='rating', )
    average_rating = models.FloatField(null=True)
    num_votes = models.IntegerField(validators=[MinValueValidator(0, message='The number of votes must be at least 0')], null=True)

    def __str__(self):
        if (self.num_votes):
            return str(self.num_votes) + ' votes'
        else:
            return "No registered votes"
    
    class Meta:
        db_table = 'tbl_rating'

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    nconst = models.CharField(max_length=20)
    primary_name = models.CharField(max_length=150)
    birth_year = models.IntegerField(validators=[MinValueValidator(1, message='The year must be at least 1'), 
                                                MaxValueValidator(9999, message='The year must be up to 9999')], 
                                  null=True)
    death_year = models.IntegerField(validators=[MinValueValidator(1, message='The year must be at least 1'), 
                                                MaxValueValidator(9999, message='The year must be up to 9999')], 
                                  null=True)
    primary_profession = ArrayField(models.CharField(max_length=50), size=3, null=True)

    def __str__(self):
        return self.primary_name
    
    class Meta:
        db_table = 'tbl_actor'

class TitleActor(models.Model):
    title_id = models.ForeignKey('Title', on_delete=models.CASCADE, to_field='title_id', related_name='title')
    actor_id = models.ForeignKey('Actor', on_delete=models.CASCADE, to_field='actor_id', related_name='actor')

    class Meta:
        db_table = 'tbl_title_actor'


    
