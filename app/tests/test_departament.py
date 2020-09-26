import json
from app.tests import BaseTest


class TestDepartament(BaseTest):
    def test_create_departament(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        self.assertEqual(request.status_code, 201)

    def test_get_all_departaments(self):
        self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        response = self.client.get(
            '/v1/departaments',
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['_meta']['total_items'], 1)

    def test_get_departament(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        response = self.client.get(
            '/v1/departaments/{}'.format(departament['id']),
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['name'], 'Comercial')

    def test_update_departament(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        response = self.client.put(
            '/v1/departaments/{}'.format(departament['id']),
            headers=self.headers(),
            data=json.dumps({'name': 'Vendas e Marketing'})
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['name'], 'Vendas e Marketing')

    def test_delete_departament(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        response = self.client.delete(
            'v1/departaments/{}'.format(departament['id']),
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 204)

    def test_get_all_departaments_employees(self):
        request = self.client.post(
            '/v1/departaments',
            headers=self.headers(),
            data=json.dumps({'name': 'Comercial'})
        )
        departament = json.loads(request.get_data(as_text=True))
        self.client.post(
            '/v1/employees',
            headers=self.headers(),
            data=json.dumps(
                {
                    "full_name": "Joao",
                    "departament_id": departament['id'],
                    "dependents": [
                        "Ana",
                        "Maria"
                    ]
                }
            )
        )
        response = self.client.get(
            'v1/departaments/employees',
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['_meta']['total_items'], 1)

    def test_get_departament_employees(self):
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
            'v1/departaments/{}/employees'.format(departament['id']),
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['employees'][0]['full_name'], 'Joao')