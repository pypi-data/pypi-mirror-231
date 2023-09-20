from flightanalysis.base.table import Table, SVar, Constructs, SVar
from geometry import Point


class Coefficients(Table):
    constructs = Table.constructs + Constructs([
        SVar("force", Point, ["cx", "cy", "cz"], None),
        SVar("moment", Point, ["cl", "cm", "cn"], None)
    ])

    @staticmethod
    def build(sec, flow, consts):
        I = consts.inertia
        u = sec.vel
        du = sec.acc
        w = sec.rvel
        dw = sec.racc
        moment=I*(dw + w.cross(w)) / (flow.q * consts.s) 
        #not correct need to extend geometry module to include inertia matrix

        return Coefficients.from_constructs(
            sec.time,
            force=(du + w.cross(u)) * consts.mass / (flow.q * consts.s),
            moment=moment / Point(consts.b, consts.c, consts.b).tile(len(moment))
        )



