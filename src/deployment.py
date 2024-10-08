from google.cloud import aiplatform

def deploy_model_to_vertex_ai(model_artifact, endpoint_name):
    aiplatform.init()
    model = aiplatform.Model.upload(display_name="fashion-gan-model", artifact_uri=model_artifact)
    endpoint = model.deploy(machine_type="n1-standard-4", endpoint_name=endpoint_name)
    return endpoint