from audio_utils import record_audio
from pitch_detection import get_pitches
from practice_sessions.sargam_practice import SARGAM_NOTES
from feedback_engine import evaluate_pitch

if __name__ == "__main__":
    record_audio(duration=10)
    pitch_values = get_pitches("output.wav")
    expected_freqs = list(SARGAM_NOTES.values())[:len(pitch_values)]
    feedback = evaluate_pitch(pitch_values, expected_freqs)

    for i, (pitch, expected, match) in enumerate(feedback):
        print(f"Note {i+1}: You sang {round(pitch, 2)} Hz, expected {expected} Hz - {'OK' if match else 'Try again'}")
