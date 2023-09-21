from .search import (
    SearchByScianId,
    SearchByScianString,
    SearchByCiiuId,
    SearchByCiiuString,
)
from typing import Dict


def scian_id_to_ciiu(scian: str) -> Dict:
    search = SearchByScianId()
    return search.find(scian) if scian is not None else {}


def scian_string_to_ciiu(scian: str) -> Dict:
    search = SearchByScianString()
    return search.find(scian) if scian is not None else {}


def ciiu_id_to_scian(ciiu: str) -> Dict:
    search = SearchByCiiuId()
    return search.find(ciiu) if ciiu is not None else {}


def ciiu_string_to_scian(ciiu: str) -> Dict:
    search = SearchByCiiuString()
    return search.find(ciiu) if ciiu is not None else {}
