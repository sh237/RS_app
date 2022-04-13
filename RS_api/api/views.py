from django.shortcuts import render
import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View,FormView
from rest_framework import serializers,generics
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

import datetime 

from .forms import DateForm
from .models import DateManage

# Create your views here.

class DateManageSerializer(serializers.ModelSerializer):
    class Meta:
        model=DateManage
        fields ='__all__'

class DateManageFilter(django_filters.FilterSet):
    class Meta:
        model=DateManage
        fields={'date':['gte', ], }

class DateManageViewSet(viewsets.ModelViewSet):
    queryset=DateManage.objects.all().order_by("date")

    serializer_class=DateManageSerializer
    filter_class=DateManageFilter

    authentication_classes=(SessionAuthentication,BasicAuthentication)
    # permission_classes=(IsAuthenticated,)

# class MainView(View):
#     model = DateManage
#     template_name='index.html'
#     form_class = DateForm

def list(request):
    data = DateManage.objects.all()
    params = {'data': data}
    return render(request, 'index.html', params)
    
class DateFormView(FormView):
    model = DateManage
    template_name='create.html'
    form_class = DateForm
    success_url = reverse_lazy('create')

    def form_valid(self, form):
        
        form.save()
        return super().form_valid(form)
class TodayView(generics.ListCreateAPIView):
    queryset = DateManage.objects.all()
    serializer_class = DateManageSerializer

    def get_queryset(self):
        queryset = DateManage.objects.all()
        date = self.request.query_params.get('date',None)
        if date is not None:
            queryset = queryset.filter(datemanage__date=date)
        return queryset
