#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script creates a .slurm file that can \ be submitted to the Pinnacle cluster")

# add positional (required) Arguments
parser.add_argument("job_name", help="The name of your job", type=str)

# add optional arguments
# the default for "store_true" is ... "False"
parser.add_argument ('-q', '--queue', help='specifiy the queue to submit the job to (default = comp01)')
parser.add_argument ('-n', '--nodes', help='specifiy the number of nodes to run on (default = 1)')
parser.add_argument ('-p', '--processors', help='specifiy the number of processors to use (default = 1)')
parser.add_argument ('-t', '--walltime', help='specifiy the allotted number of hours for the job (default = 01)')


# parse teh actual arguments
# access argument values via "args" variable
args = parser.parse_args()


#print variables
print('#SBATCH --job-name=' + args.job_name)
print('#SBATCH --partition', str(args.queue))
print('#SBATCH --nodes=' + str(args.nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(args.num_processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH -0 test_%j.out')
print('#SBATCH -e test_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=ravis@uark.edu')
#cd $SLURM_SUBMIT_DIR



