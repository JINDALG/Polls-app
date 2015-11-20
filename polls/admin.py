from django.contrib import admin

from models import Question
from models import Choice

class ChoiceInline(admin.TabularInline):
	"""docstring for ChoiceInline"""
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	list_display = ('question_text' , 'pub_date', 'was_published_recently')
	fieldsets = [
		(None,{'fields':['question_text']}),
		('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question_text']


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
