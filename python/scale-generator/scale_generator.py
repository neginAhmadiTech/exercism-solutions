SHARP_NOTES = ["G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]
FLAT_NOTES = ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]

TONICS_USING_FLATS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]
INTERVAL_STEPS = {
    "m": 1,
    "M": 2,
    "A": 3,
}


class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        self.tonic_sanitized = tonic.capitalize()

    def chromatic(self):

        notes = []
        if self.tonic in TONICS_USING_FLATS:
            notes = FLAT_NOTES
        else:
            notes = SHARP_NOTES

        start_index = notes.index(self.tonic_sanitized)

        result = []
        for _ in range(12):
            result.append(notes[start_index])
            start_index = (start_index + 1) % 12

        return result

    def interval(self, intervals):

        notes = self.chromatic()
        current_index = 0

        result = [notes[current_index]]
        for interval in intervals:
            current_index = (current_index + INTERVAL_STEPS[interval]) % 12
            result.append(notes[current_index])

        return result
