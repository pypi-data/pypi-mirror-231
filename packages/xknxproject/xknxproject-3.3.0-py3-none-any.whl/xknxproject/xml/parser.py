"""Parser logic for ETS XML files."""
from __future__ import annotations

import html
import logging

from striprtf.striprtf import rtf_to_text

from xknxproject.__version__ import __version__
from xknxproject.loader import (
    ApplicationProgramLoader,
    HardwareLoader,
    KNXMasterLoader,
    ProjectLoader,
)
from xknxproject.models import (
    MEDIUM_TYPES,
    Area,
    CommunicationObject,
    Device,
    DeviceInstance,
    Flags,
    Function,
    GroupAddress,
    GroupAddressRef,
    GroupAddressStyle,
    GroupRange,
    HardwareToPrograms,
    KNXProject,
    Line,
    Product,
    ProjectInfo,
    Space,
    XMLArea,
    XMLFunction,
    XMLGroupAddress,
    XMLGroupAddressRef,
    XMLGroupRange,
    XMLProjectInformation,
    XMLSpace,
)
from xknxproject.zip.extractor import KNXProjContents

_LOGGER = logging.getLogger("xknxproject.log")


class XMLParser:
    """Class that parses XMLs and returns useful information."""

    def __init__(self, knx_proj_contents: KNXProjContents) -> None:
        """Initialize the parser."""
        self.knx_proj_contents = knx_proj_contents
        self.spaces: list[XMLSpace] = []
        self.group_addresses: list[XMLGroupAddress] = []
        self.group_ranges: list[XMLGroupRange] = []
        self.areas: list[XMLArea] = []
        self.devices: list[DeviceInstance] = []
        self.language_code: str | None = None

        self.project_info: XMLProjectInformation
        self.functions: list[XMLFunction] = []

    def parse(self, language: str | None = None) -> KNXProject:
        """Parse ETS files."""
        self.load(language=language)
        _ga_id_to_address = {ga.identifier: ga.address for ga in self.group_addresses}

        communication_objects: dict[str, CommunicationObject] = {}
        devices_dict: dict[str, Device] = {}
        for device in self.devices:
            device_com_objects: list[str] = []
            for com_object in device.com_object_instance_refs:
                if not com_object.links:
                    continue
                group_address_links = [
                    valid_link
                    for link in com_object.links
                    if (valid_link := _ga_id_to_address.get(link))
                ]
                if not group_address_links:
                    # skip orphaned ComObjectInstanceRef pointing only to non-existent GroupAddress
                    # see https://github.com/XKNX/knx-frontend/issues/71
                    continue
                com_object_key = f"{device.individual_address}/{com_object.ref_id}"
                communication_objects[com_object_key] = CommunicationObject(
                    name=com_object.name,  # type: ignore[typeddict-item]
                    number=com_object.number,  # type: ignore[typeddict-item]
                    text=com_object.text,  # type: ignore[typeddict-item]
                    function_text=com_object.function_text,  # type: ignore[typeddict-item]
                    description=com_object.description or "",
                    device_address=device.individual_address,
                    dpts=com_object.datapoint_types,
                    object_size=com_object.object_size,  # type: ignore[typeddict-item]
                    flags=Flags(
                        read=com_object.read_flag,  # type: ignore[typeddict-item]
                        write=com_object.write_flag,  # type: ignore[typeddict-item]
                        communication=com_object.communication_flag,  # type: ignore[typeddict-item]
                        update=com_object.update_flag,  # type: ignore[typeddict-item]
                        read_on_init=com_object.read_on_init_flag,  # type: ignore[typeddict-item]
                        transmit=com_object.transmit_flag,  # type: ignore[typeddict-item]
                    ),
                    group_address_links=group_address_links,
                )
                device_com_objects.append(com_object_key)

            devices_dict[device.individual_address] = Device(
                name=device.product_name,
                hardware_name=device.hardware_name,
                description=device.description,
                manufacturer_name=device.manufacturer_name,
                individual_address=device.individual_address,
                project_uid=device.project_uid,
                communication_object_ids=device_com_objects,
            )

        topology_dict: dict[str, Area] = {}
        for area in self.areas:
            lines_dict: dict[str, Line] = {}
            for line in area.lines:
                devices_topology: list[str] = []
                for device in line.devices:
                    devices_topology.append(device.individual_address)
                lines_dict[str(line.address)] = Line(
                    name=line.name,
                    description=line.description,
                    devices=devices_topology,
                    medium_type=MEDIUM_TYPES.get(line.medium_type, "Unknown"),
                )
            topology_dict[str(area.address)] = Area(
                name=area.name, description=area.description, lines=lines_dict
            )

        group_address_dict: dict[str, GroupAddress] = {}
        for group_address in self.group_addresses:
            _com_object_ids = [
                com_object_id
                for com_object_id, com_object in communication_objects.items()
                if group_address.address in com_object["group_address_links"]
            ]
            group_address_dict[group_address.address] = GroupAddress(
                name=group_address.name,
                identifier=group_address.identifier,
                raw_address=group_address.raw_address,
                address=group_address.address,
                project_uid=group_address.project_uid,
                dpt=group_address.dpt,
                communication_object_ids=_com_object_ids,
                description=group_address.description,
                comment=html.unescape(rtf_to_text(group_address.comment)),
            )

        group_range_dict: dict[str, GroupRange] = {}
        for group_range in self.group_ranges:
            group_range_dict[group_range.str_address()] = self.convert_group_range(
                group_range, self.project_info.group_address_style
            )

        space_dict: dict[str, Space] = {}
        for space in self.spaces:
            space_dict[space.name] = self.recursive_convert_spaces(space)

        functions_dict: dict[str, Function] = {}
        for function in self.functions:
            functions_dict[function.identifier] = self.convert_functions(function)

        info = ProjectInfo(
            project_id=self.project_info.project_id,
            name=self.project_info.name,
            last_modified=self.project_info.last_modified,
            group_address_style=self.project_info.group_address_style.value,
            guid=self.project_info.guid,
            created_by=self.project_info.created_by,
            schema_version=self.project_info.schema_version,
            tool_version=self.project_info.tool_version,
            xknxproject_version=__version__,
            language_code=self.language_code,
        )

        return KNXProject(
            info=info,
            communication_objects=communication_objects,
            topology=topology_dict,
            devices=devices_dict,
            group_addresses=group_address_dict,
            group_ranges=group_range_dict,
            locations=space_dict,
            functions=functions_dict,
        )

    def convert_group_address_ref(
        self, group_address_ref: XMLGroupAddressRef
    ) -> GroupAddressRef:
        """Convert group address ref to the final output format."""
        return GroupAddressRef(
            address=group_address_ref.address,
            name=group_address_ref.name,
            project_uid=group_address_ref.project_uid,
            role=group_address_ref.role,
        )

    def convert_functions(self, function: XMLFunction) -> Function:
        """Convert function to the final output format."""

        ga_dict = {}
        for group_address in function.group_addresses:
            ga_dict[group_address.address] = self.convert_group_address_ref(
                group_address
            )

        return Function(
            function_type=function.function_type,
            group_addresses=ga_dict,
            identifier=function.identifier,
            name=function.name,
            project_uid=function.project_uid,
            space_id=function.space_id,
            usage_text=function.usage_text,
        )

    def recursive_convert_spaces(self, space: XMLSpace) -> Space:
        """Convert spaces to the final output format."""
        subspaces: dict[str, Space] = {}
        for subspace in space.spaces:
            subspaces[subspace.name] = self.recursive_convert_spaces(subspace)

        return Space(
            type=space.space_type.value,
            identifier=space.identifier,
            name=space.name,
            usage_id=space.usage_id,
            usage_text=space.usage_text,
            number=space.number,
            description=space.description,
            project_uid=space.project_uid,
            devices=space.devices,
            spaces=subspaces,
            functions=space.functions,
        )

    def convert_group_range(
        self, group_range: XMLGroupRange, group_address_style: GroupAddressStyle
    ) -> GroupRange:
        """Convert XMLGroupRange into GroupRange."""
        group_ranges: dict[str, GroupRange] = {}
        for child_gr in group_range.group_ranges:
            group_ranges[child_gr.str_address()] = self.convert_group_range(
                child_gr, group_address_style
            )

        return GroupRange(
            name=group_range.name,
            address_start=group_range.range_start,
            address_end=group_range.range_end,
            group_addresses=[
                XMLGroupAddress.str_address(ga, group_address_style)
                for ga in group_range.group_addresses
            ],
            comment=html.unescape(rtf_to_text(group_range.comment)),
            group_ranges=group_ranges,
        )

    def load(self, language: str | None) -> None:
        """Load XML files."""
        (
            knx_master_data,
            self.language_code,
        ) = KNXMasterLoader.load(
            knx_proj_contents=self.knx_proj_contents,
            knx_master_file=self.knx_proj_contents.root_path / "knx_master.xml",
            language=language,
        )
        (
            self.group_addresses,
            self.group_ranges,
            self.areas,
            self.devices,
            self.spaces,
            self.project_info,
            self.functions,
        ) = ProjectLoader.load(
            knx_proj_contents=self.knx_proj_contents,
            knx_master_data=knx_master_data,
        )

        products_dict: dict[str, Product] = {}
        hardware_application_map: HardwareToPrograms = {}
        for _products, _hardware_programs in [
            HardwareLoader.load(
                hardware_file=hardware_file,
                language_code=self.language_code,
            )
            for hardware_file in HardwareLoader.get_hardware_files(
                project_contents=self.knx_proj_contents
            )
        ]:
            products_dict.update(_products)
            hardware_application_map.update(_hardware_programs)

        for device in self.devices:
            device.manufacturer_name = knx_master_data.manufacturer_names.get(
                device.manufacturer, ""
            )

            try:
                product = products_dict[device.product_ref]
            except KeyError:
                _LOGGER.warning(
                    "Could not find hardware product for device %s with product_ref %s",
                    device.individual_address,
                    device.product_ref,
                )
                continue
            device.product_name = product.text
            device.hardware_name = product.hardware_name

            try:
                application_program_ref = hardware_application_map[
                    device.hardware_program_ref
                ]
            except KeyError:
                _LOGGER.warning(
                    "Could not find application_program_ref for device %s with hardware_program_ref %s",
                    device.individual_address,
                    device.hardware_program_ref,
                )
                continue
            device.application_program_ref = application_program_ref
            for com_object in device.com_object_instance_refs:
                com_object.resolve_com_object_ref_id(
                    application_program_ref, self.knx_proj_contents
                )

        application_programs = (
            ApplicationProgramLoader.get_application_program_files_for_devices(
                project_root_path=self.knx_proj_contents.root_path,
                devices=self.devices,
            )
        )
        # update self.devices items with its inherited values from their application programs
        for application_program_file, devices in application_programs.items():
            ApplicationProgramLoader.load(
                application_program_path=application_program_file,
                devices=devices,
                language_code=self.language_code,
            )
