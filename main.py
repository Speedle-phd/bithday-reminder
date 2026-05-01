"""
Enhanced Birthday Reminder Application

This application has been improved with robust error handling, comprehensive validation,
and email iteration functionality.

Key Enhancements:
1. **Error Handling**: Comprehensive try-catch blocks for all operations
2. **Validation**: Email format, date format, and person data validation
3. **Email Iteration**: Sends birthday reminders to all users listed in send_to
4. **Logging**: Detailed logging to both file and console
5. **Environment Validation**: Checks for required environment variables
6. **SMTP Error Handling**: Specific handling for different SMTP errors
7. **Data Integrity**: Validates required fields and data formats

Usage:
- Run directly: python main.py
- Docker: docker run birthday-reminder
- Requires EMAIL and EMAIL_PW environment variables
"""

from email.message import EmailMessage
import os
import smtplib
from datetime import datetime as dt

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # dotenv not available, continue without it
    pass
import re
import logging
from typing import Optional, Any
from data.data import BIRTHDAY_LIST, USERS
from data.greetings import choose_message

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log/birthday_reminder.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# Environment variables
EMAIL: Optional[str] = os.getenv("EMAIL")
PW: Optional[str] = os.getenv("EMAIL_PW")


# Validation functions
def validate_environment() -> bool:
    """Validate required environment variables."""
    if not EMAIL or not PW:
        logger.error("Missing required environment variables: EMAIL and/or EMAIL_PW")
        return False
    return True


def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_date_format(date_str: str) -> bool:
    """Validate date format (YYYY-MM-DD)."""
    try:
        dt.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def calculate_age(birthday_str: str) -> int:
    """Calculate age from birthday string in YYYY-MM-DD format."""
    try:
        birth_date = dt.strptime(birthday_str, "%Y-%m-%d")
        today = dt.now()

        age = today.year - birth_date.year

        # Check if birthday has occurred this year
        if today.month < birth_date.month or (
            today.month == birth_date.month and today.day < birth_date.day
        ):
            age -= 1

        return age
    except ValueError as e:
        logger.error(f"Error calculating age for birthday {birthday_str}: {str(e)}")
        return 0


def validate_person_data(person: dict[str, Any]) -> list[str]:
    """Validate person data and return list of validation errors."""
    errors = []
    required_fields = ["fname", "lname", "birthday", "send_to"]

    for field in required_fields:
        if field not in person or not person[field]:
            errors.append(f"Missing required field: {field}")

    if "birthday" in person and person["birthday"]:
        if not validate_date_format(person["birthday"]):
            errors.append(f"Invalid date format for birthday: {person['birthday']}")

    if "send_to" in person and person["send_to"]:
        if not isinstance(person["send_to"], list):
            errors.append("send_to must be a list")
        elif len(person["send_to"]) == 0:
            errors.append("send_to list cannot be empty")

    return errors


def get_user_email(username: str) -> Optional[str]:
    """Get email address for a given username."""
    for user in USERS:
        if user.get("username") == username:
            email = user.get("email")
            if email and validate_email(email):
                return email
            else:
                logger.warning(f"Invalid email format for user {username}: {email}")
                return None
    logger.warning(f"User {username} not found in USERS list")
    return None


def send_email(message: str, name: str, recipients: list[str], age: int = 0) -> bool:
    """Send birthday reminder email to multiple recipients with optional age."""
    if not validate_environment():
        return False

    success_count = 0
    total_recipients = len(recipients)

    try:
        logger.info(
            f"Attempting to send birthday reminder for {name} to {total_recipients} recipients"
        )

        with smtplib.SMTP("smtp.ionos.de", 587, None, 30) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PW)  # type: ignore

            for username in recipients:
                try:
                    recipient_email = get_user_email(username)
                    if not recipient_email:
                        logger.error(f"Could not find valid email for user: {username}")
                        continue

                    em = EmailMessage()
                    em.set_content(message)
                    em["To"] = recipient_email
                    em["From"] = EMAIL  # type: ignore

                    # Create subject line with age if provided
                    if age > 0:
                        em["Subject"] = f"🎉 {name} is turning {age} today! 🎂"
                    else:
                        em["Subject"] = f"Birthday Reminder for {name}"

                    connection.send_message(em)
                    success_count += 1
                    logger.info(
                        f"Successfully sent birthday reminder for {name} to {username} ({recipient_email})"
                    )

                except Exception as e:
                    logger.error(f"Failed to send email to {username}: {str(e)}")
                    continue

    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"SMTP Authentication failed: {str(e)}")
        return False
    except smtplib.SMTPConnectError as e:
        logger.error(f"SMTP Connection failed: {str(e)}")
        return False
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error occurred: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error while sending emails: {str(e)}")
        return False

    if success_count > 0:
        logger.info(
            f"Successfully sent {success_count}/{total_recipients} emails for {name}"
        )
        return True
    else:
        logger.error(f"Failed to send any emails for {name}")
        return False


