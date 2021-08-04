from datetime import time

from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor}"

class Meeting(models.Model):
    #save this ones on database
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #holds the id of the room object for this object
                                                            #cascade--->if room deleted->all metiings are deleted too

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"