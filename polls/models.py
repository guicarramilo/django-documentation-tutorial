'''models: essentially, your database layout, with additional metadata.
   Each model has a number of class variables, each of which represents
   a database field in the model.

   The name of each Field instance (e.g. question_text or pub_date) is the fields name, 
   in machine-friendly format. Youll use this value in your Python code, and your database 
   will use it as the column name.
'''


import datetime

from django.db import models #Here, each model is represented by a class that subclasses django.db.models.Model
from django.utils import timezone


#A Question has a question and a publication date.
class Question(models.Model): #a class that subclasses django.db.models.Model
    #Each field is represented by an instance of a Field class
    question_text = models.CharField(max_length=200) # CharField for character fields
    pub_date = models.DateTimeField("date published")#  DateTimeField for datetimes, we’ve only defined a human-readable name for Question.pub_date

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#A Choice has two fields: the text of the choice and a vote tally.
class Choice(models.Model):
    #Each Choice is associated with a Question. each Choice is related to a single Question. 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    #A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text