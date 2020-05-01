#! /usr/bin/env python
import sys
import argparse as ap

import msprime as ms
import pandas as pd
import tskit
import math

def main(args):
    ## Parse arguments
    argp = ap.ArgumentParser(description="")
    argp.add_argument("-r", "--recomb_map")
    argp.add_argument("-m", "--mutation_rate", type=float)
    argp.add_argument("-n", "--sample_size", type=int)
    argp.add_argument("-N", "--Ne", type=int)
    argp.add_argument("-g", "--g_switch", type=int)
    argp.add_argument("-o", "--output")
    args = argp.parse_args(args)

    recomb_map = ms.RecombinationMap.read_hapmap(args.recomb_map)
    chr_seq = ms.simulate(sample_size=args.sample_size, Ne=args.Ne, recombination_map=recomb_map, mutation_rate=args.mutation_rate, model="dtwf", demographic_events=[ms.SimulationModelChange(time=args.g_switch, model="hudson"), ms.PopulationParametersChange(initial_size=args.Ne, time=0), ms.PopulationParametersChange(initial_size=10000, time=args.g_switch+10)])
    with open(args.output + ".vcf", "w") as vcf_file:
        chr_seq.write_vcf(vcf_file, ploidy=2)

## Run script
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
