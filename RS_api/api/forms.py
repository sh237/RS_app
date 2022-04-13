from django import forms
from .models import DateManage

class DateForm(forms.ModelForm):


    class Meta:
        model = DateManage
        fields = ("date","start_time","end_time")
        # widgets = {
        #             "name": forms.TextInput(attrs={'placeholder':'紀伊　太郎'}),
        #             "age": forms.RadioSelect(),

        #           }
        # widgets = {
        #         'date': datetimepicker.DatePickerInput(
        #             format='%Y-%m-%d',
        #             options={
        #                 'locale': 'ja',
        #                 'dayViewHeaderFormat': 'YYYY年 MMMM',
        #             }
        #         ),

        #         'start_time': datetimepicker.DateTimePickerInput(
        #             format='%Y-%m-%d %H:%M:%S',
        #             options={
        #                 'locale': 'ja',
        #                 'dayViewHeaderFormat': 'YYYY年 MMMM',
        #             }
        #         ),

        #         'end_time': datetimepicker.DateTimePickerInput(
        #             format='%Y-%m-%d %H:%M:%S',
        #             options={
        #                 'locale': 'ja',
        #                 'dayViewHeaderFormat': 'YYYY年 MMMM',
                    # })
        # }
