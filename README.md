# ReNeLLM
The official implementation of our paper "[A Wolf in Sheep’s Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily](https://arxiv.org/pdf/2311.08268.pdf)".

[![arXiv](https://img.shields.io/badge/cs.LG-arXiv%3A2311.08268-b31b1b)](https://arxiv.org/abs/2311.08268)
![Jailbreak Attacks](https://img.shields.io/badge/Jailbreak-Attacks-yellow.svg?style=plastic)
![Adversarial Attacks](https://img.shields.io/badge/Adversarial-Attacks-orange.svg?style=plastic)
![Large Language Models](https://img.shields.io/badge/LargeLanguage-Models-green.svg?style=plastic)

## Table of Contents
- [Updates](#updates)
- [Overview](#overview)
- [Getting Started](#getting-started)
- [Contact](#contact)
- [Citation](#citation)

## Updates
- (**2024/01/31**) 🔥🔥🔥 ReNeLLM is evaluated by the [Easyjailbreak](http://easyjailbreak.org) benchmark and exhibits strong competitiveness across various methods. Check it out!
- (**2024/01/09**) We have released a quick implementation of ReNeLLM!
- (**2023/11/14**) Our paper is on arXiv! Check it out [here](https://arxiv.org/abs/2311.08268)!

## Overview
This repository shares the code of our latest work on LLMs jailbreaking/defending. In this work:

- We introduce ReNeLLM, the first generalized jailbreak prompt attack framework for LLMs, which generalizes jailbreak prompt attacks into two aspects: prompt rewriting and scenario nesting, utilizing LLMs themselves to generate jailbreak attack prompts.
- Extensive experiments demonstrate that ReNeLLM generates jailbreak prompts that maintain a high attack success rate with less time required. Furthermore, ReNeLLM is difficult to detect by existing defense methods and exhibits generalization and transferability on representative LLMs. 
- To investigate the reasons why LLMs fail in defense, we observe the changes in the execution priority of prompts by LLMs before and after rewriting and nesting, and design defense methods accordingly. We hope our observations can serve as valuable guidance for future LLMs vendors to develop safer and more regulated systems.

<p align="center">
  <img src="example.png" width="300"/>
  <img src="ReNeLLM.png" width="400"/>
</p>

## Getting Started
1. **Clone this repository**
```shell 
git clone https://github.com/NJUNLP/ReNeLLM.git
```

2. **Build Environment**
```shell
cd ReNeLLM
conda create -n ReNeLLM python=3.9
conda activate ReNeLLM
pip install -r requirements.txt
```

3. **Run ReNeLLM**
ReNeLLM employs `gpt-3.5-turbo` for prompt rewriting and harmful classifier, while utilizing `claude-v2` as the model under attack. Therefore, you are required to input both of these API key parameters. 
```shell 
python renellm.py --gpt_api_key <your openai API key> --claude_api_key <your anthropic API key>
```
We use these two models due to their superior performance compared to open-source alternatives, as well as their lower cost in comparison with `gpt-4`. *In principle, any model could be utilized as your harmful classifier and attacked model.*

4. **Get Responses**
For `gpt`:
```shell 
python get_responses.py --data_path <jailbroken data path> --gpt_api_key <your open API key> --test_model <gpt-3.5-turbo, gpt-4>
```

For `claude`:
```shell 
python get_responses.py --data_path <jailbroken data path> --claude_api_key <your anthropic API key> --test_model <anthropic.claude-v1, anthropic.claude-v2>
```

For `llama-2-chat`:
1. Build the environment
```shell
cd llama
pip install -e .
```
2. Follow the steps at https://github.com/facebookresearch/llama?tab=readme-ov-file#quick-start to download the llama-2-chat models.
3. Get llama-2-chat responses using the command below:
```shell
bash run_chat.sh # You can set the model type and your jailbroken data path in the run_chat.sh
```
## Contact
If you have any questions about our work, please feel free to contact us via the following email:

Peng Ding: dingpeng@smail.nju.edu.cn

Shujian Huang: huangsj@nju.edu.cn

## Citation
If you find this work useful in your own research, please feel free to leave a star⭐️ and cite our paper:

```bibtex
@article{ding2023wolf,
  title={A Wolf in Sheep's Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily},
  author={Ding, Peng and Kuang, Jun and Ma, Dan and Cao, Xuezhi and Xian, Yunsen and Chen, Jiajun and Huang, Shujian},
  journal={arXiv preprint arXiv:2311.08268},
  year={2023}
}
```
