import editor
from sound import MIDIPlayer

midi_player = MIDIPlayer(editor.get_path())
midi_player.play()
