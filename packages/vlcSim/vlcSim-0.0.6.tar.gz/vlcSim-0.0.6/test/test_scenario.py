from vlcsim.scenario import *
import pytest


class TestScenario:
    @pytest.fixture(autouse=True)
    def reset(self):
        VLed.numberOfVLeds = 0
        Receiver.receiversCreated = 0

    def testConstructor(self):
        scenario = Scenario(5.0, 5.0, 2.15, 10, 0.8)

    def testPowerLOS(self):
        scenario = Scenario(5.0, 5.0, 2.15, 10, 0.8)
        vled = VLed(-1.25, -1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(-1.25, 1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(1.25, -1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(1.25, 1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        receiver = Receiver(-1.989796, -1.989796, 0, 1e-4, 1.0, 1.5, 70.0)

        powerLOS1 = float(scenario.getPowerInPointFromVled(receiver, 0))
        powerLOS2 = float(scenario.getPowerInPointFromVled(receiver, 1))
        powerLOS3 = float(scenario.getPowerInPointFromVled(receiver, 2))
        powerLOS4 = float(scenario.getPowerInPointFromVled(receiver, 3))

        assert powerLOS1 == pytest.approx(0.705779328309489)
        assert powerLOS2 == pytest.approx(0.112350368632482)
        assert powerLOS3 == pytest.approx(0.112350368632482)
        assert powerLOS4 == pytest.approx(0.0458451902869800)

    def testPowerNLOS(self):
        scenario = Scenario(5.0, 5.0, 2.15, 10, 0.8)
        vled = VLed(-1.25, -1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(-1.25, 1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(1.25, -1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(1.25, 1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        receiver = Receiver(-1.989796, -1.989796, 0, 1e-4, 1.0, 1.5, 70.0)

        powerNLOS1 = scenario.getPowerInPointFromWalls(receiver, 0)
        powerNLOS2 = scenario.getPowerInPointFromWalls(receiver, 1)
        powerNLOS3 = scenario.getPowerInPointFromWalls(receiver, 2)
        powerNLOS4 = scenario.getPowerInPointFromWalls(receiver, 3)

        assert powerNLOS1 == pytest.approx(0.239498135405109)
        assert powerNLOS2 == pytest.approx(0.0461886869184859)
        assert powerNLOS3 == pytest.approx(0.0461886869184859)
        assert powerNLOS4 == pytest.approx(0.0253974114981625)

    def testSNR(self):
        scenario = Scenario(5.0, 5.0, 2.15, 10, 0.8)
        vled = VLed(-1.25, -1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(-1.25, 1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(1.25, -1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        vled = VLed(1.25, 1.25, 2.15, 60, 60, 20, 70)
        scenario.addVLed(vled)
        receiver = Receiver(-1.989796, -1.989796, 0, 1e-4, 1.0, 1.5, 70.0)

        powerLOS1 = scenario.getPowerInPointFromVled(receiver, 0)
        powerLOS2 = scenario.getPowerInPointFromVled(receiver, 1)
        powerLOS3 = scenario.getPowerInPointFromVled(receiver, 2)
        powerLOS4 = scenario.getPowerInPointFromVled(receiver, 3)

        powerNLOS1 = scenario.getPowerInPointFromWalls(receiver, 0)
        powerNLOS2 = scenario.getPowerInPointFromWalls(receiver, 1)
        powerNLOS3 = scenario.getPowerInPointFromWalls(receiver, 2)
        powerNLOS4 = scenario.getPowerInPointFromWalls(receiver, 3)

        totalPower = (
            powerLOS1
            + powerLOS2
            + powerLOS3
            + powerLOS4
            + powerNLOS1
            + powerNLOS2
            + powerNLOS3
            + powerNLOS4
        )

        assert totalPower == pytest.approx(1.33359817660168)

        snr = receiver.snr(totalPower)

        assert snr == pytest.approx(1.465658126604280e08)
