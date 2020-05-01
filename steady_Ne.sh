#!/bin/bash
#SBATCH --time=120:00:00
#SBATCH --mem=10Gb

aklog

sample_size=100
Ne=5000
recomb_map="/share/hennlab/reference/recombination_maps/genetic_map_AfricanAmerian/AAmap.superChr.map"
filename="steadyNe_Ne${Ne}_n${sample_size}"
outdir="/share/hennlab/projects/Ethiopians/msprime_sim_results/$filename/"

if [ ! -d $outdir ]
then
    mkdir $outdir
fi

start_time=$SECONDS
python /share/hennlab/lab_scripts/shyamie_msprime/py_msprime_scripts/steady_Ne.py -r $recomb_map -m 1e-8 -n $sample_size -N $Ne -g 100 -o ${outdir}/${filename}
end_time=$SECONDS
s_elapsed=`echo $end_time - $start_time | bc`

echo up_to_chr Ne Sample_size seconds
echo $chr $Ne $sample_size $s_elapsed
