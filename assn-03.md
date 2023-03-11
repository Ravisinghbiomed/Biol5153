# Assignment-3

## 1. Use rsync to upload the mt_genomes directory onto the AHPCC in `/storage/username`. So the final path is `/storage/username/mt_genomes`

`rsync -avh mt_genomes ravis@hpc-portal2.hpc.uark.edu:/storage/ravis`

## 2. Use scp or rsync to upload `unknown.fa`, which contains an unknown sequence

`scp /mnt/c/Users/pythonclass/watermelon_files/unknown.fa ravis@hpc-portal2.hpc.uark.edu:/storage/ravis`

## 3. Run BLAST

`#!/bin/bash

#SBATCH --job-name=test
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --tasks-per-node=32
#SBATCH --time=1:00:00
#SBATCH -o test_%j.out
#SBATCH -e test_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ravi@uark.edu

export OMP_NUM_THREADS=32

module purge
module load intel/18.0.1 impi/18.0.1 mkl/18.0.1
module load blast

###### concatenate all the genomes into a single file called ‘genomes.fas’

cd $SLURM_SUBMIT_DIR
cat *.fasta > genomes.fas

###### make a blast database of all the genomes

makeblastdb -in genomes.fas -dbtype nucl

###### search the unknown sequence against your database

blastn -query  /storage/ravis/unknown.fa  -db genomes.fas >  unknown.vs.genomes.blastn`


## 4. Use rsync to synchronize the remote mt_genomes, which contains your new output file, and your local version of mt_genomes.

From your local computer run `rsync -avh  ravis@hpc-portal2.hpc.uark.edu:/storage/ravis/mt_genomes /mnt/c/Users/pythonclass/watermelon_files`


## Answer following based on above script you ran:

#### How long did it take your job to complete

`00:00:06`

#### Closest match in the database

`Cucurbita`

#### Gene we got from blast hit is

`cox1`






ravisingh@LAPTOP-SHREESHYAMJI:/mnt/c/Users/pythonclass/watermelon_files$ 
