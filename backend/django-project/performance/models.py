from django.db import models


class Group(models.Model):
    group_id = models.BigIntegerField(primary_key=True)

    competences = models.IntegerField(default=None)
    justice = models.TextField(max_length=255, blank=False, default=None)
    grade = models.TextField(max_length=255, blank=False, default=None)
    court = models.TextField(max_length=255, blank=False, default=None)
    court_class = models.TextField(max_length=255, blank=False, default=None)
    subject = models.TextField(max_length=255, blank=False, default=None)
    judging_body = models.TextField(max_length=255, blank=False, default=None)

    amount_of_varas = models.IntegerField(default=None)


class Vara(models.Model):
    vara_id = models.BigIntegerField(primary_key=True)
    name = models.TextField(max_length=255, blank=False, default=None)

    ranking = models.IntegerField(default=None)
    finished_processes = models.IntegerField(default=None)
    movements = models.IntegerField(default=None)

    group_id = models.ForeignKey(Group, on_delete=models.CASCADE) # [ref: > grupos.identificador]

    time_macrostep_1 = models.IntegerField(default=None)
    time_macrostep_2 = models.IntegerField(default=None)
    time_macrostep_3 = models.IntegerField(default=None)
    time_macrostep_4 = models.IntegerField(default=None)
    days_finish_process = models.IntegerField(default=None)

    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)


class VaraList(models.Model):
    vara_id = models.ForeignKey(Vara, on_delete=models.CASCADE) # models.BigIntegerField()
    name = models.TextField(max_length=255, blank=False, default=None)

