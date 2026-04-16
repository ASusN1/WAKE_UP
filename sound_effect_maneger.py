import ctypes
import os


SOUND_DIR = os.path.join(os.path.dirname(__file__), "sound_effect")
_alias_index = 0


def _play_sound(file_name):
	global _alias_index

	sound_path = os.path.join(SOUND_DIR, file_name)
	if not os.path.exists(sound_path):
		return

	_alias_index += 1
	alias = f"sfx_{_alias_index}"

	try:
		ctypes.windll.winmm.mciSendStringW(f'open "{sound_path}" type mpegvideo alias {alias}', None, 0, None)
		ctypes.windll.winmm.mciSendStringW(f"play {alias} from 0", None, 0, None)
	except Exception:
		pass


def play_open_note():
	_play_sound("open_note.mp3")


def play_close_note():
	_play_sound("close_note.mp3")


def play_highlighter():
	_play_sound("highlighter.mp3")


def play_deleting_note_sound():
	_play_sound("deleting_note_sound.mp3")

def play_save_note_sound():
    _play_sound("save_sound_effect.mp3")