# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
from .models import Student, Group, MonthJournal


class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        """Checkif student is leader in any group"""

        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and \
            self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError('Студент є старостою іншої групи',
                             code='invalid')

        return self.cleaned_data['student_group']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 5
    search_fields = ['last_name', 'first_name', 'ticket', 'notes']
    form = StudentFormAdmin

    # see edit on sait
    def get_view_on_site_url(self, obj=None):
        return reverse('students_edit', kwargs={'pk': obj.id})

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
admin.site.register(MonthJournal)
