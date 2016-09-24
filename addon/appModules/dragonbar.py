from appModuleHandler import AppModule
import api
import controlTypes
import tones
import ui
import windowUtils
from NVDAObjects.UIA import UIA
import NVDAObjects
import speech
import winUser
import time

class AppModule(AppModule):
	lastFlashRightText = None

	def flashRightTextChanged(self, obj):
		text = obj.name
		if not text:
			return
		if self.lastFlashRightText == text:
			return
		self.lastFlashRightText = text
		mOff="Dragon\'s microphone is off;"
		mOn="Normal mode: You can dictate and use voice"
		mSleep="The microphone is asleep;"
		if mOn in text:
			speech.speakText("Dragon mic on")
		elif mOff in text:
			speech.speakText("Dragon mic off")
		elif mSleep in text:
			speech.speakText("Dragon sleeping")

	def event_nameChange(self, obj, nextHandler):
		try:
			automationId = obj.UIAElement.currentAutomationID
		except:
			automationId = None
		if automationId == "txtFlashRight":
			self.flashRightTextChanged(obj)
		nextHandler()
