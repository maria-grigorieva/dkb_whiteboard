# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EventSummary(models.Model):
    """ Model for the Event Summary """
    status = models.CharField(max_length=25)
    datasetname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    hashtag_list = models.CharField(max_length=500)
    taskid = models.BigIntegerField()
    campaign = models.CharField(max_length=25)
    pr_id = models.BigIntegerField()
    processed_events = models.IntegerField()
    timestamp = models.DateTimeField()
    start_time = models.DateTimeField()
    dataset_status = models.CharField(max_length=25)
    phys_category = models.CharField(max_length=25)
    project = models.CharField(max_length=25)
    step_name = models.CharField(max_length=25)
    phys_group = models.CharField(max_length=25)
    energy_gev = models.CharField(max_length=25)
    taskname = models.CharField(max_length=255)
    subcampaign = models.CharField(max_length=25)
    requested_events = models.IntegerField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return "TASKID: {}".format(self.taskid)