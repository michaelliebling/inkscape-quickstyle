#!/usr/bin/env python
# coding=utf-8
import inkex
import uuid
from inkex.elements import TextElement
from inkex import Group, Marker, PathElement

class QuickStyle(inkex.Effect):
    def add_marker(self, name, rotate, scale): # from the dimensions.py extnesion with added scale argument
        """Create a marker in the defs of the svg"""
        marker = Marker()
        marker.set('id', name)
        marker.set('orient', 'auto')
        marker.set('refX', '0.0')
        marker.set('refY', '0.0')
        marker.set('style', 'overflow:visible')
        marker.set('inkscape:stockid', name)
        self.svg.defs.append(marker)

        arrow = PathElement(d='M 0.0,0.0 L 5.0,-5.0 L -12.5,0.0 L 5.0,5.0 L 0.0,0.0 z ')
        if rotate:
            arrow.set('transform', 'scale('+str(scale)+') rotate(180) translate('+str(scale*16.0)+',0)')
        else:
            arrow.set('transform', 'scale('+str(scale)+') translate('+str(scale*16.0)+',0)')
        arrow.set('style', 'fill-rule:evenodd;stroke:#000000;stroke-width:1.0pt;marker-start:none')
        marker.append(arrow)

    def add_arguments(self, pars):
        pars.add_argument("--stylecode", type=str, default="s", help="Style code")
 
    def __init__(self):
        inkex.Effect.__init__(self)

    def effect(self):
        stylecode =  self.options.stylecode
        stroke_color = "stroke:#000000;stroke-opacity:1";
        stroke_width = "stroke-width:1.0pt" # default
        stroke_dasharray = "stroke-dasharray:none" # default  
        stroke_dashoffset = "stroke-dashoffset:0" # default
        fill_color = "fill:none;fill-opacity:1" # default
        arrow_url = "" # default
        str_base_width = 0.35
        str_fact = 1.0
        if "s" in stylecode.lower(): # thin
            str_fact = 1.0
        if "g" in stylecode.lower(): # thick 
            str_fact = 2.0
        if "h" in stylecode.lower(): # thickest
            str_fact = 3.0
        if "d" in stylecode.lower(): # dotted
            stroke_dasharray = "stroke-dasharray:2,1"  
        if "e" in stylecode.lower(): # dashed
            stroke_dasharray = "stroke-dasharray:4,1.5"  
        if "f" in stylecode.lower(): # gray fill
            fill_color =  "fill:#c8c8c8;fill-opacity:1"
        if "w" in stylecode.lower(): # white fill 
            fill_color =  "fill:#ffffff;fill-opacity:1"
        if "b" in stylecode.lower(): # black
            fill_color =  "fill:#000000;fill-opacity:1"
        if "a" in stylecode.lower():
            id =stylecode.lower() #uuid.uuid4() 
            self.add_marker('Arrow1Lend_'+str(id), True,0.8/str_fact)
            arrow_url=";marker-end:url(#Arrow1Lend_"+str(id)+")"
        if "x" in stylecode.lower():
            id = stylecode.lower() #uuid.uuid4() 
            self.add_marker('Arrow1Lstart_'+str(id), False,0.8/str_fact)
            self.add_marker('Arrow1Lend_'+str(id), True,0.8/str_fact)
            arrow_url=";marker-end:url(#Arrow1Lend_"+str(id)+");marker-start:url(#Arrow1Lstart_"+str(id)+")"
        
        stroke_width = "stroke-width:"+str(str_fact*str_base_width)  

        elements = self.svg.selected.values()
        for el in elements:
            currentAtt = el.attrib.get("style")
            el.attrib["style"]=stroke_color+";"+stroke_width+";"+fill_color+";"+stroke_dasharray+";"+stroke_dashoffset+arrow_url

if __name__ == '__main__':
     QuickStyle().run()
