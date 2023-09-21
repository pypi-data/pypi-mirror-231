from __future__ import annotations
from typing import List, Optional, Type


import enum, sys, pygame as pg

from pygame.locals import *
from abc import ABC, abstractmethod


pg.init()


class Suit(enum.Enum):
    Diamond = enum.auto()
    Club = enum.auto()
    Heart = enum.auto()
    Spade = enum.auto()


class Card:
    def __init__(self, value: Optional[int], suit: Suit) -> None:
        self.texture = ""
        self.value = value
        self.suit = suit
        # check if value is none then decide
        self.is_ace: bool = False


class Hand:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def calculate_value(self) -> int:
        return 0


class Player:
    def __init__(self) -> None:
        self.hand = Hand()


class Dealer(Player):
    pass


class State(ABC):
    def __init__(self, ctx: App) -> None:
        self.ctx = ctx
        self.pend_state = Optional[Type[State]]

    @abstractmethod
    def update(self) -> None:
        """"""

    @abstractmethod
    def render(self) -> None:
        """"""

    @abstractmethod
    def pend(self) -> None:
        """"""


class App:
    def __init__(self, state: Type[State]) -> None:
        self.state = state(self)
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
        pg.display.set_caption("Blackjack")

        self.lucky = 21

    def update(self) -> None:
        self.state.update()

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

    def render(self) -> None:
        self.state.render()

    def run(self) -> None:
        card = pg.image.load("card_png/ace_of_hearts.png")

        while 1:
            self.update()
            self.render()

            self.clock.tick(60)

            self.display.fill((35, 103, 78))
            self.display.blit(card, (0, 0))

            pg.display.update()
