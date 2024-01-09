# ReNeLLM
The implementation of our paper "A Wolf in Sheep’s Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily". The arxiv link is [here](https://arxiv.org/pdf/2311.08268.pdf).
<p>
  <img src="https://github.com/NJUNLP/ReNeLLM/assets/24366782/7b33de27-0967-435c-9818-98fd6b2ac306" alt="图片 1" width="35%">
  <img src="https://github.com/NJUNLP/ReNeLLM/assets/24366782/268b3505-91b5-4593-8457-37ea08c0c988" alt="图片 2" width="60%">
</p>

> Large Language Models (LLMs), such as ChatGPT and GPT-4, are designed to provide useful and safe responses. However, adversarial prompts known as 'jailbreaks' can circumvent safeguards, leading LLMs to generate potentially harmful content. Exploring jailbreak prompts can help to better reveal the weaknesses of LLMs and further steer us to secure them. Unfortunately, existing jailbreak methods either suffer from intricate manual design or require optimization on other white-box models, compromising generalization or efficiency. In this paper, we generalize jailbreak prompt attacks into two aspects: (1) Prompt **Re**writing and (2) Scenario **Ne**sting. Based on this, we propose **ReNeLLM**, an automatic framework that leverages LLMs themselves to generate effective jailbreak prompts. Extensive experiments demonstrate that ReNeLLM significantly improves the attack success rate while greatly reducing the time cost compared to existing baselines. Our study also reveals the inadequacy of current defense methods in safeguarding LLMs. Finally, we analyze the failure of LLMs defense from the perspective of prompt execution priority, and propose corresponding defense strategies. We hope that our research can catalyze both the academic community and LLMs vendors towards the provision of safer and more regulated LLMs.

## Dataset

We use the ***Harmful Behaviors*** dataset from paper "Universal and Transferable Adversarial Attacks on Aligned Language Models"([Zou et al., 2023](https://arxiv.org/pdf/2307.15043.pdf)), you can download the dataset from: [https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench](https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench).

## LLMs used in the paper

You need to access the following LLMs via official API and get responses through specific prompts.

|                  Function                   |  Model   |      Version       |
| :-----------------------------------------: | :------: | :----------------: |
|                   Rewrite                   | GPT-3.5  | gpt-3.5-turbo-0613 |
|   Harmfulness Classification (for attack)   | GPT-3.5  | gpt-3.5-turbo-0613 |
|     LLM's response to the nestd prompt      | Claude-2 |     claude-v2      |
| Harmfulness Classification (for evaluation) |  GPT-4   |     gpt-4-0613     |

## Code description



