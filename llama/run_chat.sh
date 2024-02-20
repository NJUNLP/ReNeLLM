# for llama-2-7b-chat
export OMP_NUM_THREADS=1
export CUDA_VISIBLE_DEVICES="7" 
torchrun --master_port 61888 --nproc_per_node 1 example_chat_completion.py \
    --ckpt_dir llama-2-7b-chat/ \
    --data_path your/path/to/ReNeLLM/results/renellm/final/judge_by_gpt-3.5-turbo_attack_on_anthropic.claude-v2_normal.json \
    --tokenizer_path tokenizer.model \
    --max_seq_len 3584 --max_batch_size 6


# # for llama-2-13b-chat
# export OMP_NUM_THREADS=1
# export CUDA_VISIBLE_DEVICES="5, 6" 
# torchrun --master_port 61343 --nproc_per_node 2 example_chat_completion.py \
#     --ckpt_dir llama-2-13b-chat/ \
#     --data_path your/path/to/ReNeLLM/results/renellm/final/judge_by_gpt-3.5-turbo_attack_on_anthropic.claude-v2_normal.json \
#     --tokenizer_path tokenizer.model \
#     --max_seq_len 3584 --max_batch_size 6


# # for llama-2-70b-chat
# export OMP_NUM_THREADS=1
# export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"
# torchrun --master_port 61200 --nproc_per_node 8 example_chat_completion.py \
#     --ckpt_dir llama-2-70b-chat/ \
#     --data_path your/path/to/ReNeLLM/results/renellm/final/judge_by_gpt-3.5-turbo_attack_on_anthropic.claude-v2_normal.json \
#     --tokenizer_path tokenizer.model \
#     --max_seq_len 3584 --max_batch_size 6