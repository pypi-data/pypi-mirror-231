#!/usr/bin/env python3
# from avlwrapper import Aircraft, Symmetry, Surface, Point
import avlwrapper as avl


class Aircraft:
    def __init__(
        self,
        mach: float,
        reference_chord: float,
        reference_span: float,
        surfaces_list: list,
        ground_effect: float | None = None,
        ref_point_x: float = 0.0,
        ref_point_y: float = 0.0,
        ref_point_z: float = 0.0,
    ) -> None:
        self.mach = mach
        self.h_ge = ground_effect
        self.__c = reference_chord
        self.__b = reference_span
        self.__x = ref_point_x
        self.__y = ref_point_y
        self.__z = ref_point_z
        self.surfaces = surfaces_list
        self.__surfaces = [part.surface for part in surfaces_list]

    """ GET PROPERTIES """

    @property
    def chord(self) -> float:
        return self.__c

    @property
    def span(self) -> float:
        return self.__b

    @property
    def ref_area(self) -> float:
        return self.__b * self.__c

    @property
    def ref_x(self) -> float:
        return self.__x

    @property
    def ref_y(self) -> float:
        return self.__y

    @property
    def ref_z(self) -> float:
        return self.__z

    @property
    def ref_point(self) -> avl.Point:
        return avl.Point(self.__x, self.__y, self.__z)

    """ SET PROPERTIES """

    @chord.setter
    def chord(self, value):
        self.__c = value

    @span.setter
    def span(self, value):
        self.__b = value

    @ref_x.setter
    def ref_x(self, value):
        self.__x = value

    @ref_y.setter
    def ref_y(self, value):
        self.__y = value

    @ref_z.setter
    def ref_z(self, value):
        self.__z = value

    def geometry(self, name):
        if self.h_ge != None:
            aircraft = avl.Aircraft(
                name=name,
                reference_area=self.ref_area,
                reference_chord=self.chord,
                reference_span=self.span,
                reference_point=self.ref_point,
                mach=self.mach,
                z_symmetry=avl.Symmetry.symmetric,
                z_symmetry_plane=-self.h_ge,
                surfaces=self.__surfaces,
            )
        else:
            aircraft = avl.Aircraft(
                name=name,
                reference_area=self.ref_area,
                reference_chord=self.chord,
                reference_span=self.span,
                reference_point=self.ref_point,
                mach=self.mach,
                z_symmetry=avl.Symmetry.none,
                surfaces=self.__surfaces,
            )

        return aircraft

    def plot(
        self, figure=None, axis=None, linewidth: float = 1.0, color='black'
    ) -> tuple:

        for surface in self.surfaces:
            figure, axis = surface.plot(figure, axis, linewidth, color)
        return figure, axis

    def sessao_critica(
        alpha_max: float,
        CL_max: float,
        airplane: avl.Aircraft,
        trim_param: avl.Parameter,
    ):
        ...
        # alpha_cases = [alpha_max, 2.2*alpha_max, 0]
        # cases = [Case(name=f'trimmed{i}', alpha=case, elevator=trim_param)
        #         for i, case in enumerate(alpha_cases)]
        # session = Session(geometry=airplane.geometry('aircraft'), cases=cases)
        # results_cruz = session.run_all_cases()

        # CL_wing = [results_cruz[i + 1]['StripForces']['wing']['cl'][0]
        #             for i, _ in enumerate(alpha_cases)]
        # i_stall = [i + 1
        #             for i, CL_wup in enumerate(CL_wing)
        #             if CL_wup < CL_max][0]

        # CLmax, CDmax, CLt, alpha_m, K = estabilidade.interp(results_cruz, CL_max, i_stall, 1)
        # CLt0 = results_cruz[1]['SurfaceForces']['Tail']['CL']
        # CMalpha = results_cruz[1]['StabilityDerivatives']['Cma']
        # return CLmax, CDmax, CLt, alpha_m, K, CLt0, CMalpha
