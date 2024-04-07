from rest_framework.views import APIView
from .models import User
from rest_framework import status
from .serializers import UserRegisterSerializer,UserDetailSerializer,UserReferralSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class UserRegisterView(APIView):

    def post(self,request):
        try:
            serializer = UserRegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        


class UserDetailsView(ListAPIView):
    permission_classes =[IsAuthenticated]

    try:
        queryset = User.objects.all()
        serializer_class = UserDetailSerializer
    except Exception as e:
        Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class UserReferralsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        referrals = User.objects.filter(referral_code=user.referral_code).order_by('-registred_at')

        paginator = PageNumberPagination()
        paginator.page_size = 3
        result_page = paginator.paginate_queryset(referrals,request)

        serializer = UserReferralSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    