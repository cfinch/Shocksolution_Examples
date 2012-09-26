#!/usr/bin/python
import xml.etree.ElementTree as etree
from xml.dom import minidom

output_file = "test.wgt"    # file extension for wxGlade template file

# Attribute definitions
wxStaticText_attributes = {"class":"wxStaticText", "name":"label_1", 
    "base":"EditStaticText"}
wxCheckBox_attributes = {"class":"wxCheckBox", "name":"checkbox_1", 
    "base":"EditCheckBox"}

# Boilerplate for wxGlade templates
root = etree.Element("application", attrib={"path":"/home/cfinch/Projects/wx/wx/test",
    "name":"", "class":"", "option":"0", "language":"C++", "top_window":"grid_sizer_1",
    "encoding":"UTF-8", "use_gettext":"0", "overwrite":"0", "use_new_namespace":"1",
    "for_version":"2.8", "is_template":"1"})

templatedata = etree.SubElement(root, "templatedata")
author = etree.SubElement(templatedata, "author")
author.text = "Craig Finch"
description = etree.SubElement(templatedata, "description")
description.text = "testing"
instructions = etree.SubElement(templatedata, "instructions")
instructions.text = "testing"

# Dialog
dialog = etree.SubElement(root, "object", attrib={"class":"MyDialog", "name":"dialog",
    "base":"EditDialog"})
dialog_style = etree.SubElement(dialog, "style")
dialog_style.text = "wxDEFAULT_DIALOG_STYLE"
dialog_title = etree.SubElement(dialog, "title")
dialog_title.text = "Dialog"
dialog_size = etree.SubElement(dialog, "size")
dialog_size.text = "200, 200d"

# Add wxGridSizer to Dialog
sizer = etree.SubElement(dialog, "object", attrib={"class":"wxGridSizer", "name":"grid_sizer_1",
    "base":"EditGridSizer"})
hgap = etree.SubElement(sizer, "hgap")
hgap.text = "0"
rows = etree.SubElement(sizer, "rows")
rows.text = "6"
cols = etree.SubElement(sizer, "cols")
cols.text = "2"
vgap = etree.SubElement(sizer, "vgap")
vgap.text = "0"

# Add static text to sizer
sizeritem = etree.SubElement(sizer, "object", attrib={"class":"sizeritem"})
border = etree.SubElement(sizeritem, "border")
border.text = "0"
option = etree.SubElement(sizeritem, "option")
option.text = "0"

control = etree.SubElement(sizeritem, "object", attrib=wxStaticText_attributes)
att = etree.SubElement(control, "attribute")
att.text = "1"
label = etree.SubElement(control, "label")
label.text = "Label Text"

# Add check box control to sizer
sizeritem = etree.SubElement(sizer, "object", attrib={"class":"sizeritem"})

border = etree.SubElement(sizeritem, "border")
border.text = "0"
option = etree.SubElement(sizeritem, "option")
option.text = "0"

control = etree.SubElement(sizeritem, "object", attrib=wxCheckBox_attributes)
att = etree.SubElement(control, "attribute")
att.text = "1"
label = etree.SubElement(control, "label")
label.text = "Control Text"

# Pretty-print
reparsed = minidom.parseString(etree.tostring(root))
print(reparsed.toprettyxml())

# Save to file
f = open(output_file, 'w')
f.write(etree.tostring(root, encoding='utf-8').decode('utf-8'))
f.close()

