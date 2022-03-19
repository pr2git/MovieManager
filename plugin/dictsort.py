dictSortCZ = {
	u'ch': u'h|',
	u'CH': u'H|',
	u'Ch': u'H|',
	u'Ch': u'h|',
	u'\xc1': u'A|',
	u'\xc4': u'A}',
	u'\u010c': u'C|',
	u'\u010e': u'D|',
	u'\xc9': u'E|',
	u'\u011a': u'E}',
	u'\xcb': u'E~',
	u'\xcd': u'I|',
	u'\xcf': u'I}',
	u'\u0139': u'L|',
	u'\u013d': u'L}',
	u'\u0141': u'L~',
	u'\u0147': u'N|',
	u'\xd3': u'O|',
	u'\xd4': u'O}',
	u'\xd6': u'O~',
	u'\u0154': u'R|',
	u'\u0158': u'R}',
	u'\u0160': u'S|',
	u'\u0164': u'T|',
	u'\xda': u'U|',
	u'\u016e': u'U}',
	u'\xdc': u'U~',
	u'\xdd': u'Y|',
	u'\u0178': u'Y}',
	u'\u017d': u'Z|',
	u'\xe1': u'a|',
	u'\xe4': u'a}',
	u'\u010d': u'c|',
	u'\u010f': u'd|',
	u'\xe9': u'e|',
	u'\u011b': u'e}',
	u'\xeb': u'e~',
	u'\xed': u'i|',
	u'\xef': u'i}',
	u'\u013a': u'l|',
	u'\u013e': u'l}',
	u'\u0142': u'l~',
	u'\u0148': u'n|',
	u'\xf3': u'o|',
	u'\xf6': u'o}',
	u'\xf4': u'o~',
	u'\u0159': u'r|',
	u'\u0155': u'r}',
	u'\u0161': u's|',
	u'\u0165': u't|',
	u'\xfa': u'u|',
	u'\u016f': u'u}',
	u'\xfc': u'u~',
	u'\xfd': u'y|',
	u'\xff': u'y}',
	u'\u017e': u'z|'
}


def char2DiacriticSort(text):
#    if isinstance(text, str):
#        text = unicode(text, 'utf-8')
    for i, j in dictSortCZ.iteritems():
        text = text.replace(i, j)
    return text