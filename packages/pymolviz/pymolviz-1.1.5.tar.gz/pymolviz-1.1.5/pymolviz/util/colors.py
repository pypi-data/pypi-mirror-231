import numpy as np

def get_colormap(colormap):
	""" Infers a colormap from the given data."""
	from matplotlib import cm

	if np.issubdtype(type(colormap), np.str_):
		if colormap == "onwhite":
			from matplotlib.colors import LinearSegmentedColormap
			colors = list(reversed([np.array([165, 0, 38]), np.array([215, 48, 39]), np.array([244, 109, 67]), np.array([116, 173, 209]), np.array([69, 117, 180]), np.array([49, 54, 149])]))
			colors = np.array(colors) / 255
			colors = [(i / (len(colors) - 1), c) for i, c in enumerate(colors)]
			colormap = LinearSegmentedColormap.from_list("onwhite", colors)
		elif colormap == "onwhite_r":
			from matplotlib.colors import LinearSegmentedColormap
			colors = [np.array([165, 0, 38]), np.array([215, 48, 39]), np.array([244, 109, 67]), np.array([116, 173, 209]), np.array([69, 117, 180]), np.array([49, 54, 149])]
			colors = np.array(colors) / 255
			colors = [(i / (len(colors) - 1), c) for i, c in enumerate(colors)]
			colormap = LinearSegmentedColormap.from_list("onwhite_r", colors)
		else:
			colormap = cm.get_cmap(colormap)
	return colormap


def _convert_string_color(color):
		from .colors import get_AA_color, get_element_color
		from matplotlib import colors
		c = get_AA_color(color)
		if not c is None:
			color = c
		else:
			c = get_element_color(color)
			if not c is None:
				color = c
			else:
				color = colors.to_rgb(color)
		return color
#deprecated
element_colors_jmol = {"H":	np.array([255,255,255]),
"He":	np.array([217,255,255]),
"Li":	np.array([204,128,255]),
"Be":	np.array([194,255,0]),
"B":	np.array([255,181,181]),
"C":	np.array([144,144,144]),
"N":	np.array([48,80,248]),
"O":	np.array([255,13,13]),
"F":	np.array([144,224,80]),
"Ne":	np.array([179,227,245]),
"Na":	np.array([171,92,242]),
"Mg":	np.array([138,255,0]),
"Al":	np.array([191,166,166]),
"Si":	np.array([240,200,160]),
"P":	np.array([255,128,0]),
"S":	np.array([255,255,48]),
"Cl":	np.array([31,240,31]),
"Ar":	np.array([128,209,227]),
"K":	np.array([143,64,212]),
"Ca":	np.array([61,255,0]),
"Sc":	np.array([230,230,230]),
"Ti":	np.array([191,194,199]),
"V":	np.array([166,166,171]),
"Cr":	np.array([138,153,199]),
"Mn":	np.array([156,122,199]),
"Fe":	np.array([224,102,51]),
"Co":	np.array([240,144,160]),
"Ni":	np.array([80,208,80]),
"Cu":	np.array([200,128,51]),
"Zn":	np.array([125,128,176]),
"Ga":	np.array([194,143,143]),
"Ge":	np.array([102,143,143]),
"As":	np.array([189,128,227]),
"Se":	np.array([255,161,0]),
"Br":	np.array([166,41,41]),
"Kr":	np.array([92,184,209]),
"Rb":	np.array([112,46,176]),
"Sr":	np.array([0,255,0]),
"Y":	np.array([148,255,255]),
"Zr":	np.array([148,224,224]),
"Nb":	np.array([115,194,201]),
"Mo":	np.array([84,181,181]),
"Tc":	np.array([59,158,158]),
"Ru":	np.array([36,143,143]),
"Rh":	np.array([10,125,140]),
"Pd":	np.array([0,105,133]),
"Ag":	np.array([192,192,192]),
"Cd":	np.array([255,217,143]),
"In":	np.array([166,117,115]),
"Sn":	np.array([102,128,128]),
"Sb":	np.array([158,99,181]),
"Te":	np.array([212,122,0]),
"I":	np.array([148,0,148]),
"Xe":	np.array([66,158,176]),
"Cs":	np.array([87,23,143]),
"Ba":	np.array([0,201,0]),
"La":	np.array([112,212,255]),
"Ce":	np.array([255,255,199]),
"Pr":	np.array([217,255,199]),
"Nd":	np.array([199,255,199]),
"Pm":	np.array([163,255,199]),
"Sm":	np.array([143,255,199]),
"Eu":	np.array([97,255,199]),
"Gd":	np.array([69,255,199]),
"Tb":	np.array([48,255,199]),
"Dy":	np.array([31,255,199]),
"Ho":	np.array([0,255,156]),
"Er":	np.array([0,230,117]),
"Tm":	np.array([0,212,82]),
"Yb":	np.array([0,191,56]),
"Lu":	np.array([0,171,36]),
"Hf":	np.array([77,194,255]),
"Ta":	np.array([77,166,255]),
"W":	np.array([33,148,214]),
"Re":	np.array([38,125,171]),
"Os":	np.array([38,102,150]),
"Ir":	np.array([23,84,135]),
"Pt":	np.array([208,208,224]),
"Au":	np.array([255,209,35]),
"Hg":	np.array([184,184,208]),
"Tl":	np.array([166,84,77]),
"Pb":	np.array([87,89,97]),
"Bi":	np.array([158,79,181]),
"Po":	np.array([171,92,0]),
"At":	np.array([117,79,69]),
"Rn":	np.array([66,130,150]),
"Fr":	np.array([66,0,102]),
"Ra":	np.array([0,125,0]),
"Ac":	np.array([112,171,250]),
"Th":	np.array([0,186,255]),
"Pa":	np.array([0,161,255]),
"U":	np.array([0,143,255]),
"Np":	np.array([0,128,255]),
"Pu":	np.array([0,107,255]),
"Am":	np.array([84,92,242]),
"Cm":	np.array([120,92,227]),
"Bk":	np.array([138,79,227]),
"Cf":	np.array([161,54,212]),
"Es":	np.array([179,31,212]),
"Fm":	np.array([179,31,186]),
"Md":	np.array([179,13,166]),
"No":	np.array([189,13,135]),
"Lr":	np.array([199,0,102]),
"Rf":	np.array([204,0,89]),
"Db":	np.array([209,0,79]),
"Sg":	np.array([217,0,69]),
"Bh":	np.array([224,0,56]),
"Hs":	np.array([230,0,46]),
"Mt":	np.array([235,0,38])
}


