from pytest import fixture
from random import seed, choice, choices, randint

from faulty_sensor import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_first_example(s: Solution):
    assert s.badSensor([2, 3, 4, 5], [2, 1, 3, 4]) == 1, "faulty 1"


def test_second_example(s: Solution):
    assert s.badSensor([2, 2, 2, 2, 2], [2, 2, 2, 2, 5]) == -1, "indeterminate"


def test_third_example(s: Solution):
    assert s.badSensor([2, 3, 2, 2, 3, 2], [2, 3, 2, 3, 2, 7]) == 2, "faulty 2"


def test_little_data(s: Solution):
    assert s.badSensor([1], [1]) == -1, "no error"
    assert s.badSensor([1], [2]) == -1, "indeterminate"
    assert s.badSensor([1, 2], [1, 2]) == -1, "no error"
    assert s.badSensor([1, 2], [1, 5]) == -1, "indeterminate"
    assert s.badSensor([1, 2, 3], [1, 2, 3]) == -1, "no error"
    assert s.badSensor([1, 2, 3], [1, 2, 2]) == -1, "indeterminate"
    assert s.badSensor([1, 3, 4], [1, 2, 3]) == 1, "faulty 1"
    assert s.badSensor([1, 2, 3], [1, 3, 4]) == 2, "faulty 2"


def test_large_data(s: Solution):
    N = int(1e2)  # largest number of data
    seed(1234567890)  # seed for determinism
    sensor_data = choices([i + 1 for i in range(N)], k=N)
    # test faulty sensor1
    i = randint(0, N - 1)  # random index of sensor_data
    sensor1 = (
        sensor_data[:i] + sensor_data[i + 1 :] + [choice([i + 1 for i in range(N)])]
    )
    sensor2 = sensor_data
    assert s.badSensor(sensor1, sensor2) == 1, "faulty 1"
    # test faulty sensor2
    i = randint(0, N - 1)  # random index of sensor_data
    sensor1 = sensor_data
    sensor2 = (
        sensor_data[:i] + sensor_data[i + 1 :] + [choice([i + 1 for i in range(N)])]
    )
    assert s.badSensor(sensor1, sensor2) == 2, "faulty 2"


def test_unlucky_data(s: Solution):
    sensor1 = [1, 2, 3, 2, 3, 2]
    sensor2 = [1, 2, 3, 3, 2, 3]
    assert s.badSensor(sensor1, sensor2) == -1, "indeterminate"
    sensor1 = [1, 2, 3, 3, 2, 3]
    sensor2 = [1, 2, 3, 2, 3, 2]
    assert s.badSensor(sensor1, sensor2) == -1, "indeterminate"
