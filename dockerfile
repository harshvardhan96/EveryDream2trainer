FROM python:3.9

git clone https://github.com/harshvardhan96/EveryDream2trainer.git

cd EveryDream2trainer

pip install -r requirements.txt

wget https://huggingface.co/panopstor/EveryDream/blob/main/sd_v1-5_vae.ckpt

python utils/convert_original_stable_diffusion_to_diffusers.py --scheduler_type ddim --original_config_file v1-inference.yaml --image_size 512 --checkpoint_path sd_v1-5_vae.ckpt --prediction_type epsilon --upcast_attn False --dump_path "ckpt_cache/sd_v1-5_vae"

python server.py