from rest_framework import serializers
from ..models import *



class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ('fname', 'lname',
                  'emailid', 'address',
                  'country', 'deleted',
                  'status')