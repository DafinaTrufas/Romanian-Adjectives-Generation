from .utils import InflectionalClass, dec_letter_mapping, get_ro_fst
import pynini as pn


class Adj2_1_e(InflectionalClass):
    """2 forms, 1st type, -e

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
        return self.to_msg()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-1], get_ro_fst("i"))).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_mpl()
