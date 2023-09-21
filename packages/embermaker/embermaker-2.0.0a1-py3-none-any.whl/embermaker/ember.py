"""
The ember module defines IPCC-style 'burning embers' that can be inserted in ember diagrams (EmberGraph).
"""
import numpy as np
from embermaker import helpers as hlp
from embermaker.helpers import norm
from embermaker.drawinglib.helpers import mm, stringwidth
from embermaker.graphbase import Element, Coord, vaxis, cbyinterp


def get_skeygroup(sortlist=None):
    """
    Gets a sort key function to sort embers by groups.
    :param sortlist: the ordered list of groups; if None, embers will be sorted by alphabetic order.
    :return: the sort key fct
    """
    def skeygroup(be):
        """
        Used for sorting embers by group. If sortlist is defined, tries to use the order defined in this list.
        :param be: an ember object
        :return: sort key value
        """
        if sortlist:
            try:
                pos = sortlist.index(be.group.lower())
            except ValueError:
                pos = -1
        else:  # sortlist is not defined: will sort by alphabetic order
            pos = be.group
        return pos
    skeygroup.haslist = sortlist is not None
    return skeygroup


def get_skeyname(sortlist=None):
    """
    Gets a sort key function to sort embers by name.
    :param sortlist: the ordered list of names; if None, embers will be sorted by alphabetic order.
    :return: the sort key fct
    """
    def skeyname(be):
        """
        Used for sorting embers by name. If sortlist is defined, tries to use the order defined in this list.
        :param be: an ember object
        :return: sort key value
        """
        if sortlist:
            try:
                pos = sortlist.index(be.name.lower())
            except ValueError:
                pos = -1
        else:  # sortlist is not defined: will sort by alphabetic order
            pos = be.name
        return pos
    skeyname.haslist = sortlist is not None
    return skeyname


def get_skeyrisk(sortrlev=None, sorthazl=None):
    """
    Gets a sort key based on risk or hazard levels
    :param sortrlev: the risk level for which hazard will be obtained, then used as sort criteria
    :param sorthazl: the hazard level for which risk will be obtained, then used as sort criteria
    :return:
    """
    def skeyrisk(be):
        """
        :param be: an ember object
        :return: sort key
        """
        try:
            hazl = be.levels_values("hazl")
            risk = be.levels_values("risk")
            if sortrlev is not None:
                if risk[-1] > sortrlev:
                    pos = np.interp(sortrlev, risk, hazl)
                else:
                    # Might be improved; idea is to keep a minimal sorting when the sort criteria cannot work...
                    pos = 5.0 + np.interp(sortrlev / 2.0, risk, hazl)
            elif sorthazl is not None:
                if hazl[-1] > sorthazl:
                    pos = np.interp(sorthazl, hazl, risk)
                else:
                    pos = risk[-1]
            else:
                raise Exception("Skeyrisk cannot generate a sort key because no sort level was provided.")
        except ValueError:
            pos = 999
        if be.getmeta("inclusion_level") == 0:  # Ignore embers with Inclusion Level = 0; could be improved?
            pos = -1  # ignore ember
        return pos
    skeyrisk.haslist = sortrlev is not None or sorthazl is not None
    return skeyrisk


def selecsort(lbes, fkey: callable, reverse=False):
    """
    Sorts embers in lbes but ignores those absent from sortlist (=> fkey(be) = -1 above)
    (no ready-made option to do that?).
    :param lbes: a list of BEs
    :param fkey: the sort-key function
    :param reverse: reverses sorting order
    :return: sorted and filtered list of BEs
    """
    # Filtering
    if fkey.haslist:
        # Filtering occurs only if a sort criteria is defined (no sorting => no filtering)
        lbes = [be for be in lbes if fkey(be) != -1]
    # Sorting
    lbes.sort(key=fkey, reverse=reverse)
    return lbes


