from .utils import InflectionalClass, dec_letter_mapping, get_ro_fst
import pynini as pn


class Adj2_4_i_semivowel(InflectionalClass):
    """2 forms, 4th type, -i(semivowel)

    Args:
        InflectionalClass (_type_): Abstract class for inflectional classes
    """

    def __init__(self, stem: str) -> None:
        self.stem = stem
        self.fst = self.make_word_fst()

    def make_word_fst(self):
        return pn.accep(self.stem[:-1], token_type="utf8").optimize()

    @dec_letter_mapping
    def to_msg(self) -> pn.Fst:
        return (self.fst + pn.accep(self.stem[-1])).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-1], "e")).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return self.to_msg()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_fsg()


class Adj2_4_ci(InflectionalClass):
    """2 forms, 4th type, -ci

    Args:
        InflectionalClass (_type_): Abstract class for inflectional classes
    """

    def __init__(self, stem: str) -> None:
        self.stem = stem
        self.fst = self.make_word_fst()

    def make_word_fst(self):
        return pn.accep(self.stem[:-1], token_type="utf8").optimize()

    @dec_letter_mapping
    def to_msg(self) -> pn.Fst:
        return (
            self.fst + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst(self.stem[-1]))
        ).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return (self.fst + pn.cross(get_ro_fst(self.stem[-1]), "e")).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return self.to_msg()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_fsg()
