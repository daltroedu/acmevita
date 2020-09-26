import json
from app.tests import BaseTest


class TestEmployee(BaseTest):
    def test_get_all_dependents(self):
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
        self.client.post(
            '/v1/employees/{}/dependents'.format(employee['id']),
            headers=self.headers(),
            data=json.dumps({'full_name': 'Julia'})
        )
        response = self.client.get(
            '/v1/dependents',
            headers=self.headers()
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['_meta']['total_items'], 3)