def get_element_color(element):
    if not element.lower() in element_colors_pymol:
        element = element_symbol_to_name.get(element, "")
    return element_colors_pymol.get(element.lower(), None)

# element symbol mapped to element name
element_symbol_to_name = {
"H": "Hydrogen",
"He": "Helium",
"Li": "Lithium",
"Be": "Beryllium",
"B": "Boron",
"C": "Carbon",
"N": "Nitrogen",
"O": "Oxygen",
"F": "Fluorine",
"Ne": "Neon",
"Na": "Sodium",
"Mg": "Magnesium",
"Al": "Aluminum",
"Si": "Silicon",
"P": "Phosphorus",
"S": "Sulfur",
"Cl": "Chlorine",
"Ar": "Argon",
"K": "Potassium",
"Ca": "Calcium",
"Sc": "Scandium",
"Ti": "Titanium",
"V": "Vanadium",
"Cr": "Chromium",
"Mn": "Manganese",
"Fe": "Iron",
"Co": "Cobalt",
"Ni": "Nickel",
"Cu": "Copper",
"Zn": "Zinc",
"Ga": "Gallium",
"Ge": "Germanium",
"As": "Arsenic",
"Se": "Selenium",
"Br": "Bromine",
"Kr": "Krypton",
"Rb": "Rubidium",
"Sr": "Strontium",
"Y": "Yttrium",
"Zr": "Zirconium",
"Nb": "Niobium",
"Mo": "Molybdenum",
"Tc": "Technetium",
"Ru": "Ruthenium",
"Rh": "Rhodium",
"Pd": "Palladium",
"Ag": "Silver",
"Cd": "Cadmium",
"In": "Indium",
"Sn": "Tin",
"Sb": "Antimony",
"Te": "Tellurium",
"I": "Iodine",
"Xe": "Xenon",
"Cs": "Caesium",
"Ba": "Barium",
"La": "Lanthanum",
"Ce": "Cerium",
"Pr": "Praseodymium",
"Nd": "Neodymium",
"Pm": "Promethium",
"Sm": "Samarium",
"Eu": "Europium",
"Gd": "Gadolinium",
"Tb": "Terbium",
"Dy": "Dysprosium",
"Ho": "Holmium",
"Er": "Erbium",
"Tm": "Thulium",
"Yb": "Ytterbium",
"Lu": "Lutetium",
"Hf": "Hafnium",
"Ta": "Tantalum",
"W": "Tungsten",
"Re": "Rhenium",
"Os": "Osmium",
"Ir": "Iridium",
"Pt": "Platinum",
"Au": "Gold",
"Hg": "Mercury",
"Tl": "Thallium",
"Pb": "Lead",
"Bi": "Bismuth",
"Po": "Polonium",
"At": "Astatine",
"Rn": "Radon",
"Fr": "Francium",
"Ra": "Radium",
"Ac": "Actinium",
"Th": "Thorium",
"Pa": "Protactinium",
"U": "Uranium",
"Np": "Neptunium",
"Pu": "Plutonium",
"Am": "Americium",
"Cm": "Curium",
"Bk": "Berkelium",
"Cf": "Californium",
"Es": "Einsteinium",
"Fm": "Fermium",
"Md": "Mendelevium",
"No": "Nobelium",
"Lr": "Lawrencium",
"Rf": "Rutherfordium",
"Db": "Dubnium",
"Sg": "Seaborgium",
"Bh": "Bohrium",
"Hs": "Hassium",
"Mt": "Meitnerium"
}

