import time

from celery import shared_task


@shared_task
def send_otp(email, otp):
    # Simulate sending OTP
    time.sleep(2)
    print(f"Sending OTP {otp} to {email}")
