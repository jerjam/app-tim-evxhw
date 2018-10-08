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


from ReceiverModel import *
import xml.dom.minidom
from xml.dom.minidom import Node
from xml.dom.minidom import Document

import traceback

class MXMLIO:
	
	def _run_selection(self, selection, ops, parA, parB=None):
		self._error = []
		self._ok = []
		self._errorDesc = []
		result = []
		for name, fn in ops:
			try:
				if name in selection:
					if parB:
						result += [fn (parA, parB)]
					else:
						result += [fn (parA)]
			except:
				self._error += [ name ]
				self._errorDesc += [traceback.format_exc()]
			else:
				self._ok += [ name ]
		return result
	
	def load_from_file(self, fname, model, selection):
		doc = xml.dom.minidom.parse(str(fname))
		return self.load_from_xml(doc, model, selection)

	def save_to_file(self, fname):
		#doc = self.pre_save_to_xml(model, selection)
		doc = self.doc
		f = open(str(fname), 'w')
		f.write(doc.toprettyxml(indent="  "))
		f.close()

	def load_from_xml(self, doc, model, selection, parent=None):
		self.doc = doc

		if parent is None:
			parent = self.doc.getElementsByTagName('timing')[0].getElementsByTagName('evr')[0]

		ops = [
			[ 'PULSE',		self.load_pulses_from_xml ],
			[ 'RAM',		self.load_ram_from_xml ],
			[ 'UNIVOUT',		self.load_outputs_from_xml ],
			[ 'UNIVIN',		self.load_inputs_from_xml ],
			[ 'COUNTER',	self.load_counters_from_xml ],
		]
		self._run_selection(selection, ops, parent, model)

	def pre_save_to_xml(self, model, selection, doc=None, parent=None):
		if doc is None:
			self.doc = Document()
			timing = self.doc.createElement("timing")
			self.doc.appendChild(timing)
			evr = self.doc.createElement("evr")
			timing.appendChild(evr)
			parent = evr
		else:
			self.doc = doc

		ops = [
			[ 'PULSE',		self.save_pulses_to_xml ],
			[ 'RAM',		self.save_ram_to_xml ],
			[ 'UNIVOUT',		self.save_outputs_to_xml ],
			[ 'UNIVIN',		self.save_inputs_to_xml ],
			[ 'COUNTER',	self.save_counters_to_xml ],
		]
		toAdd = self._run_selection(selection, ops, model)

		# Ok, so all the xml has been generated allright, then we do save it
		for x in toAdd:
			parent.appendChild(x)

		return self.doc



	def _load_event_flags_from_xml(self, parent, mevent, attrName, tr=int):
		attr = getattr(mevent, attrName)
		for x in xrange(len(attr)):
			attr[x] = False
		for node in parent.getElementsByTagName(attrName):
			nid = node.getAttribute('id')
			nid = tr(nid)
			if not nid is None:
				attr[nid] = True

	def _flag2num(self, flag):
		#names = [x for x in dir(MEvent) if x[:4] == 'Flag']
		if hasattr(MEvent, flag):
			return getattr(MEvent, flag)
		return None

	def _num2flag(self, flag):
		names = [x for x in dir(MEvent) if x[:4] == 'Flag']
		for name in names:
			if getattr(MEvent, name) == flag:
				return name
		print '_num2flag error'
		return None

	def load_ram_from_xml(self, parent, model):
		ramNode = parent.getElementsByTagName('ram')
		if ramNode == []:
			raise "This XML does not include RAM info"
		ramNode = ramNode[0]

		n = 0
		for node in ramNode.getElementsByTagName('event'):
			evid = node.getAttribute('id')
			evid = int(evid)

			p = model.mram.events[evid]

			self._load_event_flags_from_xml(node, p, 'trigger', int)
			self._load_event_flags_from_xml(node, p, 'set', int)
			self._load_event_flags_from_xml(node, p, 'clear', int)
			self._load_event_flags_from_xml(node, p, 'flags', self._flag2num)


	def _save_event_flags_to_xml(self, parent, mevent, attrName, tr=int):
		attr = getattr(mevent, attrName)

		for x in xrange(len(attr)):
			if attr[x]:
				node = self.doc.createElement(attrName)
				node.setAttribute('id', str(tr(x)))
				parent.appendChild(node)
	
	def save_ram_to_xml(self, model):
		ram = self.doc.createElement("ram")

		for n in xrange(len(model.mram.events)):
			p = model.mram.events[n]
			node = self.doc.createElement("event")
			ram.appendChild(node)

			node.setAttribute("id", str(n))

			self._save_event_flags_to_xml(node, p, 'trigger', int)
			self._save_event_flags_to_xml(node, p, 'set', int)
			self._save_event_flags_to_xml(node, p, 'clear', int)
			self._save_event_flags_to_xml(node, p, 'flags', self._num2flag)
		return ram
		

	def load_pulses_from_xml(self, parent, model):
		pulsesNode = parent.getElementsByTagName('pulses')
		if pulsesNode == []:
			raise "This XML does not include PULSE info"
		pulsesNode = pulsesNode[0]

		n = 0
		for node in pulsesNode.getElementsByTagName('pulse'):
			name = node.getAttribute('name')

			model.mpulses.pulseNames[n] = str(name)
			p = model.mpulses.pulses[n]

			p.delay = int(node.getAttribute("delay"))
			p.width = int(node.getAttribute("width"))
			if n < MPulseList.TotalPrescalers:
				pr = node.getAttribute("prescaler")
				try:
					p.prescaler = int(pr)
				except:
					p.prescaler = 1

			pol = str(node.getAttribute("polarity"))
			if pol == 'ActiveHigh':
				p.polarityActiveHigh = True
			else:
				p.polarityActiveHigh = False

			ten = node.getElementsByTagName("trigger-enables")
			if len(ten) == 1:
				p.tmaster = str(ten[0].getAttribute("masteren")) == 'True'
				p.tpulse  = str(ten[0].getAttribute("pulseen")) == 'True'
				p.tset    = str(ten[0].getAttribute("seten")) == 'True'
				p.tclear  = str(ten[0].getAttribute("clearen")) == 'True'

			n += 1


	def save_pulses_to_xml(self, model):
		pulses = self.doc.createElement("pulses")

		for n in xrange(len(model.mpulses.pulses)):
			p = model.mpulses.pulses[n]
			node = self.doc.createElement("pulse")
			pulses.appendChild(node)

			node.setAttribute("name", model.mpulses.pulseNames[n])
			
			node.setAttribute("delay", str(p.delay))
			node.setAttribute("width", str(p.width))
			if n < MPulseList.TotalPrescalers:
				node.setAttribute("prescaler", str(p.prescaler))
			pol = 'ActiveLow'
			if p.polarityActiveHigh:
				pol = 'ActiveHigh'
			node.setAttribute("polarity", pol)

			ten = self.doc.createElement("trigger-enables")
			node.appendChild(ten)
			ten.setAttribute("masteren", str(p.tmaster))
			ten.setAttribute("pulseen", str(p.tpulse))
			ten.setAttribute("seten", str(p.tset))
			ten.setAttribute("clearen", str(p.tclear))
		return pulses

	def save_outputs_to_xml(self, model):
		outsNode = self.doc.createElement("outputs")

		for n in xrange(len(model.moutputs)):
			node = self.doc.createElement("output")
			outsNode.appendChild(node)

			node.setAttribute("id", str(n))
			# @todo string, no num:
			node.setAttribute("value", str(model.moutputs[n].output))

		return outsNode
			
	def load_outputs_from_xml(self, parent, model):
		outsNode = parent.getElementsByTagName('outputs')

		if outsNode == []:
			raise "This XML does not include OUTPUTS info"
		outsNode = outsNode[0]

		n = 0
		for node in outsNode.getElementsByTagName('output'):
			outid = node.getAttribute('id')
			outid = int(outid)

			outval = node.getAttribute('value')
			outval = int(outval) # @todo string, no num

			model.moutputs[outid].output = outval



