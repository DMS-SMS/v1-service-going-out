from typing import List, Optional

from domain.entity.club import Club
from domain.repository.club_repository import ClubRepository
from infrastructure.club.club_handler import ClubHandler
from infrastructure.implementation.repository.mapper.club_repository_mapper import get_club_list_mapper


class ClubRepositoryImpl(ClubRepository):
    def __init__(self):
        self.club = ClubHandler()

    def find_all_by_floor(self, uuid: str, floor: int) -> List["Club"]:
        return get_club_list_mapper(self.club.get_club_informs_with_floor(uuid, floor))