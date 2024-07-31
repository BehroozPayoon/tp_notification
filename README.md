## Setup and Run

1. Clone the repository
2. Make sure you have Docker and Docker Compose installed
3. Run `docker build -t tp_notifications:latest` to create image
4. Run `docker-compose up --d`
5. The Notification Service will be available at http://localhost:8001

## API Endpoints

### Notification Service

- POST /api/send-otp/: Send OTP (requires authentication token)
