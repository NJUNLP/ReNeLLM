# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from email import utils
from typing import Optional
import fire
import json, os

from llama import Llama
from torch.distributed.elastic.multiprocessing.errors import record

import sys
from pathlib import Path

current_file_path = Path(__file__)
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils.data_utils import jailbroken_data_reader

@record
def main(
    ckpt_dir: str,
    tokenizer_path: str,
    data_path: str,
    save_suffix: str = 'normal',
    baseline: str = 'renellm',
    # temperature: float = 0.6,
    temperature: float = 0,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    data = jailbroken_data_reader(data_path)

    # data = data[:1] # for test

    data_list = []

    system_prompt = ""
    system_message = {"role": "system",
                    "content": system_prompt
                    }

    for idx, item in enumerate(data):
        user_input = item['nested_prompt']
        user_message={"role": "user", "content": user_input}
        dialogs = []

        print(f"\n**** Process No.{idx+1} ****")

        print("\n**** Single round user prompt ****")
        print(user_input)
        print()
        # 将用户输入添加到messages中
        dialogs.append([system_message, user_message])

        # 发送API请求，输出API返回内容
        results = generator.chat_completion(
        dialogs,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )
        
        print(f"\n**** No.{idx+1} Round 1 model output ****\n")
        model_output = results[0]['generation']['content'].strip()
        print(
                f"> {results[0]['generation']['role'].capitalize()}: {model_output}"
            )


        item_new = {}
        item_new['idx']  = idx
        item_new['original_harm_behavior']  = item['original_harm_behavior']
        # item_new['rewritten_prompt']  = item['rewritten_prompt']

        item_new['nested_prompt']  = item['nested_prompt']
        item_new['baseline']  = baseline
        item_new['test_model'] = ckpt_dir[:-1]
        item_new['model_output'] = model_output


        data_list.append(item_new)

        continue
    
    # save the responses
    if not os.path.exists('../results/responses'):
        os.makedirs('../results/responses')
    # file_name = f"../results/responses/responses_of_{ckpt_dir[:-1]}_{save_suffix}.json"
    file_name = f"../results/responses/responses_of_{baseline}_on_{ckpt_dir[:-1]}_{save_suffix}.json"
        
    with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

    file_path = os.path.abspath(file_name)
    print(f"\nThe response file has been saved to:\n{file_path}\n")


if __name__ == "__main__":
    fire.Fire(main)
