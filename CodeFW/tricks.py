from __future__ import annotations

import typing
import sys
import dataclasses
import json

from pathlib import Path


@dataclasses.dataclass()
class Text:
    text: typing.Dict[str, str]

    @staticmethod
    def from_json(file: Path):
        with file.open("r") as f:
            text: typing.Dict[str, str] = json.load(f)

        return Text(text)

    def __getitem__(self, item):
        return self.text[item]


@dataclasses.dataclass()
class State:
    pass


@dataclasses.dataclass()
class Printer:
   default_speed: float = 0.1

    def printf(self, string: str, pause: float=None):
        if pause is None:
            pause = self.default_speed

        for character in string:
            sleep(pause)
            sys.stdout.write(character)

    def print(self, string: str):
        print(string)




@dataclasses.dataclass()
class Scene:

    def run(self, state: State, printer: Printer):
        pass


@dataclasses.dataclass()
class WhatTrick(Scene):

    def run(self, state: State, text: Text, printer: Printer):
        text = text["what_trick"]

        prompt = text["prompt"]
        printer.printf(prompt)

        responses = text["response"]
        for response in responses.values():
            printer.printf(response)

        return None, state

@dataclasses.dataclass()
class Game:
    printer: Printer
    text: Text
    scene: Scene
    state: State

    def run(self):
        while True:
            self.scene, self.state = self.scene.run(self.state,
                                                    self.text,
                                                    printer=printer,
                                                    )


if __name__ == "__main__":
    text = Text.from_json(Path("text.json"))
    printer = Printer()
    initial_scene = WhatTrick()
    state = State()

    game = Game(printer,
                text,
                initial_scene,
                state,
                )
    game.run()

