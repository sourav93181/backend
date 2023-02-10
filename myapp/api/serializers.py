from rest_framework import serializers
from Detail.models import Detail
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields=('companyId','companyName','website','location','jobType','experience','qualification','Batch','salary','point1','point2','point3','point4','point5')