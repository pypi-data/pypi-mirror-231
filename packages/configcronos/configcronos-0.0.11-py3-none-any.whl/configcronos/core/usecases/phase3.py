from configcronos.core.entities import Phase3, Phase3Segmentos
from configcronos.core.repositories import Phase3Repository


class Phase3Service:

    def __init__(self, phase3_repository: Phase3Repository) -> None:
        self.phase3_repository = phase3_repository

    def get_phase3(self) -> Phase3:
        response = self.phase3_repository.get_phase3()
        data = response['data'][0]
        phase3 = Phase3.from_dict(data)
        return phase3

    def get_phase3_segments(self) -> Phase3Segmentos:
        response = self.phase3_repository.get_phase3_segments()
        data = response['data'][0]
        phase3_segments = Phase3Segmentos.from_dict(data)
        return phase3_segments
