from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.model import compute_ats_score

main_bp = Blueprint('main', __name__)

@main_bp.route('/score', methods=['POST'])
@swag_from({
    'tags': ['ATS Scoring'],
    'description': 'Calculate ATS score for a given resume and job description.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'resume': {
                        'type': 'string',
                        'example': 'Sample resume text'
                    },
                    'job_description': {
                        'type': 'string',
                        'example': 'Sample job description text'
                    }
                },
                'required': ['resume', 'job_description']
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'A JSON object with the ATS score.',
            'schema': {
                'type': 'object',
                'properties': {
                    'resume': {'type': 'string'},
                    'job_description': {'type': 'string'},
                    'ats_score': {'type': 'number'}
                }
            }
        }
    }
})
def score_resume():
    data = request.get_json()
    resume_text = data.get('resume', '')
    job_description = data.get('job_description', '')
    
    # Dummy ATS score calculation (to be replaced with model logic later)
    # dummy_score = 0.85

    # Calculate ATS score using the model
    ats_score = compute_ats_score(resume_text, job_description)
    
    return jsonify({
        'resume': resume_text,
        'job_description': job_description,
        'ats_score': ats_score
    })