def drawlinear(egr, xmin, xmax, yamin, yamax, ygmin, ygmax, yvmin, yvmax, plotlevels, colorlevels):
    """
    This method handles the drawing of a colour gradient in a box, to fulfill the common needs of
    drawing embers and drawing the legend.
    The arguments are explained in self.draw.
    """
    c = egr.c
    # Set the properties of the box around the ember:
    linewidth = 0.35 * mm
    c.set_stroke_width(linewidth)

    # Useful intermediary variable(s):
    xsiz = xmax - xmin

    # Draw the background grey area in case of 'missing data'
    c.rect(xmin, yamin, xsiz, yamax - yamin, stroke='black', fill='vlgrey')

    # Enclosing rectangle
    rect = (xmin, yvmin, xsiz, yvmax - yvmin)

    # Draw the color gradients
    if yamax - yamin > xmax - xmin:  # vertical (the criteria is based on the axis, regardless of the data)
        c.lin_gradient_rect(rect, (xmin, ygmin, xmin, ygmax), colorlevels, plotlevels)
    else:  # horizontal, for legend only (would not work for regular embers, as these are more complex)
        c.lin_gradient_rect(rect, (xmin, ygmin, xmax, ygmin), colorlevels, plotlevels)

    # Draw the surrounding box
    c.rect(xmin, yamin, xsiz, yamax - yamin, stroke='black')


class Level(dict):
    """
    A dictionnary providing data about a level (phase, hazl, conf), with additional specific features:
    - storing a reference to the parent transition
    - ability to respond to ['risk'] by calculating the risk index from phase and transition name
    Note: phases are "steps" within transitions (see Transition below).
    """
    def __init__(self, trans, *args):
        """
        :param trans: the transition object within which this level resides
        :param args: at least this dictionnary: {"phase":phase, "hazl":hazl, "conf":conf}
        """
        super(Level, self).__init__(*args)
        self.trans = trans

    def __getitem__(self, key: str) -> str or float or int:
        if key in self:
            return super(Level, self).__getitem__(key)
        elif key == "risk":
            if "phase" not in self:
                raise Exception("'risk' is undefined because phase is undefined")
            # Calculate the risk index from the transition and "phase":
            return self.trans.base_risk(0) + Transition.phaserisk(self["phase"]) * self.trans.base_risk(1)
        else:
            raise KeyError(key)


