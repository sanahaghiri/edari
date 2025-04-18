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
def create_person(request):
    s_data = request.data
    print(request.data)
    data_serializers = PersonelSerializers(data=s_data)
    if data_serializers.is_valid():
        data_serializers.save()
        return Response(data_serializers.data, status=status.HTTP_201_CREATED)
    return Response(data_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_alluser(request):
    user_data = PersonelModel.objects.all()
    return Response(
        PersonelSerializers(user_data, many=True).data, status=status.HTTP_200_OK
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        person_code = serializer.validated_data["person_code"]
        password = serializer.validated_data["password"]
        try:
            user = PersonelModel.objects.get(person_code=person_code)
            if user.password == password:
                user_data = PersonelSerializers(user).data
                return Response(user_data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "رمز عبور اشتباه است"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        except PersonelModel.DoesNotExist:
            return Response(
                {"error": "کاربری با این شماره پرسنلی یافت نشد"},
                status=status.HTTP_404_NOT_FOUND,
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)