# element colors as in pymol
element_colors_pymol = {
    "actinium": 	np.array([0.439215686, 	0.670588235, 	0.980392157]), 	
  	"aluminum": 	np.array([0.749019608, 	0.650980392, 	0.650980392]), 	
  	"americium": 	np.array([0.329411765, 	0.360784314, 	0.949019608]), 	
  	"antimony": 	np.array([0.619607843, 	0.388235294, 	0.709803922]), 	
  	"argon": 	np.array([0.501960784, 	0.819607843, 	0.890196078]), 	
  	"arsenic": 	np.array([0.741176471, 	0.501960784, 	0.890196078]), 	
  	"astatine": 	np.array([0.458823529, 	0.309803922, 	0.270588235]), 	
  	"barium": 	np.array([0.000000000, 	0.788235294, 	0.000000000]), 	
  	"berkelium": 	np.array([0.541176471, 	0.309803922, 	0.890196078]), 	
  	"beryllium": 	np.array([0.760784314, 	1.000000000, 	0.000000000]), 	
  	"bismuth": 	np.array([0.619607843, 	0.309803922, 	0.709803922]), 	
  	"bohrium": 	np.array([0.878431373, 	0.000000000, 	0.219607843]), 	
  	"boron": 	np.array([1.000000000, 	0.709803922, 	0.709803922]), 	
  	"bromine": 	np.array([0.650980392, 	0.160784314, 	0.160784314]), 	
  	"cadmium": 	np.array([1.000000000, 	0.850980392, 	0.560784314]), 	
  	"calcium": 	np.array([0.239215686, 	1.000000000, 	0.000000000]), 	
  	"californium": 	np.array([0.631372549, 	0.211764706, 	0.831372549]), 	
  	"carbon": 	np.array([0.2, 	1.0, 	0.2]), 	
  	"cerium": 	np.array([1.000000000, 	1.000000000, 	0.780392157]), 	
  	"cesium": 	np.array([0.341176471, 	0.090196078, 	0.560784314]), 	
  	"chlorine": 	np.array([0.121568627, 	0.941176471, 	0.121568627]), 	
  	"chromium": 	np.array([0.541176471, 	0.600000000, 	0.780392157]), 	
  	"cobalt": 	np.array([0.941176471, 	0.564705882, 	0.627450980]), 	
  	"copper": 	np.array([0.784313725, 	0.501960784, 	0.200000000]), 	
  	"curium": 	np.array([0.470588235, 	0.360784314, 	0.890196078]), 	
  	"deuterium": 	np.array([0.9, 	0.9, 	0.9]), 	
  	"dubnium": 	np.array([0.819607843, 	0.000000000, 	0.309803922]), 	
  	"dysprosium": 	np.array([0.121568627, 	1.000000000, 	0.780392157]), 	
  	"einsteinium": 	np.array([0.701960784, 	0.121568627, 	0.831372549]), 	
  	"erbium": 	np.array([0.000000000, 	0.901960784, 	0.458823529]), 	
  	"europium": 	np.array([0.380392157, 	1.000000000, 	0.780392157]), 	
  	"fermium": 	np.array([0.701960784, 	0.121568627, 	0.729411765]), 	
  	"fluorine": 	np.array([0.701960784, 	1.000000000, 	1.000000000]), 	
  	"francium": 	np.array([0.258823529, 	0.000000000, 	0.400000000]), 	
  	"gadolinium": 	np.array([0.270588235, 	1.000000000, 	0.780392157]), 	
  	"gallium": 	np.array([0.760784314, 	0.560784314, 	0.560784314]), 	
  	"germanium": 	np.array([0.400000000, 	0.560784314, 	0.560784314]), 	
  	"gold": 	np.array([1.000000000, 	0.819607843, 	0.137254902]), 	
  	"hafnium": 	np.array([0.301960784, 	0.760784314, 	1.000000000]), 	
  	"hassium": 	np.array([0.901960784, 	0.000000000, 	0.180392157]), 	
  	"helium": 	np.array([0.850980392, 	1.000000000, 	1.000000000]), 	
  	"holmium": 	np.array([0.000000000, 	1.000000000, 	0.611764706]), 	
  	"hydrogen": 	np.array([0.9, 	0.9, 	0.9]), 	
  	"indium": 	np.array([0.650980392, 	0.458823529, 	0.450980392]), 	
  	"iodine": 	np.array([0.580392157, 	0.000000000, 	0.580392157]), 	
  	"iridium": 	np.array([0.090196078, 	0.329411765, 	0.529411765]), 	
  	"iron": 	np.array([0.878431373, 	0.400000000, 	0.200000000]), 	
  	"krypton": 	np.array([0.360784314, 	0.721568627, 	0.819607843]), 	
  	"lanthanum": 	np.array([0.439215686, 	0.831372549, 	1.000000000]), 	
  	"lawrencium": 	np.array([0.780392157, 	0.000000000, 	0.400000000]), 	
  	"lead": 	np.array([0.341176471, 	0.349019608, 	0.380392157]), 	
  	"lithium": 	np.array([0.800000000, 	0.501960784, 	1.000000000]), 	
  	"lutetium": 	np.array([0.000000000, 	0.670588235, 	0.141176471]), 	
  	"magnesium": 	np.array([0.541176471, 	1.000000000, 	0.000000000]), 	
  	"manganese": 	np.array([0.611764706, 	0.478431373, 	0.780392157]), 	
  	"meitnerium": 	np.array([0.921568627, 	0.000000000, 	0.149019608]), 	
  	"mendelevium": 	np.array([0.701960784, 	0.050980392, 	0.650980392]), 	
  	"mercury": 	np.array([0.721568627, 	0.721568627, 	0.815686275]), 	
  	"molybdenum": 	np.array([0.329411765, 	0.709803922, 	0.709803922]), 	
  	"neodymium": 	np.array([0.780392157, 	1.000000000, 	0.780392157]), 	
  	"neon": 	np.array([0.701960784, 	0.890196078, 	0.960784314]), 	
  	"neptunium": 	np.array([0.000000000, 	0.501960784, 	1.000000000]), 	
  	"nickel": 	np.array([0.313725490, 	0.815686275, 	0.313725490]), 	
  	"niobium": 	np.array([0.450980392, 	0.760784314, 	0.788235294]), 	
  	"nitrogen": 	np.array([0.2, 	0.2, 	1.0]), 	
  	"nobelium": 	np.array([0.741176471, 	0.050980392, 	0.529411765]), 	
  	"osmium": 	np.array([0.149019608, 	0.400000000, 	0.588235294]), 	
  	"oxygen": 	np.array([1.0, 	0.3, 	0.3]), 	
  	"palladium": 	np.array([0.000000000, 	0.411764706, 	0.521568627]), 	
  	"phosphorus": 	np.array([1.000000000, 	0.501960784, 	0.000000000]), 	
  	"platinum": 	np.array([0.815686275, 	0.815686275, 	0.878431373]), 	
  	"plutonium": 	np.array([0.000000000, 	0.419607843, 	1.000000000]), 	
  	"polonium": 	np.array([0.670588235, 	0.360784314, 	0.000000000]), 	
  	"potassium": 	np.array([0.560784314, 	0.250980392, 	0.831372549]), 	
  	"praseodymium": 	np.array([0.850980392, 	1.000000000, 	0.780392157]), 	
  	"promethium": 	np.array([0.639215686, 	1.000000000, 	0.780392157]), 	
  	"protactinium": 	np.array([0.000000000, 	0.631372549, 	1.000000000]), 	
  	"radium": 	np.array([0.000000000, 	0.490196078, 	0.000000000]), 	
  	"radon": 	np.array([0.258823529, 	0.509803922, 	0.588235294]), 	
  	"rhenium": 	np.array([0.149019608, 	0.490196078, 	0.670588235]), 	
  	"rhodium": 	np.array([0.039215686, 	0.490196078, 	0.549019608]), 	
  	"rubidium": 	np.array([0.439215686, 	0.180392157, 	0.690196078]), 	
  	"ruthenium": 	np.array([0.141176471, 	0.560784314, 	0.560784314]), 	
  	"rutherfordium": 	np.array([0.800000000, 	0.000000000, 	0.349019608]), 	
  	"samarium": 	np.array([0.560784314, 	1.000000000, 	0.780392157]), 	
  	"scandium": 	np.array([0.901960784, 	0.901960784, 	0.901960784]), 	
  	"seaborgium": 	np.array([0.850980392, 	0.000000000, 	0.270588235]), 	
  	"selenium": 	np.array([1.000000000, 	0.631372549, 	0.000000000]), 	
  	"silicon": 	np.array([0.941176471, 	0.784313725, 	0.627450980]), 	
  	"silver": 	np.array([0.752941176, 	0.752941176, 	0.752941176]), 	
  	"sodium": 	np.array([0.670588235, 	0.360784314, 	0.949019608]), 	
  	"strontium": 	np.array([0.000000000, 	1.000000000, 	0.000000000]), 	
  	"sulfur": 	np.array([0.9, 	0.775, 	0.25]), 	
  	"tantalum": 	np.array([0.301960784, 	0.650980392, 	1.000000000]), 	
  	"technetium": 	np.array([0.231372549, 	0.619607843, 	0.619607843]), 	
  	"tellurium": 	np.array([0.831372549, 	0.478431373, 	0.000000000]), 	
  	"terbium": 	np.array([0.188235294, 	1.000000000, 	0.780392157]), 	
  	"thallium": 	np.array([0.650980392, 	0.329411765, 	0.301960784]), 	
  	"thorium": 	np.array([0.000000000, 	0.729411765, 	1.000000000]), 	
  	"thulium": 	np.array([0.000000000, 	0.831372549, 	0.321568627]), 	
  	"tin": 	np.array([0.400000000, 	0.501960784, 	0.501960784]), 	
  	"titanium": 	np.array([0.749019608, 	0.760784314, 	0.780392157]), 	
  	"tungsten": 	np.array([0.129411765, 	0.580392157, 	0.839215686]), 	
  	"uranium": 	np.array([0.000000000, 	0.560784314, 	1.000000000]), 	
  	"vanadium": 	np.array([0.650980392, 	0.650980392, 	0.670588235]), 	
  	"xenon": 	np.array([0.258823529, 	0.619607843, 	0.690196078]), 	
  	"ytterbium": 	np.array([0.000000000, 	0.749019608, 	0.219607843]), 	
  	"yttrium": 	np.array([0.580392157, 	1.000000000, 	1.000000000]), 	
  	"zinc": 	np.array([0.490196078, 	0.501960784, 	0.690196078]), 	
  	"zirconium": 	np.array([0.580392157, 	0.878431373, 	0.878431373]), 	
}

def get_AA_color(AA):
    return amino_acid_colors.get(AA.lower(), None)

# amino acid colors as in jmol
amino_acid_colors = {
"ala":	np.array([200,200,200])/255,
"arg":	np.array([20,90,255])/255,
"asn":	np.array([0,220,220])/255,
"asp":	np.array([230,10,10])/255,
"cys":	np.array([230,230,0])/255,
"gln":	np.array([0,220,220])/255,
"glu":	np.array([230,10,10])/255,
"gly":	np.array([235,235,235])/255,
"his":	np.array([130,130,210])/255,
"ile":	np.array([15,130,15])/255,
"leu":	np.array([15,130,15])/255,
"lys":	np.array([20,90,255])/255,
"met":	np.array([230,230,0])/255,
"phe":	np.array([50,50,170])/255,
"pro":	np.array([220,150,130])/255,
"ser":	np.array([250,150,0])/255,
"thr":	np.array([250,150,0])/255,
"trp":	np.array([180,90,180])/255,
"tyr":	np.array([50,50,170])/255,
"val":	np.array([15,130,15])/255,
"asx":	np.array([255,105,180])/255,
"glx":	np.array([255,105,180])/255,
"other":np.array([190,160,110])/255,
}