class Transition(object):
    """
    A transition is a fraction of an ember containing data about how risk changes from one level to the next.
    This concept was mostly absent from the first versions of EmberFactory because the risk changes were defined
    as unique, 'global' risk-hazard functions containing all changes.
    It is currently implemented as an addition to the initial framework with minimal interference with it:
    it will enable better documentation of transitions within the Ember class, but the existing EF code will continue
    to work without changes at least in a first step.
    A transition has a name and a list of levels.
    """

    # 'Synonyms', i.e. values which can be used but will be substituted at reading:
    names_syn = {'white to yellow': 'undetectable to moderate',
                 'yellow to red': 'moderate to high',
                 'red to purple': 'high to very high'}
    # Phases are "steps" within transitions; they also have synonyms:
    phases_std = {'min': 0.0, 'median': 0.5, 'max': 1.0, 'mode': 'mode'}
    # mode is not an actual 'phase', it is only used for elicitation
    # the value provided above is the 'percentile' within the transition
    phases_syn = {'begin': 'min', 'end': 'max', 'most likely': 'mode'}
    # A risk level is attributed to each (transition, phase) pair, knowing that
    # Undetectable is level 0, Moderate is level 1, high is level 2 and very high is level 3.
    # For example Undetectable to moderate = 0 -> 1, Moderate to high 1 -> 2...
    # *.5 = Median risk levels, and more generally *.# = percentile # within the transition, noted p#

    @classmethod
    def phaserisk(cls, phasename):
        """
        Phaserisk returns the value of the "risk index" relative to the bottom of a transition.
        "Phase" refers to a risk level within a transition for which the hazard is assessed, that is, a transition is
        assessed in several "phases".
        :param phasename: the name of the "phase" within a transition, such as min, median, max or percentile (p*)
        :return: the risk index, as fraction of the full transition [0-1], relative to the start of the transition
        """
        # Todo: shouldn't this be a method of the Levels instead of Transitions? (phase relates to levels)
        if phasename in cls.phases_syn:
            phasename = cls.phases_syn[phasename]

        if phasename in cls.phases_std:
            return cls.phases_std[phasename]
        elif phasename[0] == "p":
            try:
                return float(phasename[1:])/100.0
            except ValueError:
                pass
        # We get here in case of failure (the phasename isn't a defined phase name or a percentile).
        return None

    def __init__(self, name):
        """
        Creates standard attributes for transitions
        """
        self.levels = []
        if name in self.names_syn:
            name = self.names_syn[name]
        self.name = name
        self.meta = {}  # Metadata, as for embers
        # A mode may be attributed to transitions within the expert elicitation process;
        # In this context, the mode is the most likely value in a probability distribution.
        self.mode = None
        self.be = None  # Parent ember; set when the transition is added to an ember.

    def append_level(self, phase, hazl, conf):
        """
        Adds a level to this transition.
        :param str phase: the name of the phase (see Transition and Level)
        :param float hazl: the hazard level
        :param str conf: the confidence level
        :return:
        """
        level = Level(self, {"phase": phase, "hazl": float(hazl), "conf": conf})
        self.levels.append(level)

    def __getitem__(self, phase: str) -> Level:
        """
        Returns the level object for the requested phase in this transition.
        :param phase:
        """
        level = None
        for level in self.levels:
            if level['phase'] == phase:
                break
        return level

    def __str__(self):
        """
        So that Transitions can 'pretty-print' themselves
        """
        return self.name

    def base_risk(self, vid):
        """
        Returns the risk index at the bottom of this transition
        :return:
        """
        if self.be is None or self.be.egr.cpal is None:
            raise Exception(f"Transition '{self.name}' is not attached to an ember: "
                            f"base_risk cannot be provided because risk levels are not defined.")

        transnames_risk = self.be.egr.cpal.transnames_risk
        if self.name not in transnames_risk:
            raise Exception(f"Unknown transition named '{self.name}'")

        return transnames_risk[self.name][vid]

    def phases(self):
        return [level['phase'] for level in self.levels]

    def getmeta(self, name, default=None, html=False):
        """
        Returns transition-related metadata (these differ from file- or ember- related metadata).
        :param name: the name of the parameter to be returned.
        :param default: a default value, for use when there is no metadata corresponding to this name
        :param html: process the value trough helper.htmlbreaks
        :return: the requested metadata, or None if the metadata is not defined.
        """
        try:
            value = self.meta[name]
            if value is not None and html:
                value = hlp.htmlbreaks(value)
        except KeyError:
            value = default
        if value is None and default is not None:
            value = default
        return value


class Ember(Element):
    """
    An ember is one set of data in a "burning embers" diagram.
    It contains hazard levels and associated risk levels, as well as the 'draw' method to plot itself.
    """
    parent_type = "EmberGroup"
    _elementary = True

    def __init__(self, name=None):
        """
        Initializes an ember, by creating standard attributes
        """
        super().__init__()
        self.name = str(name) if name else ""
        self.long_name = ""
        self.group = ""
        self.trans: list[Transition] = []  # Transitions
        self.haz_valid = [0, 0]  # Hazard range (min, max) for which this ember is assumed valid (= risk was assessed)
        self.hazn = None  # Standard name of the hazard variable
        self.meta = {}  # Dictionnary of ember-related metadata
        self._inited = True

    def __str__(self):
        """
        So that embers can 'pretty-print' themselves
        :return: Ember name
        """
        return self.name

    def __repr__(self):
        """
        No known way to fully 'represent' embers so this gives a short preview of it
        :return: Ember name/group, 8 first characters
        """
        return f"Ember({self.name[0:8]}/{self.group[0:8]})"

    def __len__(self):
        """
        Returns the number of levels in this ember (total for all transitions)
        """
        # Note: it should be somewhat more efficient to just ask for len(hazl) when hazl is already available
        #       thus this might be useless
        return len(self.levels())

    def trans_append(self, trans):
        trans.be = self
        self.trans.append(trans)

    def levels(self):
        """
        Returns a flat list of levels
        :return:
        """
        # List comprehension can be applied successively: a loop is first done on .trans, then on levels it contains
        return [lv for tr in self.trans for lv in tr.levels]

    def levels_values(self, dname):
        """
        Returns a flat list or np array containing one of the data associated to the levels
        :param dname: the name of that data, that is 'risk' (risk index), 'hazl' (hazard level) or 'conf' (confidence)
        :return:
        """
        if dname in ('risk', 'hazl'):
            # Same method as for levels, but we apply it directly so that there is only one loop
            return np.array([lv[dname] for tr in self.trans for lv in tr.levels])
        elif dname == 'conf':
            return [lv[dname] for tr in self.trans for lv in tr.levels]
        else:
            raise ValueError(dname)

    def draw(self):
        """
        Draws an ember, using parameters from egr.
        Note: there was an experimental option for "circular", pie-shaped embers;
        it is no longer supported at the moment (05/2023)
        """
        egr = self.egr
        c = egr.c

        plotlevels = []
        colorlevels = []

        xmin = self.cx.c0
        xmax = self.cx.c1
        yamin = self.cy.c0
        yamax = self.cy.c1

        # Get risk and related hazard levels data
        risk = self.levels_values('risk')
        hazl = self.levels_values('hazl')

        if len(risk) == 0:
            egr.logger.addwarn(f"No data for ember: {self.name} ({self.group}).")
            return

        # Canvas range occupied by the gradients:
        ygmin = min(self.cy.tocan(np.min(hazl)), yamin)
        ygmax = max(self.cy.tocan(np.max(hazl)), yamax)
        # Canvas range for the "valid" area (intersection of the valid range and axis):
        yvmin = max(self.cy.c0, self.cy.tocan(self.haz_valid[0]))
        yvmax = min(self.cy.c1, self.cy.tocan(self.haz_valid[1]))
        if yvmin == yvmax:
            egr.logger.addfail(f"Critical error: no valid range for this ember.")

        # Remove any transition overlaps within the ember colours (do not change levels used to illustrate transitions)
        ahazl = hazl.copy()
        for ilev in np.arange(len(hazl) - 1):
            if hazl[ilev + 1] < hazl[ilev]:
                ahazl[ilev] = (hazl[ilev + 1] + hazl[ilev])/2.0
                ahazl[ilev+1] = ahazl[ilev]

        # To ensure full consistency, all hazard values are converted to canvas coordinates, and divided
        # by the range of each gradient in these coordinates (ygmax - ygmin) when plotting a gradient.

        # Generate the lists of colour change positions (`plotlevels`) and colours (colorlevels):
        for ihaz in range(len(risk)):
            # Fractional position within a gradient of each colour change
            plotlevels.append((self.cy.tocan(ahazl[ihaz]) - ygmin) / (ygmax - ygmin))
            # Associated colour
            color = cbyinterp(risk[ihaz], egr.cpal)
            colorlevels.append(color)
        # Copy the start and end colors at both ends of the plot range
        # (= extend the last colour beyond the last transition):
        plotlevels.append(1.0)
        colorlevels.append(colorlevels[-1])
        plotlevels.insert(0, 0)
        colorlevels.insert(0, colorlevels[0])  # top (copy the last available colour to the 'top' level)

        egr.logger.addinfo(f"Hazard range of the gradient: "
                           f"{self.cy.todata(ygmin):6.2f} ->{self.cy.todata(ygmax):6.2f} ")
        egr.logger.addinfo("Position as % of gradient range: " + ", ".join([f"{lv:.5f}" for lv in plotlevels]))
        egr.logger.addinfo(f"Colors: {colorlevels}")

        drawlinear(egr, xmin, xmax, yamin, yamax, ygmin, ygmax, yvmin, yvmax, plotlevels, colorlevels)

        # Add the name of the BE
        # - - - - - - - - - - -
        if egr.gp['be_name_rotate'] > 0:
            align = 'right'
            # rough estimate of the available length (could be improved if used)
            namlen = np.sqrt((egr.gp['be_x'] + egr.gp['be_int_x'])**2 + egr.gp['be_bot_y'] ** 2)
        else:
            align = 'center'
            namlen = egr.gp['be_x'] + egr.gp['be_int_x'] * 0.95
        c.paragraph(xmin + egr.gp['be_x'] / 2.0, yamin - egr.gp['fnt_size'] * 0.15, self.name,
                    width=namlen, align=align, rotate=egr.gp['be_name_rotate'],
                    valign='top', font=("Helvetica", egr.gp['fnt_size']))

        # Experimental annotation / Tooltip
        # - - - - - - - - - - - - - - - - -
        # c.rect(xmin - egr.gp['be_x'] / 2.0, yamin - egr.gp['be_bot_y'], namlen, egr.gp['be_bot_y'],
        #       stroke="transparent", fill="transparent",
        #       tooltip=self.getmeta("description"))

        # Add lines and marks indicating the confidence levels :
        # - - - - - - - - - - - - - - - - - - - - - - - - - - -
        self.drawconf(egr, xmin)

    def drawconf(self, egr, xbas):
        """
        Draws lines and marks indicating the confidence levels.
        :param egr: the EmberGraph object in which this ember is drawn.
        :param xbas: the bottom-left corner of the current ember.
        """
        c = egr.c
        hazl = self.levels_values('hazl')
        if hlp.isempty(hazl) or len(hazl) == 0:
            return
        color = 'black'

        if norm(egr.gp['show_confidence']) not in ('false', ''):
            # Set the font type and size for the symbols;
            # a scaling factor may be provided as attribute of conf_levels_graph
            fsize = egr.gp['fnt_size'] * egr.gp['conf_levels_graph']
            fname = (egr.gp.get('conf_fnt_name', default=egr.gp['fnt_name'])).strip()  # use specific font if defined
            c.set_stroke_width(0.3 * mm)
            # Get confidence level names and symbols:
            cffile = norm(egr.gp.lst('conf_levels_file'))
            cfgraph = egr.gp.lst('conf_levels_graph')

            # Define the 'gap' between confidence lines which make sures that they are not contiguous:
            ygap = self.cy.c * 0.005
            maxychi = hazl[0]  # Top of uncertainty range lines so far, to detect overlaps (initial val for ember)
            midychi = hazl[0]  # Middle of uncertainty range lines so far, to detect large overlaps
            lconflen = 0  # Stores the length of the last uncertainty range mark, to help further staggering

            # Basis position of conf levels marks on the horizontal axis
            # (xconfstep is also used to stagger the lines showing uncertainty ranges)
            if norm(egr.gp['show_confidence']) == 'on top':
                xconfstep = min(0.1 * egr.gp['be_x'], 4 * mm)
                xconf = xbas + xconfstep
                otop = True
            else:
                xconfstep = min(0.1 * egr.gp['be_int_x'], 2 * mm)
                xconf = xbas + egr.gp['be_x'] + xconfstep
                otop = False

            # Plot the confidence markings
            # . . . . . . . . . . . . . . .
            # Confidence markings may be conceptually complex; a technical information note explains the rules.
            overlapstag = 0
            for tran in self.trans:
                plevels = tran.levels
                ilo = 0  # the index of the level, inside a transition, for the start of a potential conf line
                ihi = len(plevels) - 1  # the index for the end of a potential conf line
                while ilo < ihi:
                    levlo = plevels[ilo]
                    levhi = plevels[ihi]
                    if hlp.isempty(levlo['conf']) and hlp.isempty(levhi['conf']):
                        # No confidence statement on both low and high levels: do nothing
                        ilo += 1
                        ihi -= 1
                        continue
                    if hlp.isempty(levlo['conf']):
                        # Lower level has no confidence statement: skip (this can't be an uncertainty range)
                        ilo += 1
                        continue
                    if levlo['conf'] != levhi['conf'] and not hlp.isempty(levhi['conf']):
                        egr.logger.addwarn(f"Could not define an uncertainty range for {self.name}, {tran.name}",
                                           critical=True)
                        break

                    # Calculate limits of the colour transitions along the hazard axis
                    # Lower limit of the transition 'line' in canvas coordinate (+ygap = reduce length by 2*yap):
                    yclo = self.cy.tocan(levlo['hazl']) + ygap
                    if yclo >= self.cy.c1:  # Skip any transition that would be entirely outside the plot range
                        egr.logger.addinfo('A transition is above the top of the hazard axis => skipped')
                    else:
                        # The "min" below avoids extension of the shown line above the upper end of the graph (axis)
                        ychi = min(self.cy.tocan(levhi['hazl']) - ygap, self.cy.c1)
                        yconf = (yclo + ychi) / 2.0 - fsize / 3.0

                        # Move the line and conf label to the right if there is an overlap:
                        # (1) only the lower end of the line has an overlap
                        if yclo <= maxychi:
                            overlapstag += xconfstep / 2.0
                        else:
                            overlapstag = 0
                        # (2) even the confidence level text mark has an overlap - further move to the right:
                        if yclo <= midychi:
                            overlapstag += lconflen * fsize / 2.0

                        # Updates to detect overlaps in the upcoming uncertainty ranges
                        maxychi = max(maxychi, ychi)
                        midychi = max(midychi, yconf)

                        # If 'on top' of ember, set confidence levels colour to ensure visibility:
                        if otop:
                            backcol = cbyinterp((levlo['risk'] + levhi['risk']) / 2, egr.cpal)
                            if backcol.luminance() > 0.5:  # Bright background
                                color = 'black'
                            else:
                                color = 'white'
                        # Convert the confidence level name to the symbol from the graph parameters
                        lconf = levlo['conf']
                        try:
                            conf = cfgraph[cffile.index(lconf)]
                        except ValueError:
                            egr.logger.addwarn(
                                'Confidence level from file could not be converted to graph symbol: ' + lconf)
                            conf = ""
                        c.line(xconf + overlapstag, yclo, xconf + overlapstag, ychi, stroke=color)
                        c.string(xconf + fsize / 8 + overlapstag, yconf, conf, font=(fname, fsize), color=color)
                        lconflen = len(conf)  # To handle staggering of the next line, if needed

                    # End of the processing of this potential uncertainty range: get ready for the next one
                    ilo += 1
                    ihi -= 1

    def set_cx(self, base_x):
        self.cx = Coord(base_x, self.egr.gp["be_int_x"]/2.0, self.egr.gp["be_x"], self.egr.gp["be_int_x"]/2.0)
        return self.cx.b1  # Right end of this element => left of the following one

    def check(self):
        """
        Checks consistency of the ember's data.
        :return:
        """
        hazl = self.levels_values('hazl')
        risk = self.levels_values('risk')
        if len(self.trans) == 0 or len(self.trans[0].levels) < 2:
            self.egr.logger.addwarn("No data or insufficient data for an ember: " + self.name, critical=True)
        else:
            for ilev in np.arange(len(hazl) - 1):
                rdir = 1 if (risk[-1] >= risk[0]) else -1
                if ((hazl[ilev + 1] - hazl[ilev]) * rdir) < 0:
                    # While it might be that some risk decreases with hazard, this is unusual => issue warning
                    self.egr.logger.addwarn("Risk does not increase with hazard or a transition ends above the start of"
                                            " the next one [" + str(hazl[ilev]) + " then " + str(hazl[ilev + 1])
                                            + "] for ember: " + self.name)

            r0 = min(risk)
            r1 = max(risk)
            for irisk in self.egr.cpal.cdefs[0]:  # For all risk levels that are associated to a colour...
                # Catch any risk level that is within the range of this ember but not defined in this ember:
                if r0 <= irisk <= r1 and irisk not in risk:
                    self.egr.logger.addwarn(
                        "An intermediate risk level appears undefined; this will likely result in an abnormal "
                        "colour transition for ember: '" + self.name + "'", critical=True)

    def gethazl(self, itrans, phase: str):
        """
        Returns the hazard level for a given transition and phase
        :param itrans: # or name of transition in the ember
        :param phase:  name of the transition phase (min, max, median...)
        """
        trans = self.trans[itrans] if type(itrans) is int else self.transbyname(itrans)
        return trans[phase]["hazl"]

    def transnames(self):
        return [trans.name for trans in self.trans]

    def transbyname(self, name):
        try:
            itrans = self.transnames().index(name)
        except KeyError:
            return None
        return self.trans[itrans]

    def getmeta(self, name, default=None, html=False):
        """
        Returns ember-related metadata (these differ from file-related metadata).
        :param name: the name of the parameter to be returned.
        :param html: replace all linebreaks with <br>
        :param default: a default value, for use when there is no metadata corresponding to this name
        :return: the requested metadata, or None if the metadata is not defined.
        """
        try:
            value = self.meta[name]
            if value is not None and html:
                value = hlp.htmlbreaks(value)
        except KeyError:
            value = default
        if value is None and default is not None:
            value = default
        return value


