class NotificationService:
    """
    A notification service that violates
    the Open/Closed Principle.
    """

    def send_notification(self, notification_type, message):

        if notification_type == "email":
            print(f"Sending EMAIL: {message}")

        elif notification_type == "sms":
            print(f"Sending SMS: {message}")

        elif notification_type == "push":
            print(f"Sending PUSH notification: {message}")

        else:
            print("Unknown notification type")


def main():

    service = NotificationService()

    service.send_notification(
        "email",
        "Model training completed successfully."
    )

    service.send_notification(
        "sms",
        "Model deployed successfully."
    )


if __name__ == "__main__":
    main()