# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
import pytest
from src.dispense import DispenseEvent

# Rejecting negative or zero doses
def test_invalid_dose():
    with pytest.raises(ValueError):
        DispenseEvent("P1", "Aspirin", 0, 1)


# Preventing duplicate dispensing events
def test_duplicate_dispensing():
    e1 = DispenseEvent("P1", "Aspirin", 100, 1)
    e2 = DispenseEvent("P1", "Aspirin", 200, 1)

    assert DispenseEvent.invariant_holds([e1], e2) is False


# Enforcing maximum dosage limits
def test_exceeds_maximum_dose():
    with pytest.raises(ValueError):
        DispenseEvent("P1", "Aspirin", 5000, 1)
