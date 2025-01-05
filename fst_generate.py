"""References:
https://wellformedness.com/courses/LING83800/
"""


import re

from fst_classes.fst_adj_4_0 import Adj4_0_u, Adj4_0_u_sem, Adj4_0_consonant
from fst_classes.fst_adj_3_1 import (
    Adj3_1_esc,
    Adj3_1_velar_consonant,
    Adj3_1_iu,
    Adj3_1_u_vowel,
    Adj3_1_others,
)
from fst_classes.fst_adj_3_2 import (
    Adj3_2_tor,
    Adj3_2_eu_neologisms,
    Adj3_2_âu,
    Adj3_2_ău,
)


class Adjective:
    """General class for handling adjective inflection

    Returns:
        _type_: _description_
    """

    terminations = {
        "[^aeioâă]u$": (Adj4_0_u, "4 forme, -u"),
        "[aeo]u$": (Adj4_0_u_sem, "4 forme, -u (semivocalic)"),  # ?
        # "???$": (Adj4_0_consonant, "4 forme, -(consoana)"),
        # "???$": (Adj4_0_consonant, "3 forme, -(consoana velara)"),
        "esc$": (Adj3_1_esc, "3 forme, tip 1, -esc"),
        "iu$": (Adj3_1_iu, "3 forme, tip 1, -iu"),
        "tor$": (Adj3_2_tor, "3 forme, tip 2, -tor"),
        "âu$": (Adj3_2_âu, "3 forme, tip 2, -âu"),
        "ău$": (Adj3_2_ău, "3 forme, tip 2, -âu"),
    }

    def __init__(self, stem: str) -> None:
        """Constructor for Adjective class

        Args:
            stem (str): Adjective stem
        """
        self.stem = stem
        self.generated_forms = []

        self.inflectional_class, self.rule_description = self.get_inflectional_class()

        self.inflectional_obj = self.inflectional_class(self.stem)

    def get_inflectional_class(self) -> tuple:
        """Get the inflectional class of the adjective stem based on the terminations dictionary

        Returns:
            tuple: Inflectional class and rule description
        """
        for term in self.terminations:
            if re.search(term, self.stem):
                return self.terminations[term]

        raise ValueError(
            f"Adjective stem {self.stem} does not match any inflectional class"
        )

    def generate_all_forms(self) -> None:
        """Generate all inflectional forms based on the adjective stem"""
        self.generated_forms.append(self.inflectional_obj.to_msg())
        self.generated_forms.append(self.inflectional_obj.to_fsg())
        self.generated_forms.append(self.inflectional_obj.to_mpl())
        self.generated_forms.append(self.inflectional_obj.to_fpl())


if __name__ == "__main__":
    try:
        adj = Adjective("acru")
        # adj = Adjective("greu")
        # adj = Adjective("haiducesc")
        # adj = Adjective("cenușiu")
        # adj = Adjective("răbdător")
        # adj = Adjective("lălâu")
        # adj = Adjective("clănțău")
        adj.generate_all_forms()

        print(adj.rule_description)
        print("____")
        for form in adj.generated_forms:
            print(form)
    except ValueError as e:
        print(e)
