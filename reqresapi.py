import requests
import json


class ReqresAPI:
    __env = 'https://reqres.in/api'

    def __init__(self):
        self.user_id = None

    def get_users_list(self):
        url = f'{self.__env}/users'
        response = requests.get(url=url)
        return response

    def create_user(self, name, job):
        url = f'{self.__env}/users'
        body = {"name": name, "job": job}
        response = requests.post(url=url, data=body)
        self.user_id = response.json()['id']
        return response

    def change_all_user_data(self, name, job):
        if self.user_id:
            url = f'{self.__env}/users/{self.user_id}'
            if name and job:
                body = {"name": name, "job": job}
            else:
                raise ValueError("No data for changing: name is None, job is None")
            response = requests.put(url=url, data=body)
            return response
        raise ValueError("User is not created. User ID is None")

    def change_some_user_data(self, name=None, job=None):
        if self.user_id:
            url = f'{self.__env}/users/{self.user_id}'
            if name and job:
                body = {"name": name, "job": job}
            elif name:
                body = {"name": name}
            elif job:
                body = {"job": job}
            else:
                raise ValueError("No data for changing: name is None, job is None")
            response = requests.patch(url=url, data=body)
            return response
        raise ValueError("User is not created. User ID is None")

    def get_user_info(self):
        url = f'{self.__env}/users/2'
        response = requests.get(url=url)
        return response

    def delete_user(self):
        if self.user_id:
            url = f'{self.__env}/users/{self.user_id}'
            response = requests.delete(url=url)
            return response
        raise ValueError("User is not created. User ID is None")


if __name__ == '__main__':
    req1 = ReqresAPI()
    print(json.dumps(req1.get_users_list().json(), indent=4))
    print(json.dumps(req1.create_user('UserName', 'UserJob').json(), indent=4))
    print(json.dumps(req1.get_user_info().json(), indent=4))

