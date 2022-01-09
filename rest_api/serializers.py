from rest_framework import serializers

# All Field types can be found inthe docs: https://www.django-rest-framework.org/api-guide/fields/#serializer-fields
class testSerializers(serializers.Serializer):
    list_of_strings = serializers.ListField(child=serializers.CharField(max_length=120))
    boolean_field = serializers.BooleanField()
    integer_field = serializers.IntegerField()
    fload_field = serializers.FloatField()