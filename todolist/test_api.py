import json
import requests

host = 'http://localhost:8000/api'

header = {"Content-Type": "application/json"}


def test_create_todo_list():
    data = {"detail":"work3","complete":True}
    response = requests.post(url=f'{host}/create_todo_list/', headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")


def test_get_todo_list():
    response = requests.get(url=f"{host}/get_todo_list/", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")
    return (response.json()[0]['id'])



def test_delete_todo_list(todolist_id):
    response = requests.delete(url=f"{host}/delete_todo_list/?todolist_id={todolist_id}", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_edit_todo_list(todolist_id):
    data = {"detail":"work3111","complete":False}
    response = requests.post(url=f"{host}/edit_todo_list/?todolist_id={todolist_id}", headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")


if __name__ == '__main__':
    pass
    #Test API create
    test_create_todo_list()

    #Test API GET
    todolist_id_frist = test_get_todo_list()

    #Test API DELETE
    # test_delete_todo_list(todolist_id_frist)

    #Test API EDIT
    test_edit_todo_list(todolist_id_frist)


