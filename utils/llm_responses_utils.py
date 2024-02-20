from utils.llm_completion_utils import chatCompletion, claudeCompletion

def gpt_responses(args, text: str):
    user_input = text
    user_message={"role": "user", "content": user_input}
    messages = []
    messages.append(user_message)
    model_output = chatCompletion(args.test_model,
                                  messages,
                                  args.temperature,
                                  args.retry_times,
                                  args.round_sleep,
                                  args.fail_sleep,
                                  args.gpt_api_key,
                                  args.gpt_base_url)
    return model_output

def claude_responses(args, text: str):
    user_input = text
    model_output = claudeCompletion(
                args.test_model,
                args.max_tokens,
                args.temperature,
                user_input,
                args.retry_times,
                args.round_sleep,
                args.fail_sleep,
                args.claude_api_key,
                args.claude_base_url)
    return model_output

def llama2chat_responses():
    pass