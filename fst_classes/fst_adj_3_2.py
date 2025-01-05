from .utils import InflectionalClass, dec_letter_mapping, get_ro_fst
import pynini as pn


class Adj3_2_tor(InflectionalClass):
    """3 forms, 2nd type, -tor

    Args:
        InflectionalClass (_type_): Abstract class for inflectional classes
    """

    def __init__(self, stem: str) -> None:
        self.stem = stem
        self.fst = self.make_word_fst()

    def make_word_fst(self):
        return pn.accep(self.stem[:-3], token_type="utf8").optimize()

    @dec_letter_mapping
    def to_msg(self) -> pn.Fst:
        return (self.fst + pn.accep(self.stem[-3:])).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return (
            self.fst
            + pn.accep(self.stem[-3])
            + pn.cross(self.stem[-2], "oa")
            + pn.accep(self.stem[-1])
            + pn.accep("e")
        ).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (self.fst + pn.accep(self.stem[-3:]) + pn.accep("i")).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_fsg()


class Adj3_2_âu(InflectionalClass):
    """3 forms, 2nd type, -âu

    Args:
        InflectionalClass (_type_): Abstract class for inflectional classes
    """

    def __init__(self, stem: str) -> None:
        self.stem = stem
        self.fst = self.make_word_fst()

    def make_word_fst(self):
        return pn.accep(self.stem[:-2], token_type="utf8").optimize()

    @dec_letter_mapping
    def to_msg(self) -> pn.Fst:
        return (self.fst + pn.accep(self.stem[-2:], token_type="utf8")).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return (
            self.fst
            + pn.accep(self.stem[-2], token_type="utf8")
            + pn.cross(self.stem[-1], "i")
            + pn.accep("e")
        ).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (
            self.fst
            + pn.accep(self.stem[-2], token_type="utf8")
            + pn.cross(self.stem[-1], "i")
        ).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_fsg()


class Adj3_2_ău(InflectionalClass):
    """3 forms, 2nd type, -âu

    Args:
        InflectionalClass (_type_): Abstract class for inflectional classes
    """

    def __init__(self, stem: str) -> None:
        self.stem = stem
        self.fst = self.make_word_fst()

    def make_word_fst(self):
        return pn.accep(self.stem[:-2], token_type="utf8").optimize()

    @dec_letter_mapping
    def to_msg(self) -> pn.Fst:
        return (self.fst + pn.accep(self.stem[-2:], token_type="utf8")).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return (
            self.fst
            + pn.cross(get_ro_fst(self.stem[-2]), "a")
            + pn.cross(self.stem[-1], "ie")
        ).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (
            self.fst
            + pn.accep(self.stem[-2], token_type="utf8")
            + pn.cross(self.stem[-1], "i")
        ).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_fsg()


class Adj3_2_eu_neologisms(InflectionalClass):
    """3 forms, 2nd type, -eu (neologisms)
    Args:
        InflectionalClass (_type_): Abstract class for inflectional classes
    """

    def __init__(self, stem: str) -> None:
        raise NotImplementedError("This class is not implemented yet")

    def make_word_fst(self):
        pass

    @dec_letter_mapping
    def to_msg(self) -> pn.Fst:
        pass

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        pass

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        pass

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        pass
