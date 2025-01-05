from .utils import InflectionalClass, dec_letter_mapping, get_ro_fst
import pynini as pn


class Adj3_1_esc(InflectionalClass):
    """3 forms, 1st type, -esc

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
            + pn.cross(self.stem[-3], "ea")
            + pn.accep(self.stem[-2:])
            + get_ro_fst("ă")
        ).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (
            self.fst
            + pn.accep(self.stem[-3])
            + pn.cross(self.stem[-2], get_ro_fst("ș"))
            + pn.cross(self.stem[-1], get_ro_fst("t") + pn.accep("i"))
        ).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_mpl()


class Adj3_1_iu(InflectionalClass):
    """3 forms, 1st type, -iu

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
        return (self.fst + pn.accep(self.stem[-2:])).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-2:], "ie")).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-2:], get_ro_fst("ii"))).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_mpl()


class Adj3_1_others(InflectionalClass):
    """3 forms, 1st type, exception: roșu, nou
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
        if self.stem == 'roșu':
            return (self.fst + pn.accep('ie')).optimize()
        elif self.stem == 'nou':
            return (self.fst + pn.accep(self.stem[-1]) + pn.accep(get_ro_fst('ă'))).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        if self.stem == 'roșu':
            return (self.fst + pn.accep(get_ro_fst('ii'))).optimize()
        elif self.stem == 'nou':
            return (self.fst + pn.accep(get_ro_fst('i'))).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_mpl()


class Adj3_1_u_vowel(InflectionalClass):
    """3 forms, 1st type, -(u vowel) neologisms
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
        return (self.fst + pn.accep(self.stem[-2:])).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-2:], "ie")).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-2:], get_ro_fst("ii"))).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_mpl()


class Adj3_1_velar_consonant(InflectionalClass):
    """3 forms, 1st type, -(velar consonant)
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
        return self.fst.optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        return (self.fst + pn.accep(get_ro_fst("ă"))).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (self.fst + pn.accep(get_ro_fst("i"))).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return self.to_mpl()
