#!../venv/bin/pytest

import re
from collections.abc import Callable
from pathlib import Path

import pytest
import urwid

from dbc_editor.main import main


class AbstractMockLoop:

	size: 'tuple[int, int]'

	def __init__(self,
		widget: urwid.Widget,
		palette: object, *,
		input_filter: 'Callable[[list[str], list[int]], list[str]]|None' = None,
		unhandled_input: 'Callable[[str], bool]',
		handle_mouse: bool,
	) -> None:
		if input_filter is None:
			input_filter = lambda keys, raws: keys
		self.widget = widget
		self.palette = palette
		self.input_filter = input_filter
		self.unhandled_input = unhandled_input

	def run(self) -> None:
		raise NotImplementedError()

	def simulate_key_press(self, key: str) -> bool:
		'''
		The urwid documentation says "The unhandled_input function should return True if it handled the input." [description of MainLoop.unhandled_input]
		But the return value is not checked and none of the official examples returns something from unhandled_input.
		Therefore I am not returning anything from the unhandled_input function either, making the return value of this method mean:
		True if it has been handled by widget, None if it has been passed to unhandled_input.
		'''
		keys = self.input_filter([key], [-1])
		assert len(keys) == 1
		key = keys[0]
		k = self.widget.keypress(self.size, key)
		if k:
			return self.unhandled_input(key)
		return True

class Line:
	def __init__(self, pattern: bytes) -> None:
		self.reo = re.compile(pattern)
	def __eq__(self, other: object) -> bool:
		if isinstance(other, bytes):
			return bool(self.reo.match(other))
		return NotImplemented
	def __repr__(self) -> str:
		return '%s(%r)' % (type(self).__name__, self.reo.pattern)


def test_new_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
	fn = str(tmp_path / 'new.dbc')

	class MockLoop(AbstractMockLoop):

		size = (188, 5)

		expected_widget = [
"messages in new.dbc                                                                                                                                                                         ".encode(),
"                                                                                                                                                                                            ".encode(),
"                                                                                                                                                                                            ".encode(),
"                                                                                                                                                                                            ".encode(),
"up/down: select message, +: new message, -: delete message, enter: show signals, i: edit message, v: visualize message layout, q: quit, 1: sort by id, 2: sort by name, 0: sort by dbc      ".encode(),
		]

		def run(self) -> None:
			assert self.widget.render(self.size).text == self.expected_widget
			with pytest.raises(urwid.ExitMainLoop):
				assert self.simulate_key_press('q')

	monkeypatch.setattr(urwid, 'MainLoop', MockLoop)
	main([fn])
