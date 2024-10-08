import numpy as np

def generate_fashion_design(generator):
    noise = np.random.normal(0, 1, (1, 100))
    design = generator.predict(noise) 
    print(f"Generated fashion design: {design}")
    return design