import json
from app.tests import BaseTest


class TestEmployee(BaseTest):
    def test_create_employee(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        self.assertEqual(request.status_code, 201)

    def test_get_all_employees(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        response = self.client.get(
            '/v1/employees',
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['_meta']['total_items'], 1)

    def test_get_employee(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        employee = json.loads(request.get_data(as_text=True))
        response = self.client.get(
            '/v1/employees/{}'.format(employee['id']),
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['full_name'], 'Joao')

    def test_update_employee(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        employee = json.loads(request.get_data(as_text=True))
        response = self.client.put(
            '/v1/employees/{}'.format(employee['id']),
            headers=self.headers(),
            data=json.dumps({'full_name': 'Joao da Silva'})
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['full_name'], 'Joao da Silva')

    def test_delete_employee(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        employee = json.loads(request.get_data(as_text=True))
        response = self.client.delete(
            'v1/employees/{}'.format(employee['id']),
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 204)

    def test_create_employee_dependent(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        employee = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees/{}/dependents'.format(employee['id']),
            headers=self.headers(),
            data=json.dumps({'full_name': 'Julia'})
        )
        self.assertEqual(request.status_code, 201)

    def test_get_all_employee_dependents(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        employee = json.loads(request.get_data(as_text=True))
        response = self.client.get(
            '/v1/employees/{}/dependents'.format(employee['id']),
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['_meta']['total_items'], 2)

    def test_get_employee_dependent(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        employee = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees/{}/dependents'.format(employee['id']),
            headers=self.headers(),
            data=json.dumps({'full_name': 'Julia'})
        )
        dependent = json.loads(request.get_data(as_text=True))
        response = self.client.get(
            '/v1/employees/{}/dependents/{}'.format(employee['id'], dependent['id']),
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['full_name'], 'Julia')

    def test_update_employee_dependent(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        employee = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees/{}/dependents'.format(employee['id']),
            headers=self.headers(),
            data=json.dumps({'full_name': 'Julia'})
        )
        dependent = json.loads(request.get_data(as_text=True))
        response = self.client.put(
            '/v1/employees/{}/dependents/{}'.format(employee['id'], dependent['id']),
            headers=self.headers(),
            data = json.dumps({'full_name': 'Julia da Silva'})
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['full_name'], 'Julia da Silva')

    def test_delete_employee_dependent(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    'full_name': 'Joao',
                    'departament_id': departament['id'],
                    'dependents': [
                        'Ana',
                        'Maria'
                    ]
                }
            )
        )
        employee = json.loads(request.get_data(as_text=True))
        request = self.client.post(
            '/v1/employees/{}/dependents'.format(employee['id']),
            headers=self.headers(),
            data=json.dumps({'full_name': 'Julia'})
        )
        dependent = json.loads(request.get_data(as_text=True))
        response = self.client.delete(
            '/v1/employees/{}/dependents/{}'.format(employee['id'], dependent['id']),
            headers=self.headers(),
        )
        self.assertEqual(response.status_code, 204)