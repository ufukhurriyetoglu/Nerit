#!/usr/bin/env python
# -*- coding: UTF-8 -*
import ConfigParser
from Menu import Menu
from LinuxPrinter import LinuxPrinter

class Nerit(Menu):

	""" Clase cliente ejecutable para Linux"""
	

	def __init__(self,config_file='../config/nerit.ini'):
		super(Nerit,self).__init__(config_file)

	def getConfig(self):
		
		config = ConfigParser.RawConfigParser()
		config.optionxform = str 
		self.final_stage=LinuxPrinter()
		config.read(self.config_file)
		return config

menu=Nerit()
config=menu.getConfig()
menu.show_menu(config)