def check_birthday() -> bool:
    """Check for birthdays today and send reminder emails."""
    if not validate_environment():
        logger.error("Environment validation failed. Aborting birthday check.")
        return False

    today = dt.now()
    today_month = today.strftime("%m")
    today_day = today.strftime("%d")

    logger.info(f"Checking birthdays for {today.strftime('%Y-%m-%d')}")

    processed_count = 0
    success_count = 0

    for person in BIRTHDAY_LIST:
        try:
            # Validate person data
            validation_errors = validate_person_data(person)
            if validation_errors:
                person_name = (
                    person.get("fname", "Unknown")
                    + " "
                    + person.get("lname", "Unknown")
                )
                logger.error(
                    f"Validation failed for {person_name}: {', '.join(validation_errors)}"
                )
                continue

            # Check if birthday is today
            birthday_parts = person["birthday"].split("-")
            if len(birthday_parts) != 3:
                logger.error(
                    f"Invalid birthday format for {person['fname']} {person['lname']}: {person['birthday']}"
                )
                continue

            birthday_month = birthday_parts[1]
            birthday_day = birthday_parts[2]

            if birthday_month == today_month and birthday_day == today_day:
                logger.info(f"Birthday found for {person['fname']} {person['lname']}")

                try:
                    name = f"{person['fname']} {person['lname']}"
                    age = calculate_age(person["birthday"])

                    logger.info(f"{name} is turning {age} years old today!")

                    # Send personalized messages to each recipient
                    success_count_for_person = 0
                    total_recipients_for_person = len(person["send_to"])

                    for username in person["send_to"]:
                        try:
                            # Generate personalized message for this specific recipient
                            message = choose_message(person, username)

                            if send_email(message, name, [username], age):
                                success_count_for_person += 1
                                logger.info(
                                    f"Personalized birthday reminder sent to {username} for {name}"
                                )
                        except Exception as e:
                            logger.error(
                                f"Error generating/sending personalized message to {username} for {name}: {str(e)}"
                            )
                            continue

                    if success_count_for_person > 0:
                        success_count += 1
                        logger.info(
                            f"Birthday reminder processing completed for {name} (age {age}) - sent to {success_count_for_person}/{total_recipients_for_person} recipients"
                        )
                    else:
                        logger.error(
                            f"Failed to send any personalized birthday reminders for {name}"
                        )

                except Exception as e:
                    logger.error(
                        f"Error processing birthday for {person['fname']} {person['lname']}: {str(e)}"
                    )

            processed_count += 1

        except Exception as e:
            person_name = (
                person.get("fname", "Unknown") + " " + person.get("lname", "Unknown")
            )
            logger.error(f"Unexpected error processing person {person_name}: {str(e)}")
            continue

    logger.info(
        f"Birthday check completed. Processed {processed_count} people, sent reminders for {success_count} birthdays."
    )
    return success_count > 0


if __name__ == "__main__":
    try:
        logger.info("Starting birthday reminder application")
        success = check_birthday()
        if success:
            logger.info("Birthday reminder application completed successfully")
        else:
            logger.info(
                "Birthday reminder application completed with no birthdays processed"
            )
    except Exception as e:
        logger.error(f"Fatal error in birthday reminder application: {str(e)}")
        exit(1)
