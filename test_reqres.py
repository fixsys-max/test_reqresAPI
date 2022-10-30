from reqresapi import ReqresAPI
import time
from random import choice

RESPONSE_TIME = 250
req = ReqresAPI()


class TestGetUsersList:
    time1 = time.time()
    response = req.get_users_list()
    time2 = time.time()

    def test_status_code(self):
        code = self.response.status_code
        assert code == 200, f'Status code is not 200 ({code})'

    def test_response_time(self):
        response_time = (self.time2 - self.time1) * 1000
        assert response_time < RESPONSE_TIME, f'Response time {response_time:.0f}ms more than {RESPONSE_TIME}ms'

    def test_body_should_have_required_fields(self):
        body = self.response.json()
        results = []
        for i in ['page', 'per_page', 'total', 'total_pages', 'data', 'support']:
            results.append(i in body)
        assert all(results), 'Response body do not have required fields'

    def test_body_data_should_have_required_fields(self):
        body_data = self.response.json()['data'][0]
        results = []
        for i in ['id', 'email', 'first_name', 'last_name', 'avatar']:
            results.append(i in body_data)
        assert all(results), 'Response body data do not have required fields'


class TestCreateUser:
    name = 'UserName'
    job = 'UserJob'
    time1 = time.time()
    response = req.create_user(name=name, job=job)
    time2 = time.time()

    def test_status_code(self):
        code = self.response.status_code
        assert code == 201, f'Status code is not 201 ({code})'

    def test_response_time(self):
        response_time = (self.time2 - self.time1) * 1000
        assert response_time < RESPONSE_TIME, f'Response time {response_time:.0f}ms more than {RESPONSE_TIME}ms'

    def test_body_should_have_required_fields(self):
        body = self.response.json()
        results = []
        for i in ['name', 'job', 'id', 'createdAt']:
            results.append(i in body)
        assert all(results), 'Response body do not have required fields'

    def test_users_name_and_job_is_right(self):
        name = self.response.json()['name']
        job = self.response.json()['job']
        assert name == self.name and job == self.job, 'Name or job is not changed'


class TestChangeAllUserData:
    name = 'NewUserName'
    job = 'NewUserJob'
    time1 = time.time()
    response = req.change_all_user_data(name=name, job=job)
    time2 = time.time()

    def test_status_code(self):
        code = self.response.status_code
        assert code == 200, f'Status code is not 200 ({code})'

    def test_response_time(self):
        response_time = (self.time2 - self.time1) * 1000
        assert response_time < RESPONSE_TIME, f'Response time {response_time:.0f}ms more than {RESPONSE_TIME}ms'

    def test_body_should_have_required_fields(self):
        body = self.response.json()
        results = []
        for i in ['name', 'job', 'updatedAt']:
            results.append(i in body)
        assert all(results), 'Response body do not have required fields'

    def test_users_name_and_job_was_changed(self):
        name = self.response.json()['name']
        job = self.response.json()['job']
        assert name == self.name and job == self.job, 'Name or job is not changed'


class TestChangeSomeUserData:
    name, job = choice([('NewUserName2', None), (None, 'NewUserJob2')])
    time1 = time.time()
    response = req.change_some_user_data(name=name, job=job)
    time2 = time.time()

    def test_status_code(self):
        code = self.response.status_code
        assert code == 200, f'Status code is not 200 ({code})'

    def test_response_time(self):
        response_time = (self.time2 - self.time1) * 1000
        assert response_time < RESPONSE_TIME, f'Response time {response_time:.0f}ms more than {RESPONSE_TIME}ms'

    def test_body_should_have_required_fields(self):
        body = self.response.json()
        results = []
        if self.name:
            fields = ['name', 'updatedAt']
        elif self.job:
            fields = ['job', 'updatedAt']
        else:
            raise ValueError('Name or job is not definite')
        for i in fields:
            results.append(i in body)
        assert all(results), 'Response body do not have required fields'

    def test_users_name_or_job_was_changed(self):
        if self.name:
            name = self.response.json()['name']
            assert name == self.name, 'Name is not changed'
        else:
            job = self.response.json()['job']
            assert job == self.job, 'Job is not changed'


class TestGetUserInfo:
    time1 = time.time()
    response = req.get_user_info()
    time2 = time.time()

    def test_status_code(self):
        code = self.response.status_code
        assert code == 200, f'Status code is not 200 ({code})'

    def test_response_time(self):
        response_time = (self.time2 - self.time1) * 1000
        assert response_time < RESPONSE_TIME, f'Response time {response_time:.0f}ms more than {RESPONSE_TIME}ms'

    def test_body_should_have_required_fields(self):
        body = self.response.json()
        results = []
        for i in ['data', 'support']:
            results.append(i in body)
        assert all(results), 'Response body do not have required fields'

    def test_body_data_should_have_required_fields(self):
        body_data = self.response.json()['data']
        results = []
        for i in ['id', 'email', 'first_name', 'last_name', 'avatar']:
            results.append(i in body_data)
        assert all(results), 'Response body data do not have required fields'


class TestDeleteUer:
    time1 = time.time()
    response = req.delete_user()
    time2 = time.time()

    def test_status_code(self):
        code = self.response.status_code
        assert code == 204, f'Status code is not 204 ({code})'

    def test_response_time(self):
        response_time = (self.time2 - self.time1) * 1000
        assert response_time < RESPONSE_TIME, f'Response time {response_time:.0f}ms more than {RESPONSE_TIME}ms'