class EmberGroup(Element):
    """
    A group of embers, as element on an EmberGraph
    """
    parent_type = "GraphLine"

    def __init__(self, name=None):
        super().__init__()
        self.name = name

    def attach(self, egr=None):
        super().attach(egr)
        has_ag = norm(egr.gp['haz_axis_grid']).split("-")
        # The left part [0] relates to the axis, the right part [1] relates to the grid; "group" means the group has it.
        self.has_vaxis = has_ag[0] == "group"
        self.has_vgrid = has_ag[1] == "group"
        self.has_vaxis2 = self.has_vaxis and egr.gp['haz_axis2'] in ["True", "Right"]
        self.has_vgrid2 = self.has_vgrid and egr.gp['haz_axis2'] in ["True", "Right"]

    def set_cx(self, base_x):
        # left margin (may include an axis)
        mar_1 = self.has_vaxis * (self.has_axis_name * self.egr.gp["haz_name_x"] + self.egr.gp["scale_x"])
        # right margin
        mar_2 = self.egr.gp["gr_int_x"] + self.has_vaxis2 * (self.has_axis2_name * self.egr.gp["haz_name_x"]
                                        + 3 * self.egr.gp['fnt_size']
                                        + stringwidth(self.egr.gp['haz_axis2_unit'], fontsize=self.egr.gp['fnt_size']))
                                        # Since there is no specific "scale_x" for axis2 => rough calculation
        in_0 = base_x + mar_1
        in_x = in_0
        for el in self.elements:
            in_x = el.set_cx(in_x)  # Asks the ember to set its coordinate, starting at in_x, and get in_x for the next
        self.cx = Coord(base_x, mar_1, in_x - in_0, mar_2)
        return self.cx.b1  # Right end of this element => left of the following one

    def show_changes(self):
        """
        Draws the lines showing the changes between embers
        :return:
        """
        egr = self.egr
        gp = egr.gp

        # Prepare data for each ember
        bexs = []
        ahlevs = []
        for be in self.elements:
            hazl = be.levels_values('hazl')
            risk = be.levels_values('risk')
            rlevs = gp.lst('show_changes')
            hlevs = np.interp(rlevs, risk, hazl, left=np.NaN, right=np.NaN)
            # ^When a rlev is outside the range of defined risk values, don't get a hlev (= set it to NaN)
            bexs.append(be.cx.c0 + be.cx.c/2.0)
            ahlevs.append(hlevs)
            # ^[a]ll [h]azard-[lev]els = for all requested risk levels and all embers in the group

        # Plot the connecting lines
        markers = "o" if "markers" in norm(gp['show_changes']) else None
        ahlevs = np.transpose(ahlevs)
        for shlevs in ahlevs:  # for one curve = for a [s]ingle of the requested risk-levels
            beys = [self.cy.tocan(shlev) for shlev in shlevs]  # scale to Canvas coordinates
            ymax = self.cy.tocan(gp['haz_axis_top'])  # Do not draw line from or to levels above the axis
            for ibe in range(len(beys) - 1):  # Draw, by line segment
                if beys[ibe] <= ymax and beys[ibe + 1] <= ymax:
                    # Dashed line: # 3 unit on, 2 unit off (not done with polyline because gaps may occur)
                    egr.c.line(bexs[ibe], beys[ibe], bexs[ibe + 1], beys[ibe + 1], stroke="tgrey",
                               dash=(3, 2), markers=markers)
            egr.logger.addinfo("Mean hazard / requested risk level: {:.3}".format(np.mean(shlevs)))

    def draw(self):
        egr = self.egr
        gp = egr.gp

        # Vertical axis and grid lines, if it applies to this group
        if self.has_vaxis or self.has_vgrid:
            vaxis(self)

        # Group title
        # Position in x starts at the left of the first ember colour bar (old design choice)
        x0 = self.cx.c0 + gp['be_int_x'] / 2.0
        width = self.cx.c
        if len(self.elements) == 1:
            x0 = self.cx.c0 - 3 * gp['fnt_size']
            width = self.cx.c0 + self.cx.m2
        self.egr.c.paragraph(x0, self.cy.c1 + gp['be_top_y'] * 0.35, self.name,
                             width=width, font=("Helvetica", gp['gr_fnt_size']))

        # Draw embers
        super().draw()
        # Show changes between embers (a task of the EmberGroup)
        if norm(gp['show_changes']) in ["true", "lines", "lines+markers"]:
            self.show_changes()


