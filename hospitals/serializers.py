from rest_framework import serializers

from hospitals.models import Hospital, HospitalPhone, HospitalPhoto


class HospitalPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalPhoto
        fields = (
            'id',
            'image',
        )


class HospitalPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalPhone
        fields = (
            'phone',
        )


class HospitalSerializer(serializers.ModelSerializer):
    photo = HospitalPhotoSerializer(required=False)
    phones = serializers.StringRelatedField(many=True)

    class Meta:
        model = Hospital
        fields = (
            'id',
            'name',
            'address',
            'url',
            'url_on_map',
            'phones',
            'photo',
        )
        extra_kwargs = {
            'url': { 'required': False },
            'photo': { 'required': False },
        }
