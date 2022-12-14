from django.db import models


class F1Drivers(models.Model):
    number = models.IntegerField(db_column='Number', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    team = models.CharField(db_column='Team', max_length=50)  # Field name made lowercase.
    born = models.DateField(db_column='Born')  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'f1_drivers'

    def __str__(self):
        return self.name


class F1StatsSoFar(models.Model):
    number = models.OneToOneField(F1Drivers, models.DO_NOTHING, db_column='Number', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    wins = models.IntegerField(db_column='Wins')  # Field name made lowercase.
    points = models.IntegerField(db_column='Points')  # Field name made lowercase.

    class Meta:
        db_table = 'f1_stats_so_far'

    def __str__(self):
        return self.name + " " + str(self.points)


class Schedule(models.Model):
    round = models.IntegerField(db_column='Round', primary_key=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    champion = models.ForeignKey(F1Drivers, models.DO_NOTHING, db_column='Champion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'schedule'

    def __str__(self):
        return str(self.round) + " " + str(self.country) + " " + str(self.date)
