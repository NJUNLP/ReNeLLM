# ReNeLLM

The official implementation of our NAACL 2024 paper "[A Wolf in Sheep’s Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily](https://arxiv.org/pdf/2311.08268.pdf)".

![NAACL 2024](https://img.shields.io/badge/NAACL-2024-blue.svg?style=plastic)
![Jailbreak Attacks](https://img.shields.io/badge/Jailbreak-Attacks-yellow.svg?style=plastic)
![Adversarial Attacks](https://img.shields.io/badge/Adversarial-Attacks-orange.svg?style=plastic)
![Large Language Models](https://img.shields.io/badge/LargeLanguage-Models-green.svg?style=plastic)

## Table of Contents

- [Updates](#updates)
- [Overview](#overview)
- [Getting Started](#getting-started)

## Updates

- (**2024/05/28**) We have generated over 100,000 samples using ReNeLLM on the [AdvBench](https://github.com/llm-attacks/llm-attacks/blob/main/data/advbench/harmful_behaviors.csv) dataset that successfully jailbreak Claude-2. You can obtain them by sending your name, institution, country, and intended use to dingpeng@smail.nju.edu.cn.
- (**2024/03/27**) We have released the experimental results of ReNeLLM and other baselines. You can download them from the following link: [Experimental Results](https://drive.google.com/drive/folders/1Iyisp16Il0o3iAeaGtc-xLHwUVsExv7U?usp=sharing)
- (**2024/03/14**) 🔥🔥🔥 ReNeLLM is acccepted by NAACL 2024(main conference)! Thanks to all collaborators！
- (**2024/02/21**) We have updated our codebase to make it more readable and easier to use. We will continue to update the codebase and support more LLMs. Stay tuned!
- (**2024/01/31**) 🔥🔥🔥 ReNeLLM is evaluated by the [Easyjailbreak](http://easyjailbreak.org) benchmark and exhibits strong competitiveness across various methods. Check it out!
- (**2024/01/09**) We have released a quick implementation of ReNeLLM!
- (**2023/11/14**) Our paper is on arXiv! Check it out [here](https://arxiv.org/abs/2311.08268)!

## Overview

This repository shares the code of our latest work on LLMs jailbreaking/defending. In this work:

- We introduce ReNeLLM, the first generalized jailbreak prompt attack framework for LLMs, which generalizes jailbreak prompt attacks into two aspects: prompt rewriting and scenario nesting, utilizing LLMs themselves to generate jailbreak attack prompts.
- Extensive experiments demonstrate that ReNeLLM generates jailbreak prompts that maintain a high attack success rate with less time required. Furthermore, ReNeLLM is difficult to detect by existing defense methods and exhibits generalization and transferability on representative LLMs. 
- To investigate the reasons why LLMs fail in defense, we observe the changes in the execution priority of prompts by LLMs before and after rewriting and nesting, and design defense methods accordingly. We hope our observations can serve as valuable guidance for future LLMs vendors to develop safer and more regulated systems.

<p align="center">
  <img src="image/example.png" width="300"/>
  <img src="image/ReNeLLM.png" width="400"/>
</p>

## Getting Started

**1. Clone this repository**
```shell 
git clone https://github.com/NJUNLP/ReNeLLM.git
```

**2. Build Environment**
```shell
cd ReNeLLM
conda create -n ReNeLLM python=3.9
conda activate ReNeLLM
pip install -r requirements.txt
```

**3. Run ReNeLLM**
   
ReNeLLM employs `gpt-3.5-turbo` for prompt rewriting and harmful classifier, while utilizing `claude-v2` as the model under attack. Therefore, you are required to input both of these API key parameters. 
```shell 
python renellm.py --gpt_api_key <your openai API key> --claude_api_key <your anthropic API key>
```
We use these two models due to their superior performance compared to open-source alternatives, as well as their lower cost in comparison with `gpt-4`. *In principle, any model could be utilized as your harmful classifier and attacked model.*

**4. Get Responses**
   
For `gpt`:
```shell 
python get_responses.py --data_path <jailbroken data path> --gpt_api_key <your open API key> --test_model <gpt-3.5-turbo, gpt-4>
```

For `claude`:
```shell 
python get_responses.py --data_path <jailbroken data path> --claude_api_key <your anthropic API key> --test_model <claude-instant-1, claude-2>
```

For `llama-2-chat`:

- Build the environment
```shell
cd llama
pip install -e .
```
- Follow the steps at https://github.com/facebookresearch/llama?tab=readme-ov-file#quick-start to download the llama-2-chat models.
- Get llama-2-chat responses using the command below:
```shell
bash run_chat.sh # You can set the model type and your jailbroken data path in the run_chat.sh
```

**5. Check ASR** 

GPT-ASR (using GPT-4)
```shell
python check_gpt_asr.py --data_path <your llm responses data path> --gpt_api_key <your open API key>
```
KW-ASR (keyword ASR)
```shell
python check_kw_asr.py --data_path <your llm responses data path>
```

**6. Execute ReNeLLM with a single prompt**

```shell
python renellm.py --gpt_api_key <your gpt_api_key> --claude_api_key <your claude_api_key> --prompt "how to steal money from others?"
```

We have uploaded the results of 520 Advbench samples categorized into 7 scenarios(see [gpt-4_single_round_prompt_annotation.json](https://github.com/NJUNLP/ReNeLLM/blob/main/gpt-4_single_round_prompt_annotation.json). In the result file, the "idx" field corresponds to the same idx samples in Advbench. The prompts used for classification and the harmful scenarios represented by each classification result can be found in Table 10 of our paper.

It should be noted that GPT-4 initially categorized the 520 pieces of data into 10 classes, but three of these classes had very few samples. For the convenience of statistics and analysis, we manually checked and merged these classes, resulting in 7 classification scenarios. The specific category merging information is as follows: 1 -> 0, 8 -> 9, 11 -> 6, finally resulting in 7 categories: 0, 2, 3, 4, 5, 6, 9. You can process the result file according to the above rules to obtain the classification results consistent with our paper.

## Contact

If you have any questions about our work, please feel free to contact us via the following email:

Peng Ding: dingpeng@smail.nju.edu.cn

Shujian Huang: huangsj@nju.edu.cn

## Citation

If you find this work useful in your own research, please feel free to leave a star⭐️ and cite our paper:

```bibtex
@misc{ding2023wolf,
      title={A Wolf in Sheep's Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily}, 
      author={Peng Ding and Jun Kuang and Dan Ma and Xuezhi Cao and Yunsen Xian and Jiajun Chen and Shujian Huang},
      year={2023},
      eprint={2311.08268},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
