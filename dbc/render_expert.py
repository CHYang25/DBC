import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import os, sys
import argparse
import numpy as np
import gym
import d4rl  # Import required to register environments
from torch.utils.data import Dataset, DataLoader
from rlf.algos import BaseAlgo, BehavioralCloning, DBC
from tqdm import tqdm
from PIL import Image
from rlf.rl.envs import make_env
from rlf.envs.env_interface import get_env_interface

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--env_name', type=str, default='maze2d-medium-v2')
    parser.add_argument('--expert_dataset', type=str, default='expert_datasets/maze.pt')
    parser.add_argument('--save_path', type=str, default='data/image')
    parser.add_argument('--seed', type=int, default=1)
    args = parser.parse_args()

    env_interface = get_env_interface(args.env_name)(args)
    env_interface.setup(args, None)

    expert_data = torch.load(args.expert_dataset)

    args.il_out_action_norm=True
    args.bc_state_norm=True
    args.warp_frame=False

    env = make_env(
        rank=0,
        env_id=args.env_name,
        seed=0,
        allow_early_resets=False,
        env_interface=env_interface,
        set_eval=False,
        alg_env_settings=DBC().get_env_settings(args),
        args=args,
        immediate_call=True,
    )
    print(expert_data['obs'][0])
    print(expert_data['actions'][0])
    env.reset_model_(expert_data['obs'][0])

    frame = env.render('rgb_array')
    im = Image.fromarray(frame)
    im.save(os.path.join(args.save_path, "image.png"))