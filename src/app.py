from flask import Flask, jsonify
from src.ingestion import ingest_data
from src.data_preprocessing import preprocess_data
from src.model_building import build_generator, build_discriminator
from src.training import compile_gan, train_gan
from src.deployment import deploy_model_to_vertex_ai
from src.inference import generate_fashion_design

app = Flask(__name__)

# Global variables to store the models
generator = None
discriminator = None

def setup():
    global generator, discriminator
    # Step 1: Ingest Data
    ingest_data()

    # Step 2: Preprocess Data
    processed_data = preprocess_data()

    # Step 3: Build Models
    generator = build_generator()
    discriminator = build_discriminator()

    # Step 4: Compile and Train GAN
    gan = compile_gan(generator, discriminator)
    train_gan(generator, discriminator, gan, processed_data)

    # Step 5: Deploy Model
    deploy_model_to_vertex_ai("gs://fashion-model-bucket/gan_model", "fashion-gan-endpoint")

@app.route('/generate', methods=['GET'])
def generate():
    design = generate_fashion_design(generator)
    return jsonify({"design": design})

if __name__ == "__main__":
    setup()  # Run setup before starting the app
    app.run(host='0.0.0.0', port=8080)