"""
===============================================================================
Module: bad_design.py

Path: module-1.1-software-design-oop/demos/demo-09-solid-ocp/bad_design.py

Purpose:
Demonstrate an incorrect implementation of the Open/Closed Principle (OCP),
where new notification types require modifying existing code.

===============================================================================
"""


class NotificationService:
    """Notification service that violates OCP."""

    def send_notification(self, notification_type, message):  # Uses conditional logic.

        if notification_type == "email":
            print(f"Sending EMAIL: {message}")

        elif notification_type == "sms":
            print(f"Sending SMS: {message}")

        elif notification_type == "push":
            print(f"Sending PUSH notification: {message}")

        else:
            print("Unknown notification type")  # Handles unsupported types.


def main():  # Coordinates the demonstration.
    """Program entry point."""

    service = NotificationService()

    service.send_notification(
        "email",
        "Model training completed successfully."
    )

    service.send_notification(
        "sms",
        "Model deployed successfully."
    )


if __name__ == "__main__":  # Script entry point.
    main()