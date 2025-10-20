from music21 import stream, note, chord, instrument, tempo, midi

# Create a Score
score = stream.Score()
score.append(tempo.MetronomeMark(number=80))  # Slow ballad tempo

# Define Instruments
piano_part = stream.Part()
piano_part.insert(0, instrument.Piano())

strings_part = stream.Part()
strings_part.insert(0, instrument.Violin())

# Chord progression (key of C major, romantic ballad style)
# I – V – vi – IV progression is common in pop ballads
chords_list = [
    chord.Chord(['C4','E4','G4']),     # I
    chord.Chord(['G3','B3','D4']),     # V
    chord.Chord(['A3','C4','E4']),     # vi
    chord.Chord(['F3','A3','C4'])      # IV
]

# Piano: chords every 2 beats
for i in range(30):  # 30 chords × 2 beats ≈ 60s at 80 BPM
    c = chord.Chord(chords_list[i % 4])
    c.quarterLength = 2
    piano_part.append(c)

# Strings: simple melodic counterpoint
melody_notes = ['E5','G5','F5','D5','C5','A4','B4','G4']
for i in range(60):  # 60 half-beat notes → ~60s
    n = note.Note(melody_notes[i % len(melody_notes)])
    n.quarterLength = 0.5
    strings_part.append(n)

# Add parts to score
score.insert(0, piano_part)
score.insert(0, strings_part)

# Export MIDI & MusicXML
score.write('midi', fp='westlife_style.mid')
score.write('musicxml', fp='westlife_style.xml')

print("✅ 60-second Westlife-style ballad generated!")
