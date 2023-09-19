#!/usr/bin/env python3
"""Postprocess tabular file generated by ``SnpSift extractFields``."""
import argparse
import copy
import csv
import os

from resolwe_runtime_utils import send_message, warning

VALID_VAR_SOURCES = ["gatk_hc", "lofreq"]

parser = argparse.ArgumentParser(
    description="Postprocess tabular file generated by SnpSift extractFields."
)
parser.add_argument("--infile", help="Input *.tsv file.")
parser.add_argument("--outfile", help="Output *.tsv file.")
parser.add_argument(
    "--var-source",
    help="Tool used to make VCF file (must be one of tools in VALID_VAR_SOURCES).",
)


def iterate_snpeff_file(file_handle, filename):
    """Iterate entries in file produced by SnpSift extractFields."""
    for row in file_handle:
        # One line can contain two or more ALT values (and consequently two or more AF/AD values) Such "multiple"
        # entries are split into one ALT/AF/AD value per row. Lofreq data does not contain AD value, this is why
        # ``ad_s`` generation might appear messy (to cover the case with or without AD column).
        alts = row["ALT"].strip().split(",")
        afqs = row["AF"].strip().split(",")
        default_ad_s = ",".join([""] * (len(alts) + 1))
        # First entry is AD of REF allele, and the rest of them are for ALT alleles.
        ad_s = row.get("GEN[0].AD", default_ad_s).strip().split(",")[1:]
        if not (len(alts) == len(afqs) == len(ad_s)):
            send_message(
                warning(
                    "Inconsistency for entry {} in file {}. Skipping this entry.".format(
                        row, os.path.basename(filename)
                    )
                )
            )
            continue

        if len(ad_s) == 1:
            row["AD"] = ad_s[0]
            yield row
        else:
            for alt, afq, ad_ in zip(alts, afqs, ad_s):
                row_copy = copy.deepcopy(row)
                row_copy["ALT"] = alt
                row_copy["AF"] = afq
                if ad_:
                    row_copy["AD"] = ad_
                yield row_copy


if __name__ == "__main__":
    args = parser.parse_args()
    assert args.var_source.lower() in VALID_VAR_SOURCES

    with open(args.infile, "rt") as ifile, open(args.outfile, "wt") as ofile:
        infile = csv.DictReader(
            ifile, dialect="unix", delimiter="\t", restkey="additional_columns"
        )

        outfile = csv.writer(
            ofile, dialect="unix", delimiter="\t", quoting=csv.QUOTE_NONE
        )
        outfile.writerow(infile.fieldnames)

        for row in iterate_snpeff_file(infile, args.infile):
            if row.get("additional_columns", False):
                # There can be many entries in last two columns (EFF[*].GENE / EFF[*].AA) and they are separated with
                # tab-character. Therefore they appear as there are multiple additional_columns. By default they are
                # stored as list in a single 'additional_columns' column. They are then separeted (gene name vs. Amino
                # acid change), merged into appropriate column and seprated by comma.
                all_data = set(
                    [row["EFF[*].GENE"]]
                    + [row["EFF[*].AA"]]
                    + row["additional_columns"]
                ) - set([""])
                aa_changes = set(item for item in all_data if item.startswith("p."))
                row["EFF[*].AA"] = ",".join(sorted(aa_changes))
                genes = all_data - aa_changes
                row["EFF[*].GENE"] = ",".join(sorted(genes))

            if args.var_source.lower() == "lofreq":
                # Replace commas with semicolons in DP4 column, since opening in Excel results in strange formatting
                row["DP4"] = ";".join(row["DP4"].strip().split(","))
            elif args.var_source.lower() == "gatk_hc":
                # Fix AF calculation for GATK results. Output "empirical AF", rather then "theoretical AF".
                # See discussion here:
                # https://gatkforums.broadinstitute.org/gatk/discussion/6202/vcf-file-and-allele-frequency
                row["AF"] = int(row["AD"]) / int(row["DP"])

            outfile.writerow([row[column_name] for column_name in infile.fieldnames])
