import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .tasks import send_otp


class SendOTPView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        otp = str(random.randint(100000, 999999))
        send_otp.delay(email, otp)

        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
