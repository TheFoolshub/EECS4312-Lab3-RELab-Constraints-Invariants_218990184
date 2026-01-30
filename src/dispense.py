class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.
    """

    MAX_DAILY_DOSE = {
        "Aspirin": 4000,
        "Ibuprofen": 3200,
    }

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.
        """

        if patient_id is None or str(patient_id).strip() == "":
            raise ValueError("patient_id must be provided")

        if medication is None or str(medication).strip() == "":
            raise ValueError("medication identifier must be provided")

        if dose_mg <= 0:
            raise ValueError("Dose must be positive")

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity

    # TODO Task 4: Define and check system invariants
    @staticmethod
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
        """
        for e in existing_events:
            if e.patient_id == new_event.patient_id and e.medication == new_event.medication:
                return False
        return True
