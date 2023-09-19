
from typing import List
from enum import IntEnum, unique


class layer_settings():
    def __init__(self) -> None:
        pass


class extended_settings():
    def __init__(self) -> None:
        pass

    def get_btl_wall_export(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_chief_element(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_group_export(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_ignore_for_connector_axis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_log_home_export(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_log_macro_export(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_mfb_export(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_outline_export(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_piece_by_piece_export_with_dimensions(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_piece_by_piece_export_without_dimensions(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def get_wall_export(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def set_btl_wall_export(self, value: bool) -> None:
        """set btl wall export

        Args:
            value (bool): condition

        Returns:
            None
        """

    def set_chief_element(self, value: bool) -> None:
        """set chief element

        Args:
            value (bool): condition

        Returns:
            None
        """

    def set_group_export(self, value: bool) -> None:
        """set group export

        Args:
            value (bool): condition

        Returns:
            None
        """

    def set_ignore_for_connector_axis(self, value: bool) -> None:
        """set ignore for connector axis

        Args:
            value (bool): condition

        Returns:
            None
        """

    def set_log_home_export(self, value: bool) -> None:
        """set log home export

        Args:
            value (bool): condition

        Returns:
            None
        """

    def set_mfb_export(self, value: bool) -> None:
        """set mfb export

        Args:
            value (bool): condition

        Returns:
            None
        """

    def set_outline_export(self, value: bool) -> None:
        """set outline export

        Args:
            value (bool): condition

        Returns:
            None
        """

    def set_piece_by_piece_export_with_dimensions(self, value: bool) -> None:
        """set piece by piece export with dimensions

        Args:
            value (bool): condition

            Returns:
                None
        """

    def set_piece_by_piece_export_without_dimensions(self, value: bool) -> None:
        """set piece by piece export without dimensions

        Args:
            value (bool): condition

        Returns:
            None
        """

    def set_wall_export(self, value: bool) -> None:
        """set wall export

        Args:
            value (bool): condition

        Returns:
            None
        """


class output_type():
    def __init__(self) -> None:
        pass

    def is_hip_valley(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_jack_rafter(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_log(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_none(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_panel_1(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_panel_2(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_panel_3(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_panel_4(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_panel_5(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_purlin(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rafter(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rough_volume_framed_wall(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rough_volume_log_home(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rough_volume_solid_wood_wall(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_stud(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_tread(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_truss(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_1(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_2(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_3(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_4(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_5(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def set_hip_valley(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_jack_rafter(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_log(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_none(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_1(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_2(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_3(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_4(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_5(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_purlin(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_rafter(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_rough_volume_framed_wall(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_rough_volume_log_home(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_rough_volume_solid_wood_wall(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_stud(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_tread(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_truss(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_1(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_2(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_3(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_4(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_5(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """


class process_type():
    def __init__(self) -> None:
        pass

    def is_hip_valley(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_jack_rafter(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_log(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_none(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_panel_1(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_panel_2(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_panel_3(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_panel_4(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_panel_5(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_purlin(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rafter(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rough_volume_framed_wall(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rough_volume_log_home(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rough_volume_solid_wood_wall(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_stud(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_tread(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_truss(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_1(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_2(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_3(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_4(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_user_5(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def set_hip_valley(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_jack_rafter(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_log(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_none(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_1(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_2(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_3(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_4(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_panel_5(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_purlin(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_rafter(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_rough_volume_framed_wall(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_rough_volume_log_home(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_rough_volume_solid_wood_wall(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_stud(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_tread(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_truss(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_1(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_2(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_3(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_4(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """

    def set_user_5(self) -> None:
        """setter method - usage see https://docs.cadwork.com/projects/cwapi3dpython/en/latest/examples/cadwork/#output-type
        """


class element_type():
    def __init__(self) -> None:
        pass

    def isAdditionalElement(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isAuxiliary(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isCadwork(self) -> bool:
        """

        !!! Warning
            Function deprecated.

        Returns:
            bool: condition
        """

    def isCircularAxis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isCircularBeam(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isConnectorAxis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isConnectorNode(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isContainer(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isDimension(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isDrillingAxis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isEaveAxis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isExportSolid(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isExportSolidScene(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isFloor(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isGlobalCut(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isGraphicalObject(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isLine(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isNestingParent(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isNone(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isNormalNode(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isOpening(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isPanel(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isRectangularAxis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isRectangularBeam(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isRoof(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isRoom(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isRotationElement(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isSectionTrace(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isSteelShape(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isSurface(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isTextDocument(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isWall(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def isWireAxis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_additional_element(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_auxiliary(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_cadwork(self) -> bool:
        """
        !!! Warning
            Function deprecated.

        Returns:
            bool: condition
        """

    def is_circular_axis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_circular_beam(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_connector_axis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_connector_node(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_container(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_dimension(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_drilling_axis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_eave_axis(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_export_solid(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_export_solid_scene(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_floor(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_global_cut(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_graphical_object(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_line(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_nesting_parent(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_none(self) -> bool:
        """



        Returns:
            bool: condition
        """

    def is_normal_node(self) -> bool:
        """



        Returns:
            bool: condition
        """

    def is_opening(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_panel(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rectangular_axis(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_rectangular_beam(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_roof(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_room(self) -> bool:
        """
         Returns:
             bool: condition
         """

    def is_rotation_element(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_section_trace(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_steel_shape(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_surface(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_text_document(self) -> bool:
        """

        Returns:
            bool: condition
        """

    def is_wall(self) -> bool:
        """
        Returns:
            bool: condition
        """

    def is_wire_axis(self) -> bool:
        """

        Returns:
            bool: condition
        """


class rgb_color():
    def __init__(self, r: int, b: int, g: int) -> None:
        self.r = r
        self.b = b
        self.g = g


class visibility_state():
    def __init__(self) -> None:
        pass


class activation_state():
    def __init__(self) -> None:
        pass


class point_3d():

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, another_point_3d):
        """adds two points

        Args:
            point_3d (point_3d): a second point

        Returns:
            point_3d: a third point
        """

    def __sub__(self, another_point_3d):
        """subtracts two points

        Args:
            point_3d (point_3d): a second point

        Returns:
            point_3d: a third point
        """

    def __mul__(self, another_point_3d):
        """multiplies two points

        Args:
            point_3d (point_3d): a second point

        Returns:
            point_3d: a third point
        """

    def __div__(self, another_point_3d):
        """divides two points

        Args:
            point_3d (point_3d): a second point

        Returns:
            point_3d: a third point
        """

    def __eq__(self, another_point_3d):
        """checks if two points are equal

        Args:
            point_3d (point_3d): a second point

        Returns:
            bool: condition
        """

    def __ne__(self, another_point_3d):
        """checks if two points are not equal

        Args:
            point_3d (point_3d): a second point
        """

    def __getitem__(self, index: int):
        """gets the value of a point at a given index

        Args:
            index (int): index

        Returns:
            float: value
        """

    def __setitem__(self, index: int, value: float):
        """sets the value of a point at a given index

        Args:
            index (int): index
            value (float): value
        """

    def cross(self, another_point_3d):
        """cross product takes two vectors and produces a third vector that is orthogonal to both

        Args:
            point_3d (point_3d): a second vector

        Returns:
            point_3d: a third vector orthogonal to both
        """

    def distance(self, another_point_3d) -> float:
        """distance between to points

        Args:
            point_3d (point_3d): a second point

        Returns:
            float: distance
        """

    def dot(self, another_point_3d) -> float:
        """When calculating the dot product of two unit vectors, the result is always between -1 and +1.
        The scalar product of two vectors of given length is thus zero if they are perpendicular to each other, and maximum if they have the same direction.
        A negative dot product between two vectors means that the two vectors go in the opposite general direction.

        Args:
            point_3d (point_3d): a second vector

        Returns:
            float: value betweend 0.0 and 1.0
        """

    def magnitude(self) -> float:
        """magnitude of a vector is the length of the vector.

        Returns:
            float: vector length
        """

    def normalized(self):
        """A normalized vector is a vector with a length equal to one unit.

        Returns:
            point_3d: normalized vector
        """

    def invert(self):
        """Invert point_3d

        Returns:
            point_3d: inverted point_3d
        """


def get_auto_attribute_elements() -> List[int]:
    """Get ontly the elements of the selected types in the attribute manager dialog. All other elements will 
    get an empty attribute value.

    Returns:
        List[int]: element IDs
    """


def set_auto_attribute(elements: List[int], value: str) -> None:
    """Set the auto attribute to the selected element types. 

    Args:
        elements (List[int]): element IDs 
        value (str): attribute 
    """


class element_module_properties():
    def __init__(self) -> None:
        pass

    def get_cutting_element_priority(self, element_module_properties) -> int:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cutting_priority = cw.element_module_properties.get_cutting_element_priority(element_module_properties)

        Args:
            element_module_properties (_type_): element module properties

        Returns:
            int: cutting_element_priority
        """

    def get_distribute_in_axis_direction_distance(self, element_module_properties) -> float:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> distribute_in_axis_direction_distance = cw.element_module_properties.get_distribute_in_axis_direction_distance(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            float: distribute_in_axis_direction_distance
        """

    def get_distribute_in_axis_direction_number(self, element_module_properties) -> int:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> distribute_in_axis_direction_number = cw.element_module_properties.get_distribute_in_axis_direction_number(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            int: distribute_in_axis_direction_number
        """

    def get_distribute_perpendicular_to_axis_direction_distance(self, element_module_properties) -> float:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> distribute_perpendicular_to_axis_direction_distance = cw.element_module_properties.get_distribute_perpendicular_to_axis_direction_distance(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            float: distribute_perpendicular_to_axis_direction_distance
        """

    def get_distribute_perpendicular_to_axis_direction_number(self, element_module_properties) -> int:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> distribute_perpendicular_to_axis_direction_number = cw.element_module_properties.get_distribute_perpendicular_to_axis_direction_number(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            int: distribute_perpendicular_to_axis_direction_number
        """

    def get_keep_in_center_of_layer_current_wall(self, element_module_properties) -> str:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> unique_layer_name = cw.element_module_properties.get_keep_in_center_of_layer_current_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            str: unique_layer_name
        """

    def get_keep_in_center_of_layer_neighbour_wall(self, element_module_properties) -> str:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> unique_layer_name = cw.element_module_properties.get_keep_in_center_of_layer_neighbour_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            str: unique_layer_name
        """

    def get_unique_layername(self, element_module_properties) -> str:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> unique_layer_name = cw.element_module_properties.get_unique_layername(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            str: unique_layer_name
        """

    def is_auxiliary(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_auxiliary = cw.element_module_properties.is_auxiliary(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_bottom_plate(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_bottom_plate = cw.element_module_properties.is_bottom_plate(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_cutting_element(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_cutting_element = cw.element_module_properties.is_cutting_element(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_in_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_in_axis_direction = cw.element_module_properties.is_distribute_in_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_in_axis_direction_use_max_distance(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_in_axis_direction_use_max_distance = cw.element_module_properties.is_distribute_in_axis_direction_use_max_distance(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_in_axis_direction_use_number(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_in_axis_direction_use_number = cw.element_module_properties.is_distribute_in_axis_direction_use_number(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_perpendicular_to_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_perpendicular_to_axis_direction = cw.element_module_properties.is_distribute_perpendicular_to_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_perpendicular_to_axis_direction_use_max_distance(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_perpendicular_to_axis_direction_use_max_distance = cw.element_module_properties.is_distribute_perpendicular_to_axis_direction_use_max_distance(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_distribute_perpendicular_to_axis_direction_use_number(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_distribute_perpendicular_to_axis_direction_use_number = cw.element_module_properties.is_distribute_perpendicular_to_axis_direction_use_number(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_element_from_detail(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_element_from_detail = cw.element_module_properties.is_element_from_detail(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_keep_in_center_of_layer_current_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_keep_in_center_of_layer_current_wall = cw.element_module_properties.is_keep_in_center_of_layer_current_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_keep_in_center_of_layer_neighbour_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_keep_in_center_of_layer_neighbour_wall = cw.element_module_properties.is_keep_in_center_of_layer_neighbour_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_main_element(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_main_element = cw.element_module_properties.is_main_element(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_move_according_length_axis(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_move_according_length_axis = cw.element_module_properties.is_move_according_length_axis(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_move_according_thickness_axis(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_move_according_thickness_axis = cw.element_module_properties.is_move_according_thickness_axis(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_move_with_top_of_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_move_with_top_of_wall = cw.element_module_properties.is_move_with_top_of_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_no_collision_control(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_no_collision_control = cw.element_module_properties.is_no_collision_control(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_no_inside_cover_control(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_no_inside_cover_control = cw.element_module_properties.is_no_inside_cover_control(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_not_cut_with_cutting_element(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_not_cut_with_cutting_element = cw.element_module_properties.is_not_cut_with_cutting_element(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_not_placed_at_end_of_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_not_placed_at_end_of_wall = cw.element_module_properties.is_not_placed_at_end_of_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_not_placed_at_start_of_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_not_placed_at_start_of_wall = cw.element_module_properties.is_not_placed_at_start_of_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_opening_lintel(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_opening_lintel = cw.element_module_properties.is_opening_lintel(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_opening_sill(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_opening_sill = cw.element_module_properties.is_opening_sill(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_solder_in_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_solder_in_axis_direction = cw.element_module_properties.is_solder_in_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stop_in_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stop_in_axis_direction = cw.element_module_properties.is_stop_in_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stop_perpendicular_to_axis_direction(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stop_perpendicular_to_axis_direction = cw.element_module_properties.is_stop_perpendicular_to_axis_direction(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_strecht_according_length_axis(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_strecht_according_length_axis = cw.element_module_properties.is_strecht_according_length_axis(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_strecht_according_thickness_axis(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_strecht_according_thickness_axis = cw.element_module_properties.is_strecht_according_thickness_axis(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stretch_with_opening_lintel(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stretch_with_opening_lintel = cw.element_module_properties.is_stretch_with_opening_lintel(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stretch_with_opening_sill(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stretch_with_opening_sill = cw.element_module_properties.is_stretch_with_opening_sill(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stretch_in_opening_width(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stretch_in_opening_width = cw.element_module_properties.is_stretch_in_opening_width(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_stretch_with_top_of_wall(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_stretch_with_top_of_wall = cw.element_module_properties.is_stretch_with_top_of_wall(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_top_plate(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_top_plate = cw.element_module_properties.is_top_plate(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
        Returns:
            bool: condition
        """

    def is_unique_layername(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_unique_layername = cw.element_module_properties.is_unique_layername(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def is_use_for_detail_coordinate_system(self, element_module_properties) -> bool:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> is_use_for_detail_coordinate_system = cw.element_module_properties.is_use_for_detail_coordinate_system(element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties

        Returns:
            bool: condition
        """

    def set_auxiliary(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_auxiliary(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_bottom_plate(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_bottom_plate(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_cutting_element(self, element_module_properties, active: bool, priority: int) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_cutting_element(element_module_properties, True, 3)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            priority (int): _description_
        """

    def set_distribute_in_axis_direction_use_max_distance(self, element_module_properties, acitve: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_in_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_in_axis_direction_use_max_distance(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            priority (int): _description_
        """

    def set_distribute_in_axis_direction_use_number(self, element_module_properties, active: bool, number: int) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_in_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_in_axis_direction_use_number(element_module_properties, True, 11)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            number (int): _description_
        """

    def set_distribute_in_axis_direction(self, element_module_properties, active: bool, distance: float) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_in_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_in_axis_direction_use_max_distance(element_module_properties, False)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            distance (float): _description_
        """

    def set_distribute_perpendicular_to_axis_direction_use_max_distance(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction_use_max_distance(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_distribute_perpendicular_to_axis_direction_use_number(self, element_module_properties, active: bool, number: int) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction_use_number(element_module_properties, True, 15)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            number (int): _description_
        """

    def set_distribute_perpendicular_to_axis_direction(self, element_module_properties, active: bool, distance: float) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction(element_module_properties, True, 555.5)
                >>> cw.element_module_properties.set_distribute_perpendicular_to_axis_direction_use_max_distance(element_module_properties, False)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            distance (float): _description_
        """

    def set_element_from_detail(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_element_from_detail(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_keep_in_center_of_layer_current_wall(self, element_module_properties, active: bool, layer_name: str) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_keep_in_center_of_layer_current_wall(element_module_properties, True, 'layer_name')
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            name (str): _description_
        """

    def set_keep_in_center_of_layer_neighbour_wall(self, element_module_properties, active: bool, layer_name: str) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_keep_in_center_of_layer_neighbour_wall(element_module_properties, True, 'layer_name')
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            name (str): _description_
        """

    def set_keep_in_center_of_rough_volume(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_keep_in_center_of_rough_volume(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_main_element(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_keep_in_center_of_rough_volume(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_move_according_length_axis(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_move_according_length_axis(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_move_according_thickness_axis(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_move_according_thickness_axis(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_move_with_top_of_wall(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_move_with_top_of_wall(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_no_collision_control(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_no_collision_control(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_no_inside_cover_control(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_no_inside_cover_control(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_not_cut_with_cutting_element(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_not_cut_with_cutting_element(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_not_placed_at_end_of_wall(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_not_placed_at_end_of_wall(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_not_placed_at_start_of_wall(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_not_placed_at_start_of_wall(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_opening_lintel(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_opening_lintel(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_opening_sill(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_opening_sill(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_solder_in_axis_direction(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_solder_in_axis_direction(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stop_in_axis_direction(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stop_in_axis_direction(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stop_perpendicular_to_axis_direction(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stop_perpendicular_to_axis_direction(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_according_length_axis(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_strecht_according_length_axis(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_according_thickness_axis(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_strecht_according_thickness_axis(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_with_opening_lintel(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stretch_with_opening_lintel(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_with_opening_sill(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stretch_with_opening_sill(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_with_top_of_wall(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stretch_with_top_of_wall(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_stretch_in_opening_width(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_stretch_in_opening_width(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_top_plate(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_top_plate(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """

    def set_unique_layername(self, element_module_properties, active: bool, layer_name: str) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_unique_layername(element_module_properties, True, 'layer_name')
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
            name (str): _description_
        """

    def set_use_for_detail_coordinate_system(self, element_module_properties, active: bool) -> None:
        """
        Examples:
            >>> import element_controller as ec
            >>> import cadwork as cw
            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> element_module_properties = ec.get_element_module_properties_for_element(element)
                >>> cw.element_module_properties.set_use_for_detail_coordinate_system(element_module_properties, True)
                >>> ec.set_element_module_properties_for_elements([element], element_module_properties)

        Args:
            element_module_properties (_element_module_properties_): element module properties
            active (bool): _description_
        """


class ifc_2x3_element_type():
    def __init__(self) -> None:
        pass

    def is_ifc_beam(self, ifc_type) -> bool:
        """
        Examples:
            >>> import      element_controller      as ec
            >>> import      bim_controller          as bc
            >>> import      cadwork

            >>> element_ids = ec.get_active_identifiable_element_ids()
            >>> for element in element_ids:
                >>> ifc_type = bc.get_ifc2x3_element_type(element)
                >>> if cadwork.ifc_2x3_element_type.is_ifc_member(ifc_type):
                    >>>   # do something
        Args:
            ifc_type (_type_): ifc element type

        Returns:
            bool: condition
        """

    def is_ifc_building_element_part(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_building_element_proxy(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_chimney(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_column(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_covering(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_curtain_wall(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_discrete_accessory(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_door(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_fastener(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_flow_segment(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_footing(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_furnishing_element(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_mechanical_fastener(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_member(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_opening_element(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_plate(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_railing(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_ramp(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_ramp_flight(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_roof(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_slab(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_space(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_stair(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_stair_flight(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_wall(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_wall_standard_case(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_ifc_window(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def is_none(self, ifc_type) -> bool:
        """ToDo Documentation
        """

    def set_ifc_beam(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_building_element_part(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_building_element_proxy(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_chimney(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_column(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_covering(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_curtain_wall(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_discrete_accessory(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_door(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_fastener(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_flow_segment(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_footing(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_furnishing_element(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_mechanical_fastener(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_member(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_opening_element(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_plate(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_railing(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_ramp(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_ramp_flight(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_roof(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_slab(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_space(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_stair(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_stair_flight(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_wall(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_wall_standard_case(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_ifc_window(self, element_ids: List[int], ifc_type) -> None:
        """ToDo Documentation
        """

    def set_none(self, element_ids: List[int], ifc_type) -> None:
        """_summary_

        Args:
            element_ids (List[int]): _description_
            ifc_type (_type_): _description_
        """


@unique
class node_symbol(IntEnum):
    """Change node symbol. 

    Examples:
        >>> point = cadwork.point_3d(0, 0, 0)
        >>> node = element_controller.create_node(point)
        >>> node.set_node_symbol(node, node_symbol.circle)

    Args:
        SmallCircle (int): 1
        Square (int): 2
        Cross (int): 3
        Circle (int): 4
        FilledCircle (int): 5
        ChessSquare (int): 6
        HalfFilledSquare (int): 7
        CrossSquare (int): 8
        FilledSquare (int): 9  
    """
    SmallSquare = 1
    Square = 2
    Cross = 3
    Circle = 4
    FilledCircle = 5
    ChessSquare = 6
    HalfFilledSquare = 7
    CrossSquare = 8
    FilledSquare = 9

    def __int__(self) -> int:
        return self.value


@unique
class element_module_detail(IntEnum):
    """Add element situation to detail. 

    Examples:
        >>> element_controller.add_elements_to_detail(element_ids, element_module_detail.cross)

    Args:
        no_detail (int): 0
        angle_detail (int): 1
        area_detail (int): 2
        cross_detail (int): 3
        edge_detail (int): 4
        end_detail (int): 5
        line_detail (int): 6
        open_detail (int): 7
        t_detail (int): 8
        floor_area_detail (int): 9
        floor_end_detail (int): 10
        floor_line_detail (int): 11
        floor_open_detail (int): 12

    """
    no_detail = 0,
    angle_detail = 1,
    area_detail = 2,
    cross_detail = 3,
    edge_detail = 4,
    end_detail = 5,
    line_detail = 6,
    open_detail = 7,
    t_detail = 8,
    floor_area_detail = 9,
    floor_end_detail = 10,
    floor_line_detail = 11,
    floor_open_detail = 12

    def __int__(self) -> int:
        return self.value


@unique
class division_zone_direction(IntEnum):
    """ Add division zone direction.

    Examples:
        >>> point = cadwork.point_3d(0, 0, 0)
        >>> geometry_controller.create_division_zone(123456, point, division_zone_direction.positive)

    Args:
        positive (int): 1
        negative (int): -1
        none (int): 0
    """
    positive = 1
    negative = -1
    no_direction = 0

    def __int__(self) -> int:
        return self.value


@unique
class shortcut_key(IntEnum):
    """Shortcut key.

    Examples:
        >>> utility_controller.execute_shortcut(shortcut_key.F1, shortcut_key_modifier.shift)

    Args:
        F1 (int): 1
        F2 (int): 2
        F3 (int): 3
        F4 (int): 4
        F5 (int): 5
        F6 (int): 6
        F7 (int): 7
        F8 (int): 8
        F9 (int): 9
        F10 (int): 10
        F11 (int): 11
        F12 (int): 12
    """
    F1 = 1
    F2 = 2
    F3 = 3
    F4 = 4
    F5 = 5
    F6 = 6
    F7 = 7
    F8 = 8
    F9 = 9
    F10 = 10
    F11 = 11
    F12 = 12

    def __int__(self) -> int:
        return self.value


@unique
class shortcut_key_modifier(IntEnum):
    """Shortcut key.

    Examples:
        >>> utility_controller.execute_shortcut(shortcut_key.F1, shortcut_key_modifier.shift)

    Args:
        no_modifier (int): 0
        shift (int): 1
        ctrl (int): 2
        alt (int): 3
    """
    no_modifier = 0
    shift = 1
    ctrl = 2
    alt = 3

    def __int__(self) -> int:
        return self.value


@unique
class btl_version(IntEnum):
    """BTL version.

    Examples:
        >>> machine_controller.export_btl(btl_version.btl_1_6, "C:\\temp\\test.btl")

    Args:
        btl_1_0 (int): 110
        btl_1_1 (int): 111
        btl_1_2 (int): 112
        btl_1_3 (int): 113
        btl_1_4 (int): 114
        btl_1_5 (int): 115
        btl_1_6 (int): 116

    """
    btl_1_0 = 110
    btl_1_1 = 111
    btl_1_2 = 112
    btl_1_3 = 113
    btl_1_4 = 114
    btl_1_5 = 115
    btl_1_6 = 116

    def __int__(self) -> int:
        return self.value


@unique
class hundegger_machine_type(IntEnum):
    """Hundegger machine type.

    Examples:
        >>> machine_controller.export_hundegger(hundegger_machine_type.k2)

    Args:
        p8_10 (int): 1
        k1 (int): 2
        k2 (int): 3
        k2_cambium (int): 4
        k2_uf_5 (int): 5
        k2_uf_5_cambium (int): 6
        speedcut (int): 7
        pba (int): 8
        pba_bvx (int): 9
        pba_bvx_cambium (int): 10
        spm (int): 12
        spm_cambium (int): 13
        robot_drive (int): 14
        turbo_drive (int): 15

    """

    p8_10 = 1
    k1 = 2
    k2 = 3
    k2_cambium = 4
    k2_uf_5 = 5
    k2_uf_5_cambium = 6
    speedcut = 7
    pba = 8
    pba_bvx = 9
    pba_bvx_cambium = 10
    spm = 12
    spm_cambium = 13
    robot_drive = 14
    turbo_drive = 15

    def __int__(self) -> int:
        return self.value


@unique
class weinmann_mfb_version(IntEnum):
    """Weinmann MFB version.

    Examples:
        >>> machine_controller.export_weinmann_mfb(weinmann_mfb_version.wup_2_0)

    Args:
        wup_2_0 (int): 20
        wup_3_1 (int): 31
        wup_3_2 (int): 32
        wup_3_3 (int): 33
        wup_3_4 (int): 34

    """

    wup_2_0 = 20
    wup_3_1 = 31
    wup_3_2 = 32
    wup_3_3 = 33
    wup_3_4 = 34

    def __int__(self) -> int:
        return self.value


@unique
class element_grouping_type(IntEnum):
    """ Element grouping type.

    Examples:
        >>> attribute_controller.set_element_grouping_type(element_grouping_type.subgroup)
        >>> attribute_controller.get_element_grouping_type()

    Args:
        group (int): 1
        subgroup (int): 2

    """

    group = 1
    subgroup = 2
    _none = 3

    def __int__(self) -> int:
        return self.value
