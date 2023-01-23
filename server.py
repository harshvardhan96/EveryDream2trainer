import numpy as np
from flask import Flask, request, jsonify
import pickle
import joblib
import json
import subprocess

app = Flask(__name__)

@app.route('/train', methods=['GET'])
def train():
    result = subprocess.call(["python", "train.py", "--resume_ckpt", "sd_v1-5_vae", "--max_epochs", "50", "--data_root", "input",
                              "--lr_scheduler", "cosine", "--project_name", "myproj", "-batch_size", "6", "--sample_steps", "200",
                              "--lr", "3e-6", "--ckpt_every_n_minutes", "10", "--useadam8bit", "--ed1_mode"])
    if result != 0:
        print("Error: Script did not run correctly")
    else:
        print("Script ran successfully")
    output = result
    print("Output:", output)
    return "Training started"


if __name__ == '__main__' :
    app.run(debug=True)



