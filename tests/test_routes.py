import sys
import os
# Add the project root to the system path so that "app" can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_score_endpoint(client):
    # Prepare test data
    test_data = {
        "resume": "Software engineer with Python and ML experience.",
        "job_description": "Looking for a Python developer with ML expertise."
    }
    # Make a POST request to the /score endpoint
    response = client.post('/score', data=json.dumps(test_data), content_type='application/json')
    # Assert that the response status code is 200
    assert response.status_code == 200
    # Convert response data from JSON
    data = json.loads(response.data)
    # Check that the response contains the expected keys
    assert 'ats_score' in data
    assert isinstance(data['ats_score'], float)
