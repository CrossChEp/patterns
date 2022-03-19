"""Module represents state pattern"""
import time


class TrafficLight:
    state: None

    def __init__(self, state):
        self.change_state(state)

    def change_state(self, state):
        self.state = state
        self.state.traffic_light = self

    def change_yellow(self):
        self.state.change_to_yellow()

    def change_green(self):
        self.state.change_to_green()

    def change_red(self):
        self.state.change_to_red()


class State:

    def __init__(self):
        self.traffic_light = None

    def set_traffic_light(self, traffic_light: TrafficLight):
        self.traffic_light = traffic_light

    def get_traffic_light(self):
        return self.traffic_light

    def change_to_yellow(self):
        raise NotImplementedError

    def change_to_red(self):
        raise NotImplementedError

    def change_to_green(self):
        raise NotImplementedError


class RedState(State):
    def change_to_yellow(self):
        print(f'switching to yellow')
        traffic_light = self.get_traffic_light()
        traffic_light.change_state(state=YellowState())


class YellowState(State):
    def change_to_green(self):
        print(f'switching to green')
        traffic_light = self.get_traffic_light()
        traffic_light.change_state(state=GreenState())


class GreenState(State):
    def change_to_red(self):
        print(f'switching to red')
        traffic_light = self.get_traffic_light()
        traffic_light.change_state(state=RedState())


def main():
    traffic_light = TrafficLight(RedState())
    while True:
        traffic_light.change_yellow()
        time.sleep(1)
        traffic_light.change_green()
        time.sleep(1)
        traffic_light.change_red()
        time.sleep(1)


if __name__ == '__main__':
    main()
