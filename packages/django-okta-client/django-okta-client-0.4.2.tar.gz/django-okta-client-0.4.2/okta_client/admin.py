from django.contrib import admin

from .models import OktaUser


class OktaUserAdmin(admin.ModelAdmin):
	'''User admin
	Customized user admin for Okta users.
	'''
	
	custom_attributes_fieldset_fields = ()
	fieldsets_profile = (
		('Basic Info', {'fields': ('login', 'firstName', 'lastName', 'email')}),
		('Names', {
			'classes'	: ('collapse',),
			'fields'	: ('displayName', 'honorificPrefix', 'middleName', 'honorificSuffix', 'nickName'),
			}),
		('Contact Info', {
			'classes'	: ('collapse',),
			'fields'	: ('primaryPhone', 'mobilePhone', 'profileUrl', 'secondEmail'),
			}),
		('Organization', {
			'classes'	: ('collapse',),
			'fields'	: ('organization', 'division', 'department', 'title', 'userType', 'employeeNumber', 'costCenter', 'managerId', 'manager'),
			}),
		('Addresses', {
			'classes'	: ('collapse',),
			'fields'	: ('streetAddress', 'city', 'state', 'zipCode', 'countryCode', 'postalAddress'),
			}),
		('International', {
			'classes'	: ('collapse',),
			'fields'	: ('locale', 'preferredLanguage', 'timezone'),
			})
	)
	fieldsets_aaa = (
		('Groups', {
			'classes'	: ('collapse',),
			'fields'	: ('groups',),
			}),
		('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
	)
	list_display = ('login', 'firstName', 'lastName', 'email', 'is_staff', 'is_superuser', 'is_active')
	list_filter = ('is_active', 'userType', 'organization', 'division', 'department', 'title', 'managerId')
	ordering = ('login',)
	search_fields = ('login', 'firstName', 'lastName', 'email')

	def add_custom_attributes(self):
		'''Profile customization slot
		The place to handle the custom attributes in your Okta profile.

		The default implementation creates a single "Custom Attributes" fieldset and add all the fields present on the "custom_attributes_fieldset_fields" class attribute.

		It can be overriden to create a different layout. It must return a tuple containing the fieldsets wanted the way they're explained here https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets

		These values will always be inserted after the default profile attributes ("International", containing "locale", "preferredLanguage", and "timezone") and before the AAA (permissions) part (the "Groups" section). I you want a different layout you'd have to override the "fieldsets" attribute and build everything yourself.
		'''

		if self.custom_attributes_fieldset_fields:
			return (('Custom Attributes', {'classes' : ('collapse',), 'fields' : self.custom_attributes_fieldset_fields}),)
		else:
			return ()

	@property
	def fieldsets(self):
		'''Dynamic fieldsets
		Builds the attribute dynamically, including the output of the "add_custom_attributes" method.
		'''

		return self.fieldsets_profile + self.add_custom_attributes() + self.fieldsets_aaa

	
	def save_model(self, request, obj, form, change):
		'''Custom model creation
		Takes into account the custom model manager for the Okta users.
		'''
		
		if change:
			return super().save_model(request, obj, form, change)
		else:
			return type(obj).objects.create_user(**form.cleaned_data)


admin.site.register(OktaUser, OktaUserAdmin)
