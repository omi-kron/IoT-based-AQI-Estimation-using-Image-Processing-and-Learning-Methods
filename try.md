# Ada Setup

YOU CANT USE SUDO COMMAND

[](https://hpc.iiit.ac.in/wiki/index.php/Ada_User_Guide)

[Slurm Workload Manager - Slurm Tutorials](https://slurm.schedmd.com/tutorials.html)

To get Gnode - 

```bash
srun --pty --partition=long --gres=gpu:1 --mem-per-cpu=2G -c 10 bash -l
```

—gres is for number of GPUs. 

—mem-per-cpu is the memory per cpu

-c is for number of CPUs

—nodelist to get a specific gnode e.g. —nodelist=gnode40

This is for 6 hours only.

sh get_node.sh

Scratch - Temporary storage for large files, Local disk attached to each compute node, 2.0 TB, 7 days

cd scratch

Create a new directory of your choice. Keep the data to run here. 

Ada home and Gnode home is same

To install any package, make sure that you have gnode access

Use nvidia-smi to get the GPU information

sinfo - to get the status of nodes

## Copying

scp and rsync

scp -r source destination\

scp -r <path to local file> <path to ada>

Example - file from local pc to Ada

When you are in local terminal

```bash
scp -r C:\Users\lenovo\Desktop\papers om.kathalkar@ada:~/home2/
```

When you are in ada terminal
