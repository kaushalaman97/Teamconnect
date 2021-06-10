from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime
# from datetime import datetime, timedelta


def default_start_time():
	now = datetime.datetime.now()
	start = now.replace(hour=0, minute=0, second=0, microsecond=0)
	return start.time()


class UserType(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	manager = models.BooleanField(default=False)
	normal_user = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.user)


class InvalidAttempts(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	attempts = models.IntegerField(null=True, blank=True)
	blocked = models.BooleanField(default=False)
	start_time = models.DateTimeField(blank=True,null=True)
	
	def __str__(self):
		return str(self.user)


class ManagerTimezones(models.Model):
	manager_id = models.IntegerField(null=True, blank=True)
	timezone1 = models.CharField(max_length=100,blank=True)
	timezone2 = models.CharField(max_length=100,blank=True)
	timezone3 = models.CharField(max_length=100,blank=True)
	timezone4 = models.CharField(max_length=100,blank=True)

	def __str__(self):
		return str(self.manager_id)


class CommentsModel(models.Model):
	staff_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	manager_id = models.IntegerField(null=True, blank=True)
	comment = models.TextField(blank=True, null=True)
	seen_unseen = models.BooleanField(default=False)
	create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
	update_date = models.DateTimeField(auto_now=True,blank=True, null=True)

	def __str__(self):
		return str(self.staff_user_id)

class EmailModel(models.Model):
	staff_user_id   = models.ForeignKey(User, on_delete=models.CASCADE)
	manager_id      = models.IntegerField(null=True, blank=True)
	subject         = models.TextField(null=True,blank=True)
	descrtiption    = models.TextField(null=True,blank=True)
	to_email        = models.CharField(null=True,blank=True, max_length = 250)
	from_email      = models.CharField(null=True,blank=True, max_length = 250)
	to_name         = models.CharField(null=True,blank=True, max_length = 250)
	from_name       = models.CharField(null=True,blank=True, max_length = 250)
	created_staff   = models.DateTimeField(null = True,blank=True)
	created_manager = models.DateTimeField(null = True,blank=True)
	seen_unseen     = models.BooleanField(default=False)
	email_reply     = models.TextField(null=True,blank=True)
	date_str        = models.CharField(max_length = 30, null = True, blank=True)

	def __str__(self):
		return str(self.staff_user_id)


class EailReplyModel(models.Model):
	emailobj                = models.ForeignKey(EmailModel, on_delete=models.CASCADE)
	email_reply             = models.TextField(null=True,blank=True)
	email_reply_time        = models.DateTimeField(null = True,blank=True)
	email_reply_time_staff  = models.DateTimeField(null = True,blank=True)

	def __str__(self):
		return str(self.email_reply)


class AlertModel(models.Model):
	staff_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	manager_id = models.IntegerField(null=True, blank=True)
	alert = models.BooleanField(default=False)
	alert_message = models.TextField(null = True, blank=True)
	seen_unseen = models.BooleanField(default=False)

	def __str__(self):
		return str(self.staff_user_id)



class TaskModel(models.Model):
	staff_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	manager_id = models.IntegerField(null=True, blank=True)
	task = models.TextField(null=True, blank=True)
	acknowledge = models.BooleanField(default = False)
	date_str = models.CharField(max_length = 20, null = True, blank=True)
	created = models.DateTimeField(null = True, blank=True)
	created_manager = models.DateTimeField(null = True,blank=True)
	seen_unseen = models.BooleanField(default=False)
	complete_time = models.DateTimeField(auto_now_add=True,null = True,blank=True)
	
	
	def __str__(self):
		return str(self.staff_user_id)


class Tasks(models.Model):
	task_id = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
	task = models.TextField(null=True, blank=True)
	acknowledge = models.BooleanField(default = False)
	seen_unseen = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.task)


class StaffStatusModel(models.Model):
	staff_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	manager_id = models.IntegerField(null=True, blank=True)
	status = models.TextField(null=True, blank=True)
	created_staff = models.DateTimeField(null = True, blank=True)
	created_manager = models.DateTimeField(null = True, blank=True)
	
	def __str__(self):
		return str(self.staff_user_id)


class SavedDocumentModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	path = models.TextField(null = True, blank=True)
	extension = models.CharField(max_length = 100, null = True, blank=True)
	name = models.CharField(max_length = 100, null = True, blank=True)
	file_name_by_user = models.TextField(null = True, blank=True)
	created = models.DateTimeField(null = True, blank = True)
	doc = models.BooleanField(default = False)
	docx = models.BooleanField(default = False)
	pdf = models.BooleanField(default = False)
	ppt = models.BooleanField(default = False)
	csv = models.BooleanField(default = False)
	jpeg = models.BooleanField(default = False)
	xls = models.BooleanField(default = False)
	pptx = models.BooleanField(default = False)
	xlsx = models.BooleanField(default = False)
	jpg = models.BooleanField(default = False)
	png = models.BooleanField(default = False)
	mp4 = models.BooleanField(default = False)
	
	def __str__(self):
		return str(self.user)


class Departments(models.Model):
	departments = models.TextField(null = True, blank=True)
	
	def __str__(self):
		return str(self.departments)


class Functions(models.Model):
	function = models.TextField(null = True, blank=True)
	
	def __str__(self):
		return str(self.function)


class Cities(models.Model):
	cities = models.TextField(null = True, blank=True)
	
	def __str__(self):
		return str(self.cities)


class Designation(models.Model):
	designation = models.TextField(null = True, blank=True)
	
	def __str__(self):
		return str(self.designation)


class UserDetails(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	department = models.ForeignKey(Departments, on_delete=models.CASCADE)
	manager_id = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length=100,blank=True)
	email2 = models.CharField(max_length=100,blank=True)
	phone_no_1 = models.CharField(max_length=100,blank=True)
	phone_no_2 = models.CharField(max_length=100,blank=True)
	timezone = models.CharField(max_length=100,blank=True)
	country = models.CharField(max_length=100,blank=True)
	city = models.CharField(max_length=100,blank=True)
	count_timer = models.CharField(max_length=100,blank=True)
	it_equipment_specification = models.TextField(blank=True)
	comment = models.TextField(blank=True)
	function = models.CharField(max_length=100,blank=True)
	add_schedule_date_time = models.CharField(max_length=100,blank=True)
	last_countdown_timer_time = models.DateTimeField(null = True, blank = True)
	designation = models.TextField(null = True,blank=True)
	profile_pic = models.FileField(null = True,blank=True, default="/static/img/admin-demo.png")
	last_location = models.CharField(max_length=200,blank=True)
	date_company_join = models.DateTimeField(null = True, blank = True)
	date_department_join = models.DateTimeField(null = True, blank = True)

	def __str__(self):
		return str(self.user)


class ManagerDetails(models.Model):
	manaager = models.ForeignKey(User, on_delete=models.CASCADE)
	department = models.ForeignKey(Departments, on_delete=models.CASCADE)
	designation = models.TextField(null = True,blank=True)
	phone = models.CharField(max_length=100,blank=True,null = True)
	full_name = models.CharField(max_length=100,blank=True,null = True)
	timezone = models.CharField(max_length=100,blank=True,null = True)
	created = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	profile_pic = models.FileField(null = True,blank=True, default="/static/img/admin-demo.png")

	def __str__(self):
		return str(self.manaager)


class AssignedDepartments(models.Model):
	departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
	user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
	# file_name_by_user = models.CharField(max_length = 200, null = True, blank=True)
	# name = models.CharField(max_length = 100, null = True, blank=True)
	# path = models.TextField(null = True, blank=True)
	resource_obj = models.ForeignKey(SavedDocumentModel, on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.departments)


class OnlineStatusModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	i_am_here = models.BooleanField(default = False)
	in_meeting = models.BooleanField(default = False)
	lunch_break = models.BooleanField(default = False)
	tea_break = models.BooleanField(default = False)
	offline = models.BooleanField(default = False)
	time = models.DateTimeField(null = True, blank = True)
	
	def __str__(self):
		return str(self.user)


class ScheduleTime(models.Model):
	manager = models.ForeignKey(User, on_delete=models.CASCADE)
	user_id = models.IntegerField(null=True, blank=True)
	start_date = models.DateField(null = True, blank = True)
	end_date = models.DateField(null = True, blank = True)

	def __str__(self):
		return str(self.start_date)


class ScheduleTiming(models.Model):
	manager = models.ForeignKey(User, on_delete=models.CASCADE)	
	schedule_time_id = models.ForeignKey(ScheduleTime, on_delete=models.CASCADE)
	user_id = models.IntegerField(null=True, blank=True)
	start_date = models.DateField(null = True, blank = True)
	end_date = models.DateField(null = True, blank = True)
	start_time = models.TimeField(null = True, blank = True)
	end_time = models.TimeField(null = True, blank = True)
	login_time = models.DateTimeField(null = True, blank = True)
	logout_time = models.DateTimeField(null = True, blank = True)
	online_time = models.IntegerField(null=True, blank=True, default = 0)
	offline_time = models.IntegerField(null=True, blank=True, default = 0)
	break_time = models.IntegerField(null=True, blank=True, default = 0)
	shift = models.CharField(max_length = 50, null = True, blank=True)
	login_attempts = models.IntegerField(null=True, blank=True, default = 0)
	weekday = models.CharField(max_length = 12, null=True, blank=True)
	iso_weekday = models.IntegerField(null=True, blank=True)
	day_off = models.BooleanField(default = False)

	def __str__(self):
		return str(self.day_off) + " " + str(self.start_date)+ " " + str(self.weekday)
	def get_time_diff(self):
		try:
			login_time = (self.login_time).replace(tzinfo = None)
			combine = (datetime.datetime.combine(self.start_date, self.start_time)).replace(tzinfo = None)
			diff = login_time - combine
			if diff.total_seconds() > 0:
				return "+"
			else:
				return "-"
		except:
			return ""

	def get_time_diff_end(self):
		try:
			login_time = (self.login_time).replace(tzinfo = None)
			combine = (datetime.datetime.combine(self.end_date, self.end_time)).replace(tzinfo = None)
			diff = login_time - combine
			if diff.total_seconds() > 0:
				return "+"
			else:
				return "-"
		except:
			return ""



class ChatThread(models.Model):
	sender       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_1')
	reciever     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever_1')
	date_updated = models.DateTimeField(null = True, blank = True)
	date_updated_receiver =  models.DateTimeField(blank = True, null = True)
	created      = models.DateTimeField(auto_now_add = True, null = True)
	archive      = models.BooleanField(default = False)
	archive_2    = models.BooleanField(default = False)
	def __str__(self):
		return str(self.sender)


class ChatMessage(models.Model):
	sender    =   models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
	reciever  =   models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
	message   =   models.TextField(null = True, blank = True)
	thread    =   models.ForeignKey(ChatThread, on_delete = models.CASCADE)
	created   =   models.DateTimeField(blank = True, null = True)
	created_receiver =  models.DateTimeField(blank = True, null = True)
	name      =   models.TextField(blank=True, null = True)
	
	def __str__(self):
		return str(self.message)


class Notifications(models.Model):
	manager        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager')
	user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
	name           = models.TextField(null = True, blank = True)
	greek_o_msg    = models.TextField(null = True, blank = True)
	notification   = models.TextField(null = True, blank = True)
	notification_type   = models.TextField(null = True, blank = True)
	additional_msg = models.TextField(null = True, blank = True)
	read           = models.BooleanField(default = False)
	created        = models.DateTimeField(blank = True, null = True)
	
	def __str__(self):
		return str(self.notification)





class OverTime(models.Model):
	DAYS_CHOICES = (
    ('monday','MONDAY'),
    ('tuesday', 'TUESDAY'),
    ('wednesday','WEDNESDAY'),
    ('thursday','THURSDAY'),
    ('friday','FRIDAY'),
	('saturday','SATURDAY'),
	('sunday','SUNDAY'),
	) 
	manager = models.ForeignKey(User, on_delete=models.CASCADE)	
	user_id = models.IntegerField(null=True, blank=True)
	select_date = models.DateField(null = True, blank = True)
	start_time = models.TimeField(null = True, blank = True)
	end_time = models.TimeField(null = True, blank = True)
	def __str__(self):
		return str(self.user_id) + " " + str(self.select_date)+ " " + str(self.start_time)



class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ChatRoom(TrackingModel):
	THREAD_TYPE = (
		('group', 'Group'),
    )
	name = models.CharField(max_length=50, null=True, blank=True)
	user =  models.ManyToManyField(UserDetails,blank=True,null=True)
	super_user =models.ManyToManyField(User,blank=True,null=True)
	room_no = models.IntegerField()
	

	def __str__(self) -> str:
		return f'{self.name}'

class ChatModel(models.Model):
	room_no = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
	message = models.TextField()

class ReportFilter(models.Model):
	manager_id =  models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255,blank=True,null=True)
	user_id = models.IntegerField(blank=True,null=True)
	login_time = models.DateTimeField(null = True, blank = True)
	logout_time = models.DateTimeField(null = True, blank = True)
	start_time = models.TimeField(null = True, blank = True)
	location = models.CharField(max_length=255,blank=True,null=True)
	start_date = models.DateField(null = True, blank = True)

	def __str__(self):
		return self.name



class TestModelNew(models.Model):
	pass