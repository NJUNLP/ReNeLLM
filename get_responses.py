import os
import json
import argparse

from utils.llm_completion_utils import chatCompletion, claudeCompletion
from utils.data_utils import jailbroken_data_reader
from utils.llm_responses_utils import gpt_responses, claude_responses, mistral_responses
from transformers import AutoModelForCausalLM, AutoTokenizer

def main(args):

    data = jailbroken_data_reader(args.data_path)

    # assert len(data) == 520

    # data = data[:1] # for test

    data_list = []

    if "mistral" in args.test_model:
        model_path = "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-aipnlp/BERT_TRAINING_SERVICE/platform/model/Mistral-7B-Instruct-v0.2"

        model = AutoModelForCausalLM.from_pretrained(model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)

    for idx, item in enumerate(data):
        nested_prompt = item['nested_prompt']

        if "gpt" in args.test_model:
            model_output = gpt_responses(args, nested_prompt)
            
        elif "claude" in args.test_model:
            model_output = claude_responses(args, nested_prompt)
        elif "mistral" in args.test_model:
            model_output = mistral_responses(args, model, tokenizer, nested_prompt)

        print(
                "\n################################\n\n"
                f"***** Current Data: {idx+1}/{len(data)} *****\n\n"
                f"***** Nested Prompt *****\n{nested_prompt}\n\n"
                f"***** Test Model *****\n{args.test_model}\n\n"
                f"***** Response of {args.test_model} *****\n\n"
                f"{model_output}\n\n"
                "################################\n")
        
        item_new = {}
        item_new['idx']  = idx
        item_new['original_harm_behavior']  = item['original_harm_behavior']
        # item_new['rewritten_prompt']  = item['rewritten_prompt']
        item_new['nested_prompt']  = item['nested_prompt']
        item_new['baseline']  = args.baseline
        item_new['test_model'] = args.test_model
        item_new['model_output'] = model_output

        data_list.append(item_new)

    # save the responses
    if not os.path.exists('./results/responses'):
        os.makedirs('./results/responses')
    file_name = f"./results/responses/responses_of_{args.baseline}_on_{args.test_model}_{args.save_suffix}.json"

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

    file_path = os.path.abspath(file_name)
    print(f"\nThe response file has been saved to:\n{file_path}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_path', type=str, required=True, help='data path to your renellm jailbroken json file')
    parser.add_argument('--baseline', type=str, default="renellm", choices=['renellm', 'gcg', 'autodan', 'pair'])
    parser.add_argument('--test_model', type=str, default="gpt-3.5-turbo", 
                        choices=["gpt-3.5-turbo", "gpt-4", \
                                 "anthropic.claude-instant-v1", "anthropic.claude-v2", "mistral"], help='which model to test')
    parser.add_argument('--temperature', type=float, default=0, help='model temperature')
    parser.add_argument("--max_tokens", type=int, default=3584)
    parser.add_argument('--round_sleep', type=int, default=5, help='sleep time between every round')
    parser.add_argument('--fail_sleep', type=int, default=5, help='sleep time for fail response')
    parser.add_argument('--retry_times', type=int, default=1000, help='retry times when exception occurs')
    parser.add_argument('--save_suffix', type=str, default="normal")
    parser.add_argument("--gpt_api_key", type=str, default=None)
    parser.add_argument("--claude_api_key", type=str, default=None)
    parser.add_argument("--gpt_base_url", type=str, default=None)
    parser.add_argument("--claude_base_url", type=str, default=None)

    args = parser.parse_args()

    main(args)
