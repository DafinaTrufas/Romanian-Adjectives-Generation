from .utils import InflectionalClass, dec_letter_mapping, get_ro_fst
import pynini as pn


class Adj_Invariable(InflectionalClass):
    """Invariable

    Args:
        InflectionalClass (_type_): Abstract class for inflectional classes
    """

    def __init__(self, stem: str) -> None:
        self.stem = stem
        self.fst = self.make_word_fst()

    def make_word_fst(self):
        return pn.accep(self.stem, token_type="utf8").optimize()

    @dec_letter_mapping
    def to_msg(self) -> pn.Fst:
        return (self.fst).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return self.to_msg()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return self.to_msg()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_msg()
