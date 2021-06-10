from django.shortcuts import redirect
from .models import UserType

def checkloginSuperuser(function):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated:
			if request.user.is_superuser:
				pass
			else:
				return redirect('/no_permission')
		else:
			return redirect('/login')	
		return function(request, *args, **kwargs)
	# wrap.__doc__ = function.__doc__
	# wrap.__name__ = function.__name__	
	return wrap



def checkloginManager(function):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated:
			user_id = request.user.id
			try:
				usr_obj = UserType.objects.get(user_id = user_id)
				if usr_obj.manager:
					# return redirect('/admin-dashboard')
					pass
				else:
					return redirect('/no_permission')
			except Exception as f:
				if request.user.is_superuser:
					return redirect('/no_permission')
				else:	
					return redirect('/login')
		else:
			return redirect('/login')
		return function(request, *args, **kwargs)
	# wrap.__doc__ = function.__doc__
	# wrap.__name__ = function.__name__	
	return wrap



def checkloginEmployee(function):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated:
			user_id = request.user.id
			try:
				usr_obj = UserType.objects.get(user_id = user_id)
				if usr_obj.normal_user:
					# return redirect('/admin-dashboard')
					pass
				else:
					return redirect('/no_permission')
			except Exception as f:
				if request.user.is_superuser:
					return redirect('/no_permission')
				else:	
					return redirect('/login')
		else:
			return redirect('/login')
		return function(request, *args, **kwargs)
	# wrap.__doc__ = function.__doc__
	# wrap.__name__ = function.__name__	
	return wrap