def evaluate_pitch(pitch_values, expected_freqs, tolerance=25):
    results = []
    for i, pitch in enumerate(pitch_values[:len(expected_freqs)]):
        expected = expected_freqs[i]
        match = abs(pitch - expected) < tolerance
        results.append((pitch, expected, match))
    return results
