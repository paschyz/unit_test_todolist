# import unittest
# from unittest.mock import Mock, patch
# from services.email_sender_service import EmailsenderService


# class TestEmailSending(unittest.TestCase):
#     @patch('services.EmailsenderService')
#     def test_send_email(self, mock_send_email_function):
#         EmailsenderService services: EmailsenderService = EmailsenderService()
#         EmailsenderService.send_email(
#             "from@example.com", "to@example.com", "Subject", "Body")

#         mock_send_email_function.assert_called_once_with(
#             "from@example.com", "to@example.com", "Subject", "Body")
