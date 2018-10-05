# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from auxer import *
from pulsemap import PulseMap

#See PseudoControl for information on the basic structure of the class
#Here in fact we are modifying a little this. The _undelined version of the
#interface methods do the real job: The key is it manages 2 diferent RAM with 1 set of widgets, so we can't soter the relevant information on them. There's a local copy (self.formVals) of the information which in a typical control would go in the form. The self.ram variable selects which of the 2 rams we are editing, and the updateForm copies the information of the selected ram in the real form. The self.formVals information is updated on every action of the user. getFromForm() gets the data from self.formVars instead of the real form, because we want to provide information from the 2 rams, and the form can only hold 1. The same for set2Dev()
#There are some auxiliar fucntions, with meaningful names. To edit a map, we need to show an extra Form (which can be accepted or rejected), the PulseMap form, which is managed in its own class(in its own file pulsemap.py) and from here with the auxiliar runMappingDialog.
class RamControl (PseudoControl):
	controlName = 'RamControl'

	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.ctList = ctrl.ramList
		self.ctEventNum = ctrl.ramEvent
		self.ctEnable = ctrl.ramEnable
		self.formVals = [ ({},False), ({},False) ]
		self.ram = 0

		
	def getFromDev(self):
		return self.eva.getOpsRam()
	def getFromForm(self):
		return [ self._getFromForm(0), self._getFromForm(1) ]
	def set2Dev(self, ram0, ram1):
		self.eva.setOpsRam(ram0, ram1)
	def set2Form(self, ram0, ram1):
		self._set2Form(0, ram0[0], ram0[1])
		self._set2Form(1, ram1[0], ram1[1])
		self.updateForm()


	def _getFromForm(self, ram):
		return self.formVals[ram]



	def _set2Form(self, ram, ramEvents, enable):
		self.formVals[ram] = (ramEvents, enable)

	#########################################
	# Actions
	def updateForm(self):
		self.clearListControl(self.ctList)
		ramEvents, enable = self.formVals[self.ram]
		for k, v in ramEvents.iteritems():
			self.ctList.insertItem(QListViewItem(self.ctList, self.mapName(k)))
		self.ctEnable.setChecked(enable)
	
	def getSelectedEvent(self):
		ctev = self.ctEventNum
		mapid = ctev.text().toUInt()
		if not mapid[1] or not mapid[0] in range(0, self.eva.TOTAL_EVENT_CODE + 1):
			ctev.selectAll()
			ctev.setFocus()
			return None
		return mapid[0]
	
	def modifyMapping(self, mapid=None):
		ctlist = self.ctList
		ctev = self.ctEventNum
		ramEvents = self.getRamEvents()

		if mapid==None: mapid = self.getSelectedEvent()
		if mapid==None: return

		newpulse = self.runMappingDialog(mapid)
		if not newpulse: return
		
		ramEvents[mapid] = newpulse
		i = ctlist.findItem(self.mapName(mapid),0)
		if not i: ctlist.insertItem(QListViewItem(ctlist, self.mapName(mapid)))
		
		ctev.selectAll()
		ctev.setFocus()

	def deleteMapping(self, mapid=None):
		ctlist = self.ctList
		if mapid==None: mapid = self.getSelectedEvent()
		if mapid==None: return
		ramEvents = self.getRamEvents()
		if ramEvents.has_key(mapid):
			del(ramEvents[mapid])
			i = ctlist.findItem(self.mapName(mapid),0)
			if i: ctlist.takeItem(i)
			
	def clearMappings(self):
		ramEvents = self.getRamEvents()
		ramEvents.clear()
		self.clearListControl(self.ctList)
		
	def changeSelected(self, item):
		if item:
			tx = item.text(0).toUInt()[0]
			self.ctEventNum.setText(str(tx))
		
	def changeRam(self, ram):
		if ram in range(0,2):
			self.ram = ram
			self.updateForm()
			
	def changeEnable(self, ena):
		v = self.formVals[self.ram]
		self.formVals[self.ram] = (v[0], ena)
		


	##########################
	# AUXILIAR
	def newPulseMap(self, trig, set, clear, ledev):
		if (trig | set | clear | ledev) == 0:
			return None
		r = {}
		r['trigger'] = trig
		r['set'] = set
		r['clear'] = clear
		r['ledEvent'] = ledev
		return r
	
	def runMappingDialog(self, mapid):
		ramEvents = self.getRamEvents()
		existed = False
		
		pm = PulseMap()
		if ramEvents.has_key(mapid):
			existed = True
			v = ramEvents[mapid]
			pm.loadValues(v['trigger'], v['set'], v['clear'], v['ledEvent'])
		pm.setCaption(str(mapid) + '  -  Pulse Map Editor')
		if not pm.exec_loop():
			return None
		r = apply(self.newPulseMap, pm.getValues() )
		if existed and not r:
			self.deleteMapping(mapid)
		return r
	
	def getRamEvents(self):
		return self.formVals[self.ram][0]


	def clearListControl(self, ctlist):
		i = ctlist.firstChild()
		while i:
			ia = i.nextSibling()
			ctlist.takeItem(i)
			i = ia

	def mapName(self, mapid):
		return "%03d" % mapid



