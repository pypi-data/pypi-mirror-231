from typing import List, Dict
from abc import ABC
from .data import data


class Search(ABC):
    def find(self, input: str) -> Dict:
        """function that retun the list of results"""


class SearchByScianId(Search):
    def find(self, input: str) -> Dict:
        res = {}
        for d in data:
            if input in d["SCIAN"].lower():
                if d["CIIU"] not in res:
                    res[d["CIIU"]] = list()
                if d["CIIU_string"] not in res[d["CIIU"]]:
                    res[d["CIIU"]].append(d["CIIU_string"])
        return res


class SearchByScianString(Search):
    def find(self, input: str) -> Dict:
        res = {}
        for d in data:
            if input in d["SCIAN_string"].lower():
                if d["CIIU"] not in res:
                    res[d["CIIU"]] = list()
                if d["CIIU_string"] not in res[d["CIIU"]]:
                    res[d["CIIU"]].append(d["CIIU_string"])
        return res


class SearchByCiiuId(Search):
    def find(self, input: str) -> Dict:
        res = {}
        for d in data:
            if input == d["CIIU"]:
                if d["SCIAN"] not in res:
                    res[d["SCIAN"]] = list()
                if d["SCIAN_string"] not in res[d["SCIAN"]]:
                    res[d["SCIAN"]].append(d["SCIAN_string"])
        return res


class SearchByCiiuString(Search):
    def find(self, input: str) -> Dict:
        res = {}
        for d in data:
            if input in d["CIIU_string"].lower():
                if d["SCIAN"] not in res:
                    res[d["SCIAN"]] = list()
                if d["SCIAN_string"] not in res[d["SCIAN"]]:
                    res[d["SCIAN"]].append(d["SCIAN_string"])
        return res
