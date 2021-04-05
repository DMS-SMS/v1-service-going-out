import os
import requests

from domain.exception.server_error import ServerErrorException
from domain.service.pick_service import PickService


class PickServiceImpl(PickService):
    def __init__(self):
        self.base_url = os.getenv("PICK_BASE_URL")
        self.login_uri = f"{self.base_url}{os.getenv('PICK_LOGIN_URI')}"
        self.absent_uri = f"{self.base_url}{os.getenv('PICK_ABSENT_URI')}"
        self.x_api_key = os.getenv("PICK_X_API_KEY")
        self.pick_id = os.getenv("PICK_ID")
        self.pick_pw = os.getenv("PICK_PW")

    def login(self):
        login_payload = {"id": self.pick_id, "pw": self.pick_pw}
        response = requests.post(self.login_uri, json=login_payload)
        if not response.status_code == 200: raise ServerErrorException("Unable to log in to Pick Service")
        return response.json()["accessToken"]

    def absent(self, student_number, start_time, end_time):
        access_token = self.login()
        start_and_end_date = start_time.isoformat().split("T")[0]

        headers = {"Authorization": access_token, "x-api-key": self.x_api_key}
        absent_payload = {
            "state": "외출",
            "stdnum": student_number,
            "start_date": start_and_end_date,
            "end_date": start_and_end_date,
            "start_period": PickServiceImpl.convert_to_period(start_time),
            "end_period": PickServiceImpl.convert_to_period(end_time)
        }

        response = requests.post(self.absent_uri, json=absent_payload, headers=headers)
        if not response.status_code == 200:
            raise ServerErrorException(f"{response.status_code} error in Pick Service with {response.text}. \n"
                                       f"stdnum : {student_number}, date : {start_and_end_date}")

    @staticmethod
    def convert_to_period(datetime):
        hour = datetime.hour
        minute = datetime.minute

        if hour >= 20: period = "10"
        elif hour == 19:
            if minute > 40: period = "10"
            else: period = "9"
        elif hour == 18:
            if minute > 40: period = "9"
            else: period = "8"
        else: period = "8"

        return period