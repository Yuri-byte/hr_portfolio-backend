# employees/serializers.py
from rest_framework import serializers
from .models import Employee, Role, ContactInfo, EmployeeRoleHistory

class FlexibleNestedField(serializers.Field):
    def __init__(self, serializer_class, queryset, **kwargs):
        self.serializer_class = serializer_class
        self.queryset = queryset
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        if isinstance(data, int):
            try:
                return self.queryset.get(pk=data)
            except self.queryset.model.DoesNotExist:
                raise serializers.ValidationError("Invalid ID provided.")
        elif isinstance(data, dict):
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            return serializer.save()
        raise serializers.ValidationError("Expected int or dict.")

    def to_representation(self, value):
        return self.serializer_class(value).data

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    contact_info = FlexibleNestedField(ContactInfoSerializer, queryset=ContactInfo.objects.all())
    role = FlexibleNestedField(RoleSerializer, queryset=Role.objects.all())
    manager = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        # Extract and handle nested or referenced contact_info
        contact_info_data = validated_data.pop('contact_info', None)
        if isinstance(contact_info_data, dict):
            contact_info = ContactInfo.objects.create(**contact_info_data)
        elif isinstance(contact_info_data, ContactInfo):
            contact_info = contact_info_data
        else:
            contact_info = None

        # Extract and handle nested or referenced role
        role_data = validated_data.pop('role', None)
        if isinstance(role_data, dict):
            role = Role.objects.create(**role_data)
        elif isinstance(role_data, Role):
            role = role_data
        else:
            role = None

        # Create employee object with resolved foreign key objects
        employee = Employee.objects.create(
            **validated_data,
            contact_info=contact_info,
            role=role
        )

        return employee

    def update(self, instance, validated_data):
        contact_info_data = validated_data.pop('contact_info', None)
        role_data = validated_data.pop('role', None)

        if isinstance(contact_info_data, dict):
            for attr, value in contact_info_data.items():
                setattr(instance.contact_info, attr, value)
            instance.contact_info.save()

        if isinstance(role_data, dict):
            for attr, value in role_data.items():
                setattr(instance.role, attr, value)
            instance.role.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class EmployeeRoleHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRoleHistory
        fields = '__all__'