from music21 import stream, note, chord, instrument, tempo, midi
import random

# 30-second tempo (120 BPM)
score = stream.Score()
score.append(tempo.MetronomeMark(number=120))

# Instruments
piano = stream.Part()
piano.insert(0, instrument.Piano())

flute = stream.Part()
flute.insert(0, instrument.Flute())

# Piano: random chords
chords_list = [
    ['C4','E4','G4'],
    ['F4','A4','C5'],
    ['G3','B3','D4'],
    ['A3','C4','E4']
]

for _ in range(15):  # 15 chords × 2 beats ≈ 30s
    c = chord.Chord(random.choice(chords_list))
    c.quarterLength = 2
    piano.append(c)

# Flute: random melody
melody_notes = ['C5','D5','E5','F5','G5','A5','B5']
for _ in range(60):  # 60 half-beat notes
    n = note.Note(random.choice(melody_notes))
    n.quarterLength = 0.5
    flute.append(n)

# Add parts to score
score.insert(0, piano)
score.insert(0, flute)

# Export files
score.write('midi', fp='composition.mid')
score.write('musicxml', fp='composition.xml')

print("✅ Files created: composition.mid + composition.xml")