from music21 import stream, note, meter, key

# 创建主乐谱和声部
score = stream.Score()
part = stream.Part()

# 设置调号和拍号 (原调1=F, 2/4拍) [citation:1]
part.append(key.Key('F'))
part.append(meter.TimeSignature('2/4'))

# 定义《兰花草》第一句的旋律
# 我从山中来，带着兰花草
melody_notes = [
    ('G4', 'quarter'), ('G4', 'eighth'), ('G4', 'eighth'), ('F4', 'quarter'),
    ('E4', 'eighth'), ('F4', 'eighth'), ('D4', 'half'),
    ('D4', 'quarter'), ('D4', 'eighth'), ('D4', 'eighth'), ('D4', 'quarter'),
    ('C4', 'eighth'), ('E4', 'eighth'), ('E4', 'quarter'), ('G4', 'eighth'), ('G4', 'quarter'),
    ('G4', 'quarter'), ('F4', 'eighth'), ('E4', 'eighth'), ('F4', 'eighth'), ('D4', 'eighth'), ('G4', 'quarter'),
    ('G4', 'quarter'), ('G4', 'eighth'), ('F4', 'eighth'), ('E4', 'eighth'), ('C4', 'eighth'), ('D4', 'quarter'), ('C4', 'eighth'), ('D4', 'quarter')
]

# 将音符添加到声部中
for pitch, duration in melody_notes:
    n = note.Note(pitch)
    n.duration.type = duration
    part.append(n)

# 将声部添加到乐谱中
score.insert(0, part)
score.write('midi', fp='orchid_grass.mid')
score.write('musicxml', fp='orchid_grass.xml')
# 显示乐谱 (乐谱会显示在右侧，或弹出新窗口)
score.show()