# todo outputs no va del tot be encara, deixa un dom object somewhere...


	def save_inputs_to_xml(self, model):
		insNode = self.doc.createElement("inputs")

		for n in xrange(len(model.minputs)):
			node = self.doc.createElement("input")
			insNode.appendChild(node)

			node.setAttribute("id", str(n))
			node.setAttribute("backEvent", str(model.minputs[n].backEvent))
			node.setAttribute("backEdge", str(int(model.minputs[n].backEdge)))
			node.setAttribute("backLevel", str(int(model.minputs[n].backLevel)))
			node.setAttribute("extEvent", str(model.minputs[n].extEvent))
			node.setAttribute("extEdge", str(int(model.minputs[n].extEdge)))
			node.setAttribute("extLevel", str(int(model.minputs[n].extLevel)))
			node.setAttribute("extEdgeSensitivity", str(int(model.minputs[n].extEdgeSensitivity)))
			node.setAttribute("extLevelSensitivity", str(int(model.minputs[n].extLevelSensitivity)))

		return insNode
			
	def load_inputs_from_xml(self, parent, model):
		insNode = parent.getElementsByTagName('inputs')
		if insNode == []:
			raise "This XML does not include INPUTS info"
		insNode = insNode[0]

		n = 0
		for node in insNode.getElementsByTagName('input'):
			inid = node.getAttribute('id')
			inid = int(inid)

			backEvent = node.getAttribute('backEvent')
			extEvent = node.getAttribute('extEvent')

			if backEvent is None: backEvent = node.getAttribute('back')
			if extEvent is None: extEvent = node.getAttribute('extEvent')

			if (str(backEvent) == 'None'):
				backEvent = None
			else:
				backEvent = int(backEvent)

			if (str(extEvent) == 'None'):
				extEvent = None
			else:
				extEvent = int(extEvent)

			
			model.minputs[inid].backEvent = backEvent
			model.minputs[inid].backEdge = int(node.getAttribute('backEdge'))
			model.minputs[inid].backLevel = int(node.getAttribute('backLevel'))
			model.minputs[inid].backEdge = int(node.getAttribute('backEdge'))
			model.minputs[inid].backLevel = int(node.getAttribute('backLevel'))
			model.minputs[inid].extEvent = extEvent
			model.minputs[inid].extEdge = int(node.getAttribute('extEdge'))
			model.minputs[inid].extLevel = int(node.getAttribute('extLevel'))
			model.minputs[inid].extEdgeSensitivity = int(node.getAttribute('extEdgeSensitivity'))
			model.minputs[inid].extLevelSensitivity = int(node.getAttribute('extLevelSensitivity'))

	def save_counters_to_xml(self, model):
		insNode = self.doc.createElement("counters")

		for n in xrange(len(model.mcounters)):
			node = self.doc.createElement("counter")
			insNode.appendChild(node)

			node.setAttribute("id", str(n))
			node.setAttribute("value", str(model.mcounters[n]))

		return insNode
			
	def load_counters_from_xml(self, parent, model):
		outsNode = parent.getElementsByTagName('counters')
		if outsNode is []:
			raise "This XML does not include COUNTERS info"
		outsNode = outsNode[0]

		n = 0
		for node in outsNode.getElementsByTagName('counter'):
			inid = node.getAttribute('id')
			inid = int(inid)

			val = node.getAttribute('value')

			model.mcounters[inid] = int(val)


