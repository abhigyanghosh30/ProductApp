from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Jobs(models.Model):

    resource_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    job_type = models.CharField(max_length=200)
    design_stage_gate = models.CharField(max_length=6)
    ga_drawing_number = models.CharField(max_length=200)
    milestone_description = models.TextField()
    plan_date = models.DateField()
    actual_date = models.DateField()
    hours_planned = models.IntegerField(default=0)
    hours_actual = models.IntegerField(default=0)
    compliance = models.FloatField()


class Products(models.Model):
    ga_drawing_number = models.CharField(max_length=100, primary_key=True)
    cams = models.TextField()
    wbs = models.TextField()
    product_description = models.TextField()
    location = models.TextField()
    department = models.TextField()
    line = models.TextField()

    order_quantity = models.IntegerField()
    total_weight = models.IntegerField()
    total_eqv_a1 = models.IntegerField()
    STATUS = (('O', "Ongoing"), ("C", "Completed"), ("N", "Not Started"))
    status = models.CharField(max_length=1, choices=STATUS)

    customer_input_date_plan = models.DateField()
    customer_input_date_actual = models.DateField()

    total_engg_manhours_plan = models.IntegerField(default=0)

    job_assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    percent_complete = models.IntegerField()

    r0_plan_apl = models.TextField()
    r0_plan_ts = models.TextField()
    r0_plan_drawing = models.TextField()

    running_plan_apl = models.TextField()
    running_plan_ts = models.TextField()
    running_plan_drawing = models.TextField()

    actual_plan_apl = models.TextField()
    actual_plan_ts = models.TextField()
    actual_plan_drawing = models.TextField()

    slip_days_apl = models.TextField()
    slip_days_ts = models.TextField()
    slip_days_drawing = models.TextField()

    number_of_a1_ready = models.IntegerField(default=0)
    release_details = models.TextField()
    remarks = models.TextField()

    plan_be = models.IntegerField(default=0)
    plan_3dm = models.IntegerField(default=0)
    plan_da = models.IntegerField(default=0)
    plan_2ddg = models.IntegerField(default=0)
    plan_ts = models.IntegerField(default=0)
    plan_dc = models.IntegerField(default=0)
    plan_dap = models.IntegerField(default=0)
    plan_bom = models.IntegerField(default=0)
    plan_ter = models.IntegerField(default=0)


class MonthlyMilestone(models.Model):

    id = models.IntegerField(primary_key=True)
    ga_drawing_number = models.CharField(max_length=100)
    product_group = models.CharField(max_length=100)
    milestone_description = models.TextField()
    plan_date = models.DateField()
    actual_date = models.DateField()
    responsibility = models.TextField()
    STATUS = (('O', "Ongoing"), ("C", "Completed"), ("N", "Not Started"))
    status = models.CharField(max_length=1, choices=STATUS)
    reason_for_non_compliance = models.TextField()


class LookAhead(models.Model):

    ga_drawing_number = models.ForeignKey(Products, on_delete=models.CASCADE)
    design_stage_gate = models.TextField()
    plan_start_week = models.IntegerField()
    plan_duration = models.IntegerField()
    actual_start_week = models.IntegerField()
    actual_duration = models.IntegerField()
    percent_complete = models.IntegerField()


class Data_exchange(models.Model):

    ga_drawing_number = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_group = models.CharField(max_length=100)
    date = models.DateField()
    sender = models.CharField(max_length=200)
    recipient = models.CharField(max_length=200)
    description = models.TextField()
    STATUS = (('O', "Ongoing"), ("C", "Completed"), ("N", "Not Started"))
    status = models.CharField(max_length=1, choices=STATUS)
