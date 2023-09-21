from .search import (
    SearchByScianId,
    SearchByScianString,
    SearchByCiiuId,
    SearchByCiiuString,
)
from typing import Dict


def scian_id_to_ciiu(scian: str) -> Dict:
    scian = str(scian).lower()
    search = SearchByScianId()
    return search.find(scian) if scian is not None and scian != "" else {}


def scian_string_to_ciiu(scian: str) -> Dict:
    scian = str(scian).lower()
    search = SearchByScianString()
    return search.find(scian) if scian is not None and scian != "" else {}


def ciiu_id_to_scian(ciiu: str) -> Dict:
    ciiu = str(ciiu).lower()
    search = SearchByCiiuId()
    return search.find(ciiu) if ciiu is not None and ciiu != "" else {}


def ciiu_string_to_scian(ciiu: str) -> Dict:
    ciiu = str(ciiu).lower()
    search = SearchByCiiuString()
    return search.find(ciiu) if ciiu is not None and ciiu != "" else {}
