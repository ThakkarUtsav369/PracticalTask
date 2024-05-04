from rest_framework.viewsets import ModelViewSet
from .serializers import CompanyEmployeeBulkCreateSerializer
from rest_framework.response import Response
from rest_framework import status

class UploadCsvViewSet(ModelViewSet):
    serializer_class = CompanyEmployeeBulkCreateSerializer
    http_method_names =['post']


    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                "success": True,
                "message": "Employee created successfully",
            },
            status=status.HTTP_200_OK,
        )
        return super().create(request, *args, **kwargs)