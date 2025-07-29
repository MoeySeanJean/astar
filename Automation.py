import subprocess
import os
from itertools import combinations

os.makedirs("./data/instructions", exist_ok=True)

fruits = [
    "banana",
    "strawberry",
    "apple",
    "lemon",
    "peach",
    "pear",
    "orange",
    "plum"
]
containers = [
    "plate",
    "bowl"
]
cups = [
    "orange cup",
    "blue cup",
    "green cup",
    "yellow cup",
    "red cup",
    "purple cup"
]
others = [
    "rubiks cube"
]

all_items = fruits + containers + cups + others

instruction_templates_single = [
    "touch the {} on the table",
    "move the {} to the left side of the table",
    "move the {} to the right side of the table",
    "push the {} forward",
    "pull the {} backward",
    "pick up the {} carefully",
    "place the {} near the edge of the table",
    "rotate the {} slightly",
    "flip the {} upside down",
    "slide the {} toward the center of the table",
    "lift the {} a little",
    "tilt the {} to the left",
    "tilt the {} to the right",
    "gently nudge the {} to the side"
]

instruction_templates_multi = [
    "swap the positions of the {} and the {}",
    "stack the {} on top of the {}",
    "move the {} to the left and the {} to the right",
    "place the {} in front of the {}",
    "align the {} and the {} side by side",
    "push the {} under the {}",
    "rotate the {} and place it next to the {}",
    "pick up the {} and place it on the left of the {}",
    "pick up the {} and place it on the right of the {}"
]

instructions = []

for item in all_items:
    for template in instruction_templates_single:
        instructions.append(template.format(item))

two_item_combos = list(combinations(all_items, 2))

for (item1, item2) in two_item_combos:
    for template in instruction_templates_multi:
        instructions.append(template.format(item1, item2))

for idx, instruction in enumerate(instructions):
    instr_path = f"./data/instructions/{idx}.txt"
    obs_filename = f"./data/vids/{idx}.mp4"
    actions_filename = f"./data/actions/{idx}.txt"
    if os.path.exists(instr_path) and os.path.exists(obs_filename) and os.path.exists(actions_filename):
        print(f"[INFO] Skipping index {idx} (already done)")
        continue

    print(f"\n[INFO] Running simulation index {idx}: '{instruction}'")

    instr_path = f"./data/instructions/{idx}.txt"
    with open(instr_path, "w") as f:
        f.write(instruction)
    
    env = os.environ.copy()
    env["INSTRUCTION"] = instruction
    
    obs_filename = f"{idx}.mp4"
    actions_filename = f"{idx}.txt"
    
    subprocess.run([
        "python", "Simulation.py",
        "--save",
        "--no-render",
        "--save-obs-fname", obs_filename,
        "--save-actions-fname", actions_filename
    ], env=env)