import pynini as pn
from abc import ABC, abstractmethod
from functools import cache, lru_cache


class InflectionalClass(ABC):
    @abstractmethod
    def make_word_fst(self) -> pn.Fst:
        """Generate the FST for the stem of the word

        Returns:
            pn.Fst: FST for the stem of the word
        """
        pass

    @abstractmethod
    def to_msg(self) -> pn.Fst:
        """To masculine singular

        Returns:
            pn.Fst: FST for the masculine singular form
        """
        pass

    @abstractmethod
    def to_fsg(self) -> pn.Fst:
        """To feminine singular

        Returns:
            pn.Fst: FST for the feminine singular form
        """
        pass

    @abstractmethod
    def to_mpl(self) -> pn.Fst:
        """To masculine plural

        Returns:
            pn.Fst: FST for the masculine plural form
        """
        pass

    @abstractmethod
    def to_fpl(self) -> pn.Fst:
        """To feminine plural

        Returns:
            pn.Fst: FST for the feminine plural form
        """
        pass


@cache
def letters_mapping(lang: str = "RO") -> pn.SymbolTable:
    """Map all ASCII + Romanian letters to pynini Symbol Table.
    Cached function since it performs a lot of computations but the result is always the same for RO.

    Reference: https://wellformedness.com/courses/LING83800/

    Returns:
        pn.SymbolTable: Symbol table with all ASCII + Romanian letters
    """
    letters_table = pn.SymbolTable()
    letters_table.add_symbol("<eps>", 0)

    for i in range(97, 123):
        # Add ASCII lowercase letters
        letters_table.add_symbol(f"{chr(i)}", i)

    if lang == "RO":
        # Add Romanian letters
        letters_table.add_symbol("ă", 259)
        letters_table.add_symbol("â", 226)
        letters_table.add_symbol("î", 238)
        letters_table.add_symbol("ș", 537)
        letters_table.add_symbol("ț", 539)
        letters_table.add_symbol("-", 45)

    return letters_table


@lru_cache(maxsize=20)
def dec_letter_mapping(func: callable) -> callable:
    """Add input/output symbols to the InflectionalClass subclass inflection method sub returned by the decorated function. Can be used when concatenating FSTs

    Args:
        func (callable): InflectionalClass subclass inflection method

    Returns:
        callable: Decorated function
    """

    def wrapper(*args: list, **kwargs: dict) -> pn.Fst:
        ascii_table = letters_mapping()
        res = func(*args, **kwargs)
        res.set_input_symbols(ascii_table)
        res.set_output_symbols(ascii_table)

        return res

    return wrapper


@lru_cache(maxsize=20)
def get_ro_fst(str_to_convert: str) -> pn.Fst | str:
    """Hack in order to easily use Romanian letters in pynini by substituting them with an acceptor of the same letter with utf8 token type

    Args:
        str_to_convert (str): Letter to be substituted with the corresponding utf8 acceptor

    Returns:
        pn.Fst: Acceptor of the input letter with utf8 token type
    """
    try:
        return pn.accep(str_to_convert, token_type="utf8")
    except KeyError:
        return str_to_convert
