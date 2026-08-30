SHARP_NOTES = ["G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]
FLAT_NOTES = ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]

FLATS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]


class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        self.tonic_sanitized = tonic.replace(tonic[0], tonic[0].upper(), 1)

    def chromatic(self):

        notes = []
        if self.tonic in FLATS:
            notes = FLAT_NOTES.copy()
        else:
            notes = SHARP_NOTES.copy()

        start_index = notes.index(self.tonic_sanitized)

        result = []
        for _ in range(12):
            result.append(notes[start_index])
            start_index = (start_index + 1) % 12

        return result

    def interval(self, intervals):
        notes = self.chromatic()

        start_index = notes.index(self.tonic_sanitized)

        result = []
        result.append(self.tonic_sanitized)
        for interval in intervals:

            if interval == "m":
                start_index = (start_index + 1) % 12
            elif interval == "M":
                start_index = (start_index + 2) % 12
            elif interval == "A":
                start_index = (start_index + 3) % 12

            result.append(notes[start_index])

        return result
