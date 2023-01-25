from django.db import connections
from django.db import models


class showrecs(models.Model):
    site = models.CharField(max_length=6)
    
    class Meta:
        db_table="deisel_report"
        
        
class Engineer(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    change_password = models.TextField()  # This field type is a guess.
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    enabled = models.TextField()  # This field type is a guess.
    first_name = models.CharField(max_length=255, blank=True, null=True)
    is_logged_on = models.TextField()  # This field type is a guess.
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    no_of_wrong_login_count = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    user_name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    #role = models.ForeignKey('Role', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    zendesk_id = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineer'

class DeiselReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    actual_remaining_litres = models.CharField(max_length=255, blank=True, null=True)
    expected_remaining_litres = models.CharField(max_length=255, blank=True, null=True)
    gen_run_hour = models.CharField(max_length=255, blank=True, null=True)
    indicative_consumption = models.CharField(max_length=255, blank=True, null=True)
    site = models.ForeignKey('Site', models.DO_NOTHING, blank=True, null=True)
    engineer = models.ForeignKey('Engineer', models.DO_NOTHING, blank=True, null=True)
    actual_consumption = models.CharField(max_length=255, blank=True, null=True)
    reference_top_up_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deisel_report'
        
class Site(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zone = models.CharField(max_length=255, blank=True, null=True)
    #client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
    no_of_ac_installed = models.CharField(max_length=255, blank=True, null=True)
    nof_panels = models.CharField(max_length=255, blank=True, null=True)
    sudo_name = models.CharField(max_length=255, blank=True, null=True)
    fuel_tank_size = models.CharField(max_length=255, blank=True, null=True)
    generator_size = models.CharField(max_length=255, blank=True, null=True)
    gen_run_hour_date = models.DateTimeField(blank=True, null=True)
    last_ac_maintenance_date = models.DateTimeField(blank=True, null=True)
    last_generator_service_hour = models.BigIntegerField(blank=True, null=True)
    last_panel_maintenance_date = models.DateTimeField(blank=True, null=True)
    last_preventive_maintenance = models.TextField(blank=True, null=True)
    last_preventive_maintenance_date = models.DateTimeField(blank=True, null=True)
    last_recorded_run_hour = models.BigIntegerField(blank=True, null=True)
    next_ac_maintenance_date = models.DateTimeField(blank=True, null=True)
    next_panel_maintenance_date = models.DateTimeField(blank=True, null=True)
    #last_ac_maintenance = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)
    #last_panel_maintenance = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)
    site_manager = models.ForeignKey(Engineer, models.DO_NOTHING, blank=True, null=True)
    victron_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    #last_preventive_maintenance_0 = models.ForeignKey('Task', models.DO_NOTHING, db_column='last_preventive_maintenance_id', blank=True, null=True)  # Field renamed because of name conflict.
    current_fuel_level = models.BigIntegerField(blank=True, null=True)
    fuel_level_date = models.DateTimeField(blank=True, null=True)
    communicating = models.CharField(max_length=255, blank=True, null=True)
    phcn = models.CharField(max_length=255, blank=True, null=True)
    average_daily_fuel_usage = models.CharField(max_length=255, blank=True, null=True)
    average_gen_daily_run_hour = models.BigIntegerField(blank=True, null=True)
    hours_to_service = models.BigIntegerField(blank=True, null=True)
    next_service_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site'

    # def __str__(self):
    #     return self.name 
    

class SiteReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    ac_status_report = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    connected = models.CharField(max_length=255, blank=True, null=True)
    current_fuel_level = models.CharField(max_length=255, blank=True, null=True)
    engineer = models.TextField(blank=True, null=True)
    generator_age = models.CharField(max_length=255, blank=True, null=True)
    generator_brand = models.CharField(max_length=255, blank=True, null=True)
    generator_size = models.CharField(max_length=255, blank=True, null=True)
    generator_status_report = models.TextField(blank=True, null=True)
    inverter_status = models.CharField(max_length=255, blank=True, null=True)
    last_delivery_date = models.CharField(max_length=255, blank=True, null=True)
    last_delivery_quantity = models.CharField(max_length=255, blank=True, null=True)
    last_gen_service_hours = models.CharField(max_length=255, blank=True, null=True)
    last_panel_cleaning = models.CharField(max_length=255, blank=True, null=True)
    last_service_date = models.CharField(max_length=255, blank=True, null=True)
    lighting_status_report = models.CharField(max_length=255, blank=True, null=True)
    load_on_critical_inverter_total = models.CharField(max_length=255, blank=True, null=True)
    load_onl1 = models.CharField(max_length=255, blank=True, null=True)
    load_onl2 = models.CharField(max_length=255, blank=True, null=True)
    load_onl3 = models.CharField(max_length=255, blank=True, null=True)
    next_delivery_due_date = models.CharField(max_length=255, blank=True, null=True)
    next_panel_cleaning = models.CharField(max_length=255, blank=True, null=True)
    next_service_date = models.CharField(max_length=255, blank=True, null=True)
    next_service_due = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    number_of_panels = models.CharField(max_length=255, blank=True, null=True)
    pv_harvest_status = models.CharField(max_length=255, blank=True, null=True)
    run_hour = models.CharField(max_length=255, blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    solar_strings = models.CharField(max_length=255, blank=True, null=True)
    status_report = models.CharField(max_length=255, blank=True, null=True)
    torque_level_check_date = models.CharField(max_length=255, blank=True, null=True)
    engineer_0 = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='engineer_id', blank=True, null=True)  # Field renamed because of name conflict.
    site_0 = models.ForeignKey(Site, models.DO_NOTHING, db_column='site_id', blank=True, null=True)  # Field renamed because of name conflict.
    time_sheet_end = models.CharField(max_length=255, blank=True, null=True)
    time_sheet_start = models.CharField(max_length=255, blank=True, null=True)
    battery_appearance_ok = models.CharField(max_length=255, blank=True, null=True)
    battery_temperature_ok = models.CharField(max_length=255, blank=True, null=True)
    battery_terminal_ok = models.CharField(max_length=255, blank=True, null=True)
    site_communicating = models.CharField(max_length=255, blank=True, null=True)
    date_ac_issue_report = models.CharField(max_length=255, blank=True, null=True)
    no_of_fault_ac = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    extra_image1 = models.CharField(max_length=255, blank=True, null=True)
    extra_image2 = models.CharField(max_length=255, blank=True, null=True)
    extra_image3 = models.CharField(max_length=255, blank=True, null=True)
    extra_image4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_report'


