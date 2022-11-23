import logging
import sys
import traceback
import random
import services.utils.services.authorsService as authorsService
from locust import FastHttpUser, task, constant, events, LoadTestShape, User, HttpUser



class LocustRun(HttpUser):
    wait_time = constant(0.1)

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        print("on test start")

    def on_start(self):
        print("currently executing user - " + str(self.environment.runner.user_count))

    @task(1)
    def get_authors(self):
        with authorsService.get_authors() as response:
            try:
                response_json = response.json()
                assert response.status_code == 200
                assert response.elapsed.total_seconds() <= 3
                assert response_json.__len__() > 0
                # commonServiceUtils.verify_response_schema(response_json, "author_api_request_response_body.json")
            except Exception as e:
                logging.error(getattr(e, 'message', repr(e)))
                _, _, var = sys.exc_info()
                tb_info = traceback.extract_tb(var)
                print(tb_info)
                filename, line_number, function_name, text = tb_info[-1]
                response.failure("There is {} in line {} in this statement: {}".format(repr(e), line_number, text))

    @task(2)
    def add_author(self, id=random.randint(101, 999), book_id=random.randint(1111, 9999)):
        with authorsService.add_author(id, book_id, "Bhupendra", "Kushwah") as response:
            try:
                response_json = response.json()
                assert response.status_code == 200
                assert response.elapsed.total_seconds() <= 5
                assert response_json['idBook'] == book_id
                # commonServiceUtils.verify_response_schema(response_json, "author_api_request_response_body.json")
            except Exception as e:
                _, _, var = sys.exc_info()
                tb_info = traceback.extract_tb(var)
                print(tb_info)
                filename, line_number, function_name, text = tb_info[-1]
                response.failure("There is {} in line {} in this statement: {}".format(repr(e), line_number, text))


class AuthorServiceLoadShape():
    def tick(self):
        users = self.get_current_user_count()
        if 0 <= users < 10:
            self.auth_token = "1check1"
        elif 10 <= users < 20:
            self.auth_token = "2check2"

        target = self.targets_with_times[self.step]
