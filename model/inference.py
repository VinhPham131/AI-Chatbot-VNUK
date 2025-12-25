from mlx_lm import load, generate, stream_generate

def format_llama3_chat(system_prompt, user_prompt, tokenizer):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

def generate_response(data, model, tokenizer):
    system_prompt = "You are an AI-powered virtual assistant designed to support students of the VN–UK Institute for Research and Executive Education (VNUK). You provide accurate, concise, and up-to-date information related to academic programs, scholarships, tuition fees, admissions, and student exchange opportunities. Your responses should be factual, easy to understand, and aligned with information published on VNUK's official website."
    user_prompt = data.get("message")

    max_tokens = data.get('max_tokens', 512)
    prompt = format_llama3_chat(system_prompt, user_prompt, tokenizer)
    
    response = generate(
        model,
        tokenizer,
        prompt=prompt,
        verbose=False,
        max_tokens=max_tokens
    )
    return response
    
def stream_generate_response(data, model, tokenizer):
    system_prompt = "You are an AI-powered virtual assistant designed to support students of the VN–UK Institute for Research and Executive Education (VNUK). You provide accurate, concise, and up-to-date information related to academic programs, scholarships, tuition fees, admissions, and student exchange opportunities. Your responses should be factual, easy to understand, and aligned with information published on VNUK's official website."
    user_prompt = data.get("message")

    max_tokens = data.get("max_tokens", 512)

    prompt = format_llama3_chat(system_prompt, user_prompt, tokenizer)

    for chunk in stream_generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=max_tokens,
    ):
        yield chunk.text


