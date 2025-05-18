from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt



@api_view(["POST"])
@permission_classes([AllowAny])
def create_leave(request):
    s_data = request.data
    data_serializers = LeaveSerializers(data=s_data)
    if data_serializers.is_valid():
        data_serializers.save()
        return Response(data_serializers.data, status=status.HTTP_201_CREATED)
    return Response(data_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_leave(request):
    user_data = LeaveModel.objects.all()
    return Response(
        LeaveGetSerializers(user_data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["PATCH"])
@permission_classes([AllowAny])
def edit_leave_with_manager(request, pk):
    try:
        commodity = LeaveModel.objects.get(pk=pk)
    except LeaveModel.DoesNotExist:
        return Response(
            {"error": "Commodity not found."}, status=status.HTTP_404_NOT_FOUND
        )
    data = request.data
    serializer = LeaveSerializers(commodity, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)