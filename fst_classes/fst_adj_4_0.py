from .utils import InflectionalClass, dec_letter_mapping, get_ro_fst
import pynini as pn


class Adj4_0_u(InflectionalClass):
    """4 forms, -u

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
        return (self.fst + pn.cross(self.stem[-1], get_ro_fst("ă"))).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-1], "i")).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-1], "e")).optimize()


class Adj4_0_u_sem(InflectionalClass):
    """4 forms, -u (semivowel)

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
        return (self.fst + pn.cross(self.stem[-1], "a")).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-1], "i")).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        return (self.fst + pn.cross(self.stem[-1], "le")).optimize()


class Adj4_0_consonant(InflectionalClass):
    """4 forms, -(consonant)

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
        return (
            self.fst
            + pn.cross(get_ro_fst(self.stem[-2]), get_ro_fst(self.stem[-2]))
            + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst(self.stem[-1]))
        ).optimize()

    @dec_letter_mapping
    def to_fsg(self) -> pn.Fst:
        if self.stem[-3:] in ["ros", "ios", "sor"]:
            return (
                self.fst
                + pn.cross(get_ro_fst(self.stem[-2]), "oa")
                + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst(self.stem[-1]))
                + pn.cross("", get_ro_fst("ă"))
            ).optimize()

        return (
            self.fst
            + pn.cross(get_ro_fst(self.stem[-2]), get_ro_fst(self.stem[-2]))
            + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst(self.stem[-1]))
            + pn.cross("", get_ro_fst("ă"))
        ).optimize()

    @dec_letter_mapping
    def to_mpl(self) -> pn.Fst:
        if self.stem[-3:] in ["ean"]:
            return (
                self.fst
                + pn.cross(get_ro_fst(self.stem[-2]), "")
                + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst(self.stem[-1]))
                + pn.cross("", "i")
            ).optimize()

        if self.stem[-3:] in ["ros"]:
            return (
                self.fst
                + pn.cross(get_ro_fst(self.stem[-2]), get_ro_fst(self.stem[-2]))
                + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst("ș"))
                + pn.cross("", "i")
            ).optimize()

        return (
            self.fst
            + pn.cross(
                get_ro_fst(self.stem[-2]),
                "e"
                if self.stem[-2:] in ["an"] and self.stem[-3] not in ["e"]
                else get_ro_fst("ș")
                if self.stem[-2:] in ["st"]
                else get_ro_fst(self.stem[-2]),
            )
            + pn.cross(
                get_ro_fst(self.stem[-1]),
                get_ro_fst("ț")
                if self.stem[-2:] in ["at", "ut", "nt", "ct", "it", "pt"]
                else get_ro_fst("ș")
                if self.stem[-2:] in ["us", "ns", "as", "is", "os"]
                else get_ro_fst("z")
                if self.stem[-2:] in ["rd", "nd", "ad", "id", "od"]
                else get_ro_fst(self.stem[-1]),
            )
            + pn.cross("", "i")
        ).optimize()

    @dec_letter_mapping
    def to_fpl(self) -> pn.Fst:
        if self.stem[-3:] in ["ean"]:
            return (
                self.fst
                + pn.cross(get_ro_fst(self.stem[-2]), "")
                + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst(self.stem[-1]))
                + pn.cross("", "e")
            ).optimize()

        if self.stem[-3:] in ["ros", "ios", "sor"]:
            return (
                self.fst
                + pn.cross(get_ro_fst(self.stem[-2]), "oa")
                + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst(self.stem[-1]))
                + pn.cross("", "e")
            ).optimize()

        return (
            self.fst
            + pn.cross(
                get_ro_fst(self.stem[-2]),
                "e" if self.stem[-2:] in ["an"] else get_ro_fst(self.stem[-2]),
            )
            + pn.cross(get_ro_fst(self.stem[-1]), get_ro_fst(self.stem[-1]))
            + pn.cross("", "e")
        ).optimize()
