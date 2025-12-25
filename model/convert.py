from mlx_lm import convert

repo = "vinhpham131/vnuk-chatbot-merged"
upload_repo = './mlx_model_q6'

convert(
    hf_path= repo,
    mlx_path= upload_repo,
    quantize=True,
    q_bits=6,
    q_group_size=128,
)