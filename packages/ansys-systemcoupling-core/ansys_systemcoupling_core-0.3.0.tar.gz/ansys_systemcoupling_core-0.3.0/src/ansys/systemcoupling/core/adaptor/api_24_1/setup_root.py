#
# This is an auto-generated file.  DO NOT EDIT!
#

SHASH = "add18659c90558849a12bc4820dc48069961268d3b1790256ae8a6fe59db8067"

from ansys.systemcoupling.core.adaptor.impl.types import *

from ._add_participant import _add_participant
from .activate_hidden import activate_hidden
from .add_data_transfer import add_data_transfer
from .add_data_transfer_by_display_names import add_data_transfer_by_display_names
from .add_expression_function import add_expression_function
from .add_interface import add_interface
from .add_interface_by_display_names import add_interface_by_display_names
from .add_named_expression import add_named_expression
from .add_participant import add_participant
from .add_reference_frame import add_reference_frame
from .add_transformation import add_transformation
from .analysis_control import analysis_control
from .coupling_interface import coupling_interface
from .coupling_participant import coupling_participant
from .delete_transformation import delete_transformation
from .generate_input_file import generate_input_file
from .get_execution_command import get_execution_command
from .get_region_names_for_participant import get_region_names_for_participant
from .get_setup_summary import get_setup_summary
from .get_status_messages import get_status_messages
from .has_input_file_changed import has_input_file_changed
from .import_system_coupling_input_file import import_system_coupling_input_file
from .library import library
from .output_control import output_control
from .reload_expression_function_modules import reload_expression_function_modules
from .solution_control import solution_control
from .update_participant import update_participant


class setup_root(Container):
    """
    'root' object
    """

    syc_name = "SystemCoupling"

    child_names = [
        "activate_hidden",
        "library",
        "coupling_participant",
        "analysis_control",
        "coupling_interface",
        "solution_control",
        "output_control",
    ]

    activate_hidden: activate_hidden = activate_hidden
    """
    activate_hidden child of setup_root.
    """
    library: library = library
    """
    library child of setup_root.
    """
    coupling_participant: coupling_participant = coupling_participant
    """
    coupling_participant child of setup_root.
    """
    analysis_control: analysis_control = analysis_control
    """
    analysis_control child of setup_root.
    """
    coupling_interface: coupling_interface = coupling_interface
    """
    coupling_interface child of setup_root.
    """
    solution_control: solution_control = solution_control
    """
    solution_control child of setup_root.
    """
    output_control: output_control = output_control
    """
    output_control child of setup_root.
    """
    command_names = [
        "_add_participant",
        "add_data_transfer",
        "add_data_transfer_by_display_names",
        "add_expression_function",
        "add_interface",
        "add_interface_by_display_names",
        "add_named_expression",
        "add_participant",
        "add_reference_frame",
        "add_transformation",
        "delete_transformation",
        "generate_input_file",
        "get_execution_command",
        "get_region_names_for_participant",
        "get_setup_summary",
        "get_status_messages",
        "has_input_file_changed",
        "import_system_coupling_input_file",
        "reload_expression_function_modules",
        "update_participant",
    ]

    _add_participant: _add_participant = _add_participant
    """
    _add_participant command of setup_root.
    """
    add_data_transfer: add_data_transfer = add_data_transfer
    """
    add_data_transfer command of setup_root.
    """
    add_data_transfer_by_display_names: add_data_transfer_by_display_names = (
        add_data_transfer_by_display_names
    )
    """
    add_data_transfer_by_display_names command of setup_root.
    """
    add_expression_function: add_expression_function = add_expression_function
    """
    add_expression_function command of setup_root.
    """
    add_interface: add_interface = add_interface
    """
    add_interface command of setup_root.
    """
    add_interface_by_display_names: add_interface_by_display_names = (
        add_interface_by_display_names
    )
    """
    add_interface_by_display_names command of setup_root.
    """
    add_named_expression: add_named_expression = add_named_expression
    """
    add_named_expression command of setup_root.
    """
    add_participant: add_participant = add_participant
    """
    add_participant command of setup_root.
    """
    add_reference_frame: add_reference_frame = add_reference_frame
    """
    add_reference_frame command of setup_root.
    """
    add_transformation: add_transformation = add_transformation
    """
    add_transformation command of setup_root.
    """
    delete_transformation: delete_transformation = delete_transformation
    """
    delete_transformation command of setup_root.
    """
    generate_input_file: generate_input_file = generate_input_file
    """
    generate_input_file command of setup_root.
    """
    get_execution_command: get_execution_command = get_execution_command
    """
    get_execution_command command of setup_root.
    """
    get_region_names_for_participant: get_region_names_for_participant = (
        get_region_names_for_participant
    )
    """
    get_region_names_for_participant command of setup_root.
    """
    get_setup_summary: get_setup_summary = get_setup_summary
    """
    get_setup_summary command of setup_root.
    """
    get_status_messages: get_status_messages = get_status_messages
    """
    get_status_messages command of setup_root.
    """
    has_input_file_changed: has_input_file_changed = has_input_file_changed
    """
    has_input_file_changed command of setup_root.
    """
    import_system_coupling_input_file: import_system_coupling_input_file = (
        import_system_coupling_input_file
    )
    """
    import_system_coupling_input_file command of setup_root.
    """
    reload_expression_function_modules: reload_expression_function_modules = (
        reload_expression_function_modules
    )
    """
    reload_expression_function_modules command of setup_root.
    """
    update_participant: update_participant = update_participant
    """
    update_participant command of setup_root.
    """
