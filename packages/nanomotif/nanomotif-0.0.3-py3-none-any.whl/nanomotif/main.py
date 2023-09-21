import nanomotif as nm


def main():

    args = nm.argparser.create_parser()

    assembly = nm.load_assembly(args.assembly)
    pileup = nm.load_pileup(args.pileup)

    motifs = process_sample(
        assembly,
        pileup,
        args.output,
        args.max_motif_length,
        args.min_fraction,
        args.min_coverage,
        args.min_kl_divergence,
        args.min_cdf_score,
        args.cdf_position
    )

    motifs.write_csv(args.output, separator="\t", index=False)

if __name__ == "__main__":
    main()