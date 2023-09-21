"""Module that defines the Extractor class"""

import pathlib
from typing import List

# What workflow step do you want to extract? Eg. "DC"
# In that level which tool outputs do you want to extract? Eg. "de_novo"

# TODO: Refer https://github.com/segrelab/MiCoNE-pipeline-paper/blob/master/scripts/data_extraction/extract_figure7_data.py
DC_METHODS = (
    "closed_reference(.*)",
    "open_reference(.*)",
    "de_novo",
    "dada2",
    "deblur",
)
CC_METHODS = ("uchime", "remove_bimera")
TA_METHODS = ("blast(.*)", "naive_bayes(.*)", "naive_bayes(.*)")
OP_METHODS = ("normalize_filter(on)", "normalize_filter(off)")
GROUP_LEVEL = "group(Genus)"
NI_METHODS = (
    ("dir", "cozine"),
    ("dir", "flashweave"),
    ("dir", "harmonies"),
    ("dir", "mldm"),
    ("dir", "spieceasi"),
    ("dir", "spring"),
    ("corr", "pearson"),
    ("corr", "propr"),
    ("corr", "sparcc"),
    ("corr", "spearman"),
)

METHODS = {
    "DC": DC_METHODS,
    "CC": CC_METHODS,
    "TA": TA_METHODS,
    "OP": OP_METHODS,
    "GRP": GROUP_LEVEL,
    "NI": NI_METHODS,
}


class Extractor:
    """
    Class that parses workflow directory and extracts the required files.

        Parameters
        ---------
        input_folder : pathlib.Path
            Path to the workflow folder
        output_folder : pathlib.Path
            Path to the output folder where the files will be extracted
        metadata_id : str
            The metadata id of the workflow to be extracted

        Attributes
        ---------
        files : List[pathlib.Path]
            List of files to be extracted
    """

    def __init__(
        self,
        input_folder: pathlib.Path,
        output_folder: pathlib.Path,
        metadata_id: str,
    ):
        self._input_folder = input_folder
        self._output_folder = output_folder
        self._metadata_id = metadata_id
        # This gets all the files in the workflow folder
        self.files = self._get_files()

    # TODO: Add extract function that takes level and tool ids as input
