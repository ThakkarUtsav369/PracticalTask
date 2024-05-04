from rest_framework import serializers

import pandas as pd

from ApiTask.models import Company, Employee
from rest_framework.response import Response


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "phone_number", "company","salary"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]


class CompanyEmployeeBulkCreateSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate(self, attrs):
        file = attrs.get("file")
        # Check if file is provided
        if not file:
            raise serializers.ValidationError("File is required.")
        if not file.name.lower().endswith(('.csv', '.xlsx')):
            raise serializers.ValidationError("File format not supported. Please provide a CSV or Excel file.")

        # Add more validation logic if needed
        return attrs

    def save(self, **kwargs):
        file = self.validated_data["file"]
        saved_employees = []

        # Read data from CSV file
        data = pd.read_excel(file)

        # Extract unique company names
        company_names = data["COMPANY_NAME"].unique()

        # Create companies and employees
        for name in company_names:
            # Create company instance
            company_serializer = CompanySerializer(data={"name": name})
            if company_serializer.is_valid():
                company_instance = company_serializer.save()
            else:
                continue  # Skip this company if serializer is not valid
            # Filter employees for this company
            employees_data = data[data["COMPANY_NAME"] == name]

            # Create employee instances for this company
            for _, row in employees_data.iterrows():
                employee_serializer = EmployeeSerializer(
                    data={
                        "first_name": row["FIRST_NAME"],
                        "last_name": row["LAST_NAME"],
                        "phone_number": row["PHONE_NUMBER"],
                        'salary':row["SALARY"],
                        "company": company_instance.id,
                    }
                )
                if employee_serializer.is_valid():
                    employee_serializer.save()
                    saved_employees.append(employee_serializer.data)
