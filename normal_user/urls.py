from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [

	path('login/',Login.as_view(),name='login'),
	# path('manager_login/', csrf_exempt(ManagerLogin.as_view()), name='manager_login'),
	# path('login/', LoginView.as_view(template_name="login.html",authentication_form=LoginForm), name='login'),
	path('logout/',logout_user,name='logout'),
	path('account_blocked_page/', AccountBlocked.as_view(), name='account_blocked_page'),
	path('',LandingPage.as_view(),name='landing_page'),
	path('manager_dashboard',ManagerDashboard.as_view(),name='manager_dashboard'),
	path('staff_user_window',StaffWindow.as_view(),name='staff_user_window'),
	path('add_employee',csrf_exempt(AddStaffMember.as_view()),name='add_employee'),
	path('add_clock_timezone',csrf_exempt(ManagerClock.as_view()),name='add_clock_timezone'),
	path('unblock_staff',csrf_exempt(UnblockStaff.as_view()),name='unblock_staff'),


	path('staff_status',csrf_exempt(StaffStatus.as_view()),name='staff_status'),
	path('staff_profile',csrf_exempt(StaffProfile.as_view()),name='staff_profile'),

	path('employee_profile',StaffEmployeeProfile.as_view(),name='employee_profile'),
	path('resources',Resources.as_view(),name='resources'),
	path('add_comment',csrf_exempt(UserComment.as_view()),name='add_comment'),
	path('delete_resource',csrf_exempt(DeleteResource.as_view()),name='delete_resource'),

	path('archive_chat',csrf_exempt(ArchiveChat.as_view()),name='archive_chat'),

	path('alert_user',csrf_exempt(Alert.as_view()),name='alert_user'),
	path('save_document',csrf_exempt(SaveDocument.as_view()),name='save_document'),
	path('assign_department',csrf_exempt(AssignDepartment.as_view()),name='assign_department'),
	path('remove_assigned_department',csrf_exempt(RemoveDepartment.as_view()),name='remove_assigned_department'),

	path('get_users',csrf_exempt(GetUsers.as_view()),name='get_users'),

	path('today_task',csrf_exempt(TaskAssign.as_view()),name='today_task'),
	path('delete_task',csrf_exempt(DeleteTask.as_view()),name='delete_task'),
	path('today_email',csrf_exempt(Email.as_view()),name='today_email'),
		
	path('admin_dashboard',(AdminDashboard.as_view()),name='admin_dashboard'),
	path('add_department',csrf_exempt(AddDepartment.as_view()),name='add_department'),
	path('add_city',csrf_exempt(AddCity.as_view()),name='add_city'),
	path('add_function',csrf_exempt(Addfunction.as_view()),name='add_function'),
	path('add_manager',csrf_exempt(AddManager.as_view()),name='add_manager'),
	path('add_designation',csrf_exempt(AddDesignation.as_view()),name='add_designation'),
	
	path('no_permission',csrf_exempt(NoPermission.as_view()),name='no_permission'),
	# path('sort_by_document',csrf_exempt(SortByDocument.as_view()),name='sort_by_document'),
	path('manager_profile',csrf_exempt(ManagerProfile.as_view()),name='manager_profile'),
	path('reporting_module/<int:id>',csrf_exempt(ReportingModule.as_view()),name='reporting_module'),

	path('change_staff_pass',csrf_exempt(ChangeStaffPassword.as_view()),name='change_staff_pass'),
	path('change_manager_pass',csrf_exempt(ChangeManagerPassword.as_view()),name='change_manager_pass'),
	path('user_online_status',csrf_exempt(UserOnlineStatus.as_view()),name='user_online_status'),
	path('check_user_online_status',csrf_exempt(CheckUserOnlineStatus.as_view()),name='check_user_online_status'),

	path('email_listing',csrf_exempt(EmailListing.as_view()),name='email_listing'),
	path('employee_listing',csrf_exempt(EmployeeListing.as_view()),name='employee_listing'),

	path('manager_list',csrf_exempt(ManagerList.as_view()),name='manager_list'),

	path('user_tasks',csrf_exempt(UserTasks.as_view()),name='user_tasks'),
	path('user_emails',csrf_exempt(UserEmails.as_view()),name='user_emails'),
	path('user_alert',csrf_exempt(UserAlert.as_view()),name='user_alert'),
	path('user_comment',csrf_exempt(StaffUserComments.as_view()),name='user_comment'),
	path('acknowledge_task',csrf_exempt(AcknowledgedTasks.as_view()),name='acknowledge_task'),
	path('add_schedle_time',csrf_exempt(SchedulerTime.as_view()),name='add_schedle_time'),

	path('task_list/<int:id>',csrf_exempt(TaskList.as_view()),name='task_list'),
	path('attendence_record/<int:id>',csrf_exempt(AttendenceRecord.as_view()),name='attendence_record'),
	
	path('chat_box',csrf_exempt(StaffChatByUser.as_view()),name='chat_box'),
	
	path('manager_chat_box',csrf_exempt(ManagerChatByUser.as_view()),name='manager_chat_box'),

	path('manager_chat',csrf_exempt(ManagerChat.as_view()),name='manager_chat'),
	path('get_searched_users',csrf_exempt(GetSearchedUsers.as_view()),name='get_searched_users'),
	path('get_searched_users_by_manager',csrf_exempt(GetSearchedUsersByManager.as_view()),name='get_searched_users_by_manager'),
	path('get_chat_by_manager',csrf_exempt(GetChatByManager.as_view()),name='get_chat_by_manager'),

	path('manager_profile_edit/<int:id>',csrf_exempt(ManagerProfileEdit.as_view()),name='manager_profile_edit'),

	path('manager_profile_post',csrf_exempt(ManagerProfileEditPost.as_view()),name='manager_profile_post'),

	path('staff_profile_edit/<int:id>',csrf_exempt(StaffProfileEdit.as_view()),name='staff_profile_edit'),

	path('staff_profile_post',csrf_exempt(StaffProfileEditPost.as_view()),name='staff_profile_post'),

	path('get_chat',csrf_exempt(GetChat.as_view()),name='get_chat'),

	path('end_shift',csrf_exempt(EndShift.as_view()),name='end_shift'),

	path('manager_online',csrf_exempt(OnlineManager.as_view()),name='manager_online'),
	path('cron_request',csrf_exempt(CronJobOnlineManager.as_view()),name='cron_request'),

	path('new_chat_thread',csrf_exempt(NewChatThread.as_view()),name='new_chat_thread'),

	path('staff_online',csrf_exempt(StaffStatusRuntime.as_view()),name='staff_online'),

	path('open_resource',csrf_exempt(OpenResource.as_view()),name='open_resource'),
	path('individual_staff_resource/<int:id>',csrf_exempt(IndividualStaffResource.as_view()),name='individual_staff_resource'),

	path('meeting/<meeting_id>/', meeting, name='meeting'),
	path('all_notifications',csrf_exempt(AllNotifications.as_view()),name='all_notifications'),
	path('notification_action',csrf_exempt(NotificationAction.as_view()),name='notification_action'),
	path('scheduler_list/<int:id>',csrf_exempt(SchedulerList.as_view()),name='scheduler_list'),
	path('edit_scheduler/<int:user_id>/<int:id>',csrf_exempt(EditScheduler.as_view()),name='edit_scheduler'),

	path('saveovertime',csrf_exempt(SaveOverTime.as_view()),name='saveovertime'),
	# path('employee-task-list',EmployeeTaskList.as_view(),name='employee_task_list'),
	# path('employee-task-list-detail/<int:id>',EmployeeTaskListDetail.as_view(),name='employee-task-list-detail'),
	path('overtime_list/<int:id>',csrf_exempt(OverTimeList.as_view()),name='overtime_list'),
	path('edit_overtime/<int:user_id>/<int:id>',csrf_exempt(EditOverTime.as_view()),name='edit_overtime'),
	path('comments_list/<int:id>',csrf_exempt(Comments_List.as_view()),name='comments_list'),
	path('create_thread/',csrf_exempt(CreateThread.as_view()),name='create_thread'),
	path('getchat_group/<int:id>',csrf_exempt(GetChatGroup.as_view()),name='getchat_group'),
	path('edit_comments<int:id>',csrf_exempt(EditComments.as_view()),name='edit_comments'),
	path('addgroup',csrf_exempt(GroupAdd.as_view()),name='addgroup'),
	path('latereporting_module/',csrf_exempt(LateReportingModule.as_view()),name='latereporting_module'),
	path('seacrh-report/',csrf_exempt(SearchReport.as_view()),name='seacrh-report'),
	path('home/', HomeView.as_view(),name='home'),
	path('broadcast/', BroadCreateThread.as_view(),name='broadcast'),
	path('adminbroadcast/', AdminCreateThread.as_view(),name='adminbroadcast'),
	path('manager_group_chat',csrf_exempt(ManagerGroupChat.as_view()),name='manager_group_chat'),
	# path('page_not_found',csrf_exempt(PageNotFound.as_view()),name='page_not_found'),
	path('employee-task-list',EmployeeTaskList.as_view(),name='employees_list'),
	path('employee-task-list-detail/<int:id>',EmployeeTaskListDetail.as_view(),name='employee-task'),

]

