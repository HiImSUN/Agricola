"""
자원 시장 기본 행동
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


# Todo

class ResourceMarket(Command):
    def __init__(self, player):
        self.log_text = None
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.MARKET.value]

    def execute(self):
        if self.is_filled:
            self.log_text = "이번 라운드에 이미 수행된 행동입니다."
            return False
        self.player_resource.set_food(
            self.player_resource.food + self.game_status.basic_resource[BasicBehaviorType.MARKET.value])
        self.player_resource.set_stone(
            self.player_resource.stone + self.game_status.basic_resource[BasicBehaviorType.MARKET.value])
        self.player_resource.set_reed(
            self.player_resource.reed + self.game_status.basic_resource[BasicBehaviorType.MARKET.value])
        self.log_text = f"갈대, 흙, 음식 {self.game_status.basic_resource[BasicBehaviorType.MARKET.value]}개를 획득하였습니다."
        self.game_status.set_basic_resource(BasicBehaviorType.MARKET.value, 1)
        return True

    def log(self):
        return self.log_text