def gpsort(embers: list[Ember], gp):
    global logger  # Will this actually create a global variable or just access logger outside gpsort if available?
    try:
        logger
    except NameError:
        logger = hlp.Logger()

    # Sort the embers, if requested (option) Todo: move to EmberMaker
    # --------------------------------------
    # There are two sorting levels. The sorting needs to be done on the second criteria first.
    # Second sorting level
    if gp('sort_2nd_by') == 'name':
        sortlist = gp.lst_norm('sort_2nd_by')
        # Standard Python sorting by f=skeyname + delete embers not in sortlist:
        embers = selecsort(embers, get_skeyname(sortlist))
        logger.addinfo(f"Secondary sorting by name; values: {sortlist}")
    if gp('sort_2nd_by') == 'group':
        sortlist = gp.lst_norm('sort_2nd_by')
        embers = selecsort(embers, get_skeygroup(sortlist))
        logger.addinfo(f"Secondary sorting by group; values: {sortlist}")

    # The first level may swap the role of ember group and name: this allows grouping by names (becoming 'groups')
    if gp('sort_first_by') in ['name', 'group']:
        # Allow sorting according to an order set by a list in the Excel sheet:
        sortlist = gp.lst_norm('sort_first_by')
        logger.addinfo(
            f"Primary sorting by: {gp['sort_first_by']}; values: {sortlist}")
        # Allow grouping by name instead of group, by swapping groups and names:
        if gp('sort_first_by') == 'name':
            for be in embers:
                be.name, be.group = be.group, be.name
        # Sort
        embers = selecsort(embers, get_skeygroup(sortlist))
    return embers


def getgroups(embers: list[Ember]):
    """
    Create groups of embers given the group names provided in each ember (be.group), populate them with the embers,
    and returns the list of group objects.
    :param embers: a list of burning ember
    :return: the list of groups containing the grouped embers
    """
    gbe = None
    gbes = []
    for be in embers:
        if gbe is None or gbe.name != be.group:
            gbe = EmberGroup(name=be.group)
            gbes.append(gbe)
        gbe.elements.append(be)
    return gbes
