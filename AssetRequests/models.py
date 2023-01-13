from django.db import models
from Products.models import Items

from django.db import connections, models
from django.forms import ModelForm
from django.urls import reverse
from django.utils import timezone
from .manager import RequestManager
from django.contrib.auth.models import User

# Create your models here.


class Engineer(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    #del_flag = models.CharField(max_length=255, blank=True, null=True)
    #deleted_on = models.DateTimeField(blank=True, null=True)
    #version = models.IntegerField()
    # change_password = models.TextField()  # This field type is a guess.
    email = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    # enabled = models.TextField()  # This field type is a guess.
    first_name = models.CharField(max_length=255, blank=True, null=True)
    # is_logged_on = models.TextField()  # This field type is a guess.
    #last_login_date = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    #no_of_wrong_login_count = models.IntegerField(blank=True, null=True)
    #password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    user_name = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    #status = models.CharField(max_length=255, blank=True, null=True)
    #role = models.ForeignKey('Role', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    #zendesk_id = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineer'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Site(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    #del_flag = models.CharField(max_length=255, blank=True, null=True)
    #deleted_on = models.DateTimeField(blank=True, null=True)
    #version = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    #state = models.CharField(max_length=255, blank=True, null=True)
    #zone = models.CharField(max_length=255, blank=True, null=True)
    #client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
    #no_of_ac_installed = models.CharField(max_length=255, blank=True, null=True)
    #nof_panels = models.CharField(max_length=255, blank=True, null=True)
    sudo_name = models.CharField(max_length=255, blank=True, null=True)
    #fuel_tank_size = models.CharField(max_length=255, blank=True, null=True)
    #generator_size = models.CharField(max_length=255, blank=True, null=True)
    #gen_run_hour_date = models.DateTimeField(blank=True, null=True)
    #last_ac_maintenance_date = models.DateTimeField(blank=True, null=True)
    #last_generator_service_hour = models.BigIntegerField(blank=True, null=True)
    #last_panel_maintenance_date = models.DateTimeField(blank=True, null=True)
    #last_preventive_maintenance = models.TextField(blank=True, null=True)
    #last_preventive_maintenance_date = models.DateTimeField(blank=True, null=True)
    #last_recorded_run_hour = models.BigIntegerField(blank=True, null=True)
    #next_ac_maintenance_date = models.DateTimeField(blank=True, null=True)
    #next_panel_maintenance_date = models.DateTimeField(blank=True, null=True)
    #last_ac_maintenance = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)
    #last_panel_maintenance = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)
    site_manager = models.ForeignKey(
        Engineer, models.DO_NOTHING, blank=True, null=True)
    #victron_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    # last_preventive_maintenance_0 = models.ForeignKey('Task', models.DO_NOTHING, db_column='last_preventive_maintenance_id', blank=True, null=True)  # Field renamed because of name conflict.
    #current_fuel_level = models.BigIntegerField(blank=True, null=True)
    #fuel_level_date = models.DateTimeField(blank=True, null=True)
    #communicating = models.CharField(max_length=255, blank=True, null=True)
    #phcn = models.CharField(max_length=255, blank=True, null=True)
    #average_daily_fuel_usage = models.CharField(max_length=255, blank=True, null=True)
    #average_gen_daily_run_hour = models.BigIntegerField(blank=True, null=True)
    #hours_to_service = models.BigIntegerField(blank=True, null=True)
    #next_service_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site'

    def save(self, *args, **kwargs):
        self.date_created = self.date_created
        self.sudo_name = self.sudo_name
        self.phcn = self.phcn
        self.fuel_level_date = self.fuel_level_date
        self.fuel_tank_size = self.fuel_tank_size

        super(Site, self).save(*args, **kwargs)

    def __str__(self):
        order_by = self.name
        return self.name


class AssetRequest(models.Model):
    from django.contrib.auth.models import User

    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'

    STATUS_CHOICES = (
        (STATUS_APPROVED, 'approved'),
        (STATUS_REJECTED, 'rejected'),
        (STATUS_PENDING, 'pending'),
        (STATUS_CONFIRMED, 'confirmed'),
    )

    requestdate = models.DateField(auto_now_add=True)
    request_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    mgr_approved_date = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    cto_approved_date = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    #user = models.ForeignKey(User, models.CASCADE)
    site = models.ForeignKey(Site, models.CASCADE,
                             verbose_name='Confirm Site')
    site_engineer = models.ForeignKey(
        Engineer, models.CASCADE, verbose_name='Confirm Engineer')
    site_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    #site_address = models.ForeignKey(Site, on_delete=models.CASCADE)

    product = models.ForeignKey(Items, on_delete=models.CASCADE)

    manufacturer = models.CharField(max_length=20)
    bad_last_service = models.DateField(
        verbose_name='Last Serviced Date')
    bad_serial_number = models.CharField(max_length=20,
                                         verbose_name='Serial Number')
    bad_model_number = models.CharField(max_length=20,
                                        verbose_name='Model Number')
    bad_equipment_name = models.CharField(
        max_length=50, verbose_name='Equipment Name')
    bad_equipment_rating = models.CharField(
        max_length=10, verbose_name='Equipment Rating')
    bad_days_in_ops = models.CharField(
        max_length=10, verbose_name='Days/Weeks/Months in Operations')
    bad_installation_date = models.DateField(verbose_name='Installed Date')

    new_equipment_name = models.CharField(
        max_length=100, verbose_name='Equipment Name')
    new_manufacturer = models.CharField(
        max_length=50, verbose_name='Manufacturer')
    new_equipment_rating = models.CharField(
        max_length=10, verbose_name='Rating')
    expected_date = models.DateField(verbose_name='Expected Delivery Date')

    sitemanager_comment = models.CharField(
        max_length=500, verbose_name='Site Manager Comment')
    hod_comment = models.CharField(
        max_length=500, verbose_name='HOD/CTO Comment')
    mgr_approve = models.BooleanField(blank=True, null=True)
    cto_approve = models.BooleanField(blank=True, null=True)
    mgr_status = models.CharField(blank=True, null=True,
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    cto_status = models.CharField(blank=True, null=True,
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    justification = models.CharField(max_length=3000)

    objects = RequestManager()

    class Meta:
        ordering = ['-requestdate']
        verbose_name_plural = 'Asset Requests'

    @property
    def request_approved(self):
        return self.mgr_approve == True  # and self.cto_approve == True

    @property
    def approve_request(self):
        if not self.mgr_approve:  # and self.cto_approve:
            self.mgr_approve = True
            self.mgr_status = 'confirmed'
            self.save()

    @property
    def pending_request(self):
        if self.mgr_approve:
            self.mgr_approve = False
            self.mgr_status = 'pending'
            self.save()

#########################################################################################################

    @property
    def cto_request_approved(self):
        return self.cto_approve == True  # and self.cto_approve == True

    @property
    def cto_approve_request(self):
        if not self.cto_approve:  # and self.cto_approve:
            self.cto_approve = True
            self.cto_status = 'approved'
            self.save()

    @property
    def cto_pending_request(self):
        if self.cto_approve:
            self.cto_approve = False
            self.cto_status = 'pending'
            self.save()


#########################################################################################################

    @property
    def request_cancel(self):
        if self.mgr_approve or not self.mgr_approve:
            self.mgr_approve = False
            self.mgr_status = 'cancelled'
            self.save()

    @property
    def reject_request(self):
        if self.mgr_approve or not self.mgr_approve:
            self.mgr_approve = False
            self.status = 'rejected'
            self.save()

    @property
    def is_rejected(self):
        return self.mgr_status == 'rejected'

    # def get_absolute_url(self):
    #     return reverse('request-details', kwargs={'id':self.id})

    def __str__(self, *args, **kwargs):
        return str(str(self.requestdate) + '-' + str(self.site) + '-' + str(self.mgr_status))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} UserProfile'
