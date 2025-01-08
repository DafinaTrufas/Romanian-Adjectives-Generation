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

from fst_classes.fst_adj_2_1 import Adj2_1_e
from fst_classes.fst_adj_2_2 import Adj2_2_palatal_consonant, Adj2_2_ui
from fst_classes.fst_adj_2_3 import Adj2_3_e_neologisms
from fst_classes.fst_adj_2_4 import Adj2_4_i_semivowel, Adj2_4_ci

from fst_classes.fst_adj_inv import Adj_Invariable


class Adjective:
    """General class for handling adjective inflection

    Returns:
        _type_: _description_
    """

    terminations = {
        "(?!^roșu$)(^.*[^aeioâă]u$)": (Adj4_0_u, "4 forme, -u"),
        "(?!^roșu$)(?!^nou$)(^.*[aeo]u$)": (Adj4_0_u_sem, "4 forme, -u (semivocalic)"),
        "(?!^.*tor$)((^.*[aeiouăâ]c|g$)|(^.*[^aeiouăâîcg]$))": (
            Adj4_0_consonant,
            "4 forme, -(consoană)",
        ),
        "(?!^.*esc$)(^.*[c|g]$)": (
            Adj3_1_velar_consonant,
            "3 forme, -(consoană velară)",
        ),
        "(roșu|nou|june)$": (Adj3_1_others, "3 forme, roșu/nou"),
        "esc$": (Adj3_1_esc, "3 forme, tip 1, -esc"),
        "iu$": (Adj3_1_iu, "3 forme, tip 1, -iu"),
        "tor$": (Adj3_2_tor, "3 forme, tip 2, -tor"),
        "âu$": (Adj3_2_âu, "3 forme, tip 2, -âu"),
        "ău$": (Adj3_2_ău, "3 forme, tip 2, -âu"),
        "^(?!.*che$).*e$": (Adj2_1_e, "2 forme, tip 1, -e"),
        "(che|chi|ghe|ghi)$": (
            Adj2_2_palatal_consonant,
            "2 forme, tip 2, -(consoană palatală)",
        ),
        "ui$": (Adj2_2_ui, "2 forme, tip 2, -ui"),
        "(ai|ei|oi)$": (Adj2_4_i_semivowel, "2 forme, tip 4, -i(semivocalic)"),
        "ci$": (Adj2_4_ci, "2 forme, tip 4, -ci"),
    }

    def __init__(self, stem: str, invariable: bool = False) -> None:
        """Constructor for Adjective class

        Args:
            stem (str): Adjective stem
        """
        self.stem = stem
        self.generated_forms = []
        self.invariable = invariable

        self.inflectional_class, self.rule_description = self.get_inflectional_class()

        self.inflectional_obj = self.inflectional_class(self.stem)

    def get_inflectional_class(self) -> tuple:
        """Get the inflectional class of the adjective stem based on the terminations dictionary

        Returns:
            tuple: Inflectional class and rule description
        """
        if self.invariable:
            return (Adj_Invariable, "invariabil")

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
        # adj = Adjective("acru")
        # adj = Adjective("alb")
        # adj = Adjective("greu")
        # adj = Adjective("haiducesc")
        # adj = Adjective("cenușiu")
        # adj = Adjective("răbdător")
        # adj = Adjective("lălâu")
        # adj = Adjective("clănțău")
        # adj = Adjective("adânc")
        # adj = Adjective("roșu")
        # adj = Adjective("nou")
        # adj = Adjective("dulce")
        # adj = Adjective("vechi")
        # adj = Adjective("gălbui")
        # adj = Adjective("dibaci")
        # adj = Adjective('bej', invariable=True)
        # adj = Adjective('a-tot-văzător', invariable=False)
        # adj = Adjective('aalenian', invariable=False)
        # adj = Adjective('abalienat', invariable=False)
        # adj = Adjective('abătut', invariable=False)
        # adj = Adjective('abdus', invariable=False)
        # adj = Adjective("aburos", invariable=False)
        # adj = Adjective("june", invariable=False)
        # adj = Adjective("absolutoriu", invariable=False)
        # adj = Adjective("călâi", invariable=False)
        adj = Adjective("spânău", invariable=False)

        adj.generate_all_forms()

        print(adj.rule_description)
        print("____")
        for form in adj.generated_forms:
            print(form)
    except ValueError as e:
        print(e)
