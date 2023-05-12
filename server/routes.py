from .app import app
from llm_interactions.funcs import single_describe_call, bulk_description_call, breakdown_call
from llm_interactions.utils import try_function_n_times

from flask import request, jsonify

@app.route('/v1/breakdown', methods=['GET', 'POST'])
def breakdown():
    json = request.get_json()
    topic = json.get("topic")
    if not topic:
        return jsonify({
            "status": "error",
            "error": "No topic provided."
        })
    return jsonify(try_function_n_times(breakdown_call, 3, topic))
    
    
@app.route('/v1/describe', methods=['GET', 'POST'])
def describe():
    json = request.get_json()
    subtopic = json.get("subtopic")
    context = json.get("context")
    if not subtopic:
        return jsonify({
            "status": "error",
            "error": "No subtopic provided."
        })
    if not context:
        return jsonify({
            "status": "error",
            "error": "No context provided."
        })
    return jsonify(try_function_n_times(single_describe_call, 3, subtopic, context))
    
@app.route('/v1/bulk_describe', methods=['GET', 'POST'])
def bulk_describe():
    json = request.get_json()
    subtopics = json.get("subtopics")
    context = json.get("context")
    if not subtopics:
        return jsonify({
            "status": "error",
            "error": "No subtopics provided."
        })
    if not context:
        return jsonify({
            "status": "error",
            "error": "No context provided."
        })
    return jsonify(try_function_n_times(bulk_description_call, 3, subtopics, context))