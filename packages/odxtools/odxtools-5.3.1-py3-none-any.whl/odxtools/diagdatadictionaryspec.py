# SPDX-License-Identifier: MIT
from dataclasses import dataclass
from itertools import chain
from typing import TYPE_CHECKING, Any, Dict, List, Optional
from xml.etree import ElementTree

from .basicstructure import BasicStructure
from .createanystructure import create_any_structure_from_et
from .createsdgs import create_sdgs_from_et
from .dataobjectproperty import DataObjectProperty
from .dtcdop import DtcDop
from .dynamiclengthfield import DynamicLengthField
from .endofpdufield import EndOfPduField
from .environmentdata import EnvironmentData
from .environmentdatadescription import EnvironmentDataDescription
from .exceptions import odxraise, odxrequire
from .globals import logger
from .multiplexer import Multiplexer
from .nameditemlist import NamedItemList
from .odxlink import OdxDocFragment, OdxLinkDatabase, OdxLinkId
from .specialdatagroup import SpecialDataGroup
from .table import Table
from .unitspec import UnitSpec

if TYPE_CHECKING:
    from .diaglayer import DiagLayer


@dataclass
class DiagDataDictionarySpec:
    dtc_dops: NamedItemList[DtcDop]
    data_object_props: NamedItemList[DataObjectProperty]
    structures: NamedItemList[BasicStructure]
    end_of_pdu_fields: NamedItemList[EndOfPduField]
    dynamic_length_fields: NamedItemList[DynamicLengthField]
    tables: NamedItemList[Table]
    env_data_descs: NamedItemList[EnvironmentDataDescription]
    env_datas: NamedItemList[EnvironmentData]
    muxs: NamedItemList[Multiplexer]
    unit_spec: Optional[UnitSpec]
    sdgs: List[SpecialDataGroup]

    def __post_init__(self):
        self._all_data_object_properties = NamedItemList(
            chain(
                self.data_object_props,
                self.structures,
                self.end_of_pdu_fields,
                self.dynamic_length_fields,
                self.dtc_dops,
                self.tables,
            ),)

    @staticmethod
    def from_et(et_element: ElementTree.Element,
                doc_frags: List[OdxDocFragment]) -> "DiagDataDictionarySpec":
        # Parse DOP-BASEs
        data_object_props = [
            DataObjectProperty.from_et(dop_element, doc_frags)
            for dop_element in et_element.iterfind("DATA-OBJECT-PROPS/DATA-OBJECT-PROP")
        ]

        structures = [
            odxrequire(create_any_structure_from_et(structure_element, doc_frags))
            for structure_element in et_element.iterfind("STRUCTURES/STRUCTURE")
        ]

        end_of_pdu_fields = [
            EndOfPduField.from_et(eofp_element, doc_frags)
            for eofp_element in et_element.iterfind("END-OF-PDU-FIELDS/END-OF-PDU-FIELD")
        ]

        dynamic_length_fields = [
            DynamicLengthField.from_et(dl_element, doc_frags)
            for dl_element in et_element.iterfind("DYNAMIC-LENGTH-FIELDS/DYNAMIC-LENGTH-FIELD")
        ]

        dtc_dops = []
        for dtc_dop_elem in et_element.iterfind("DTC-DOPS/DTC-DOP"):
            dtc_dop = DtcDop.from_et(dtc_dop_elem, doc_frags)
            if not isinstance(dtc_dop, DtcDop):
                odxraise()
            dtc_dops.append(dtc_dop)

        tables = [
            Table.from_et(table_element, doc_frags)
            for table_element in et_element.iterfind("TABLES/TABLE")
        ]

        env_data_descs = [
            EnvironmentDataDescription.from_et(env_data_desc_element, doc_frags)
            for env_data_desc_element in et_element.iterfind("ENV-DATA-DESCS/ENV-DATA-DESC")
        ]

        env_data_elements = chain(
            et_element.iterfind("ENV-DATAS/ENV-DATA"),
            # ODX 2.0.0 says ENV-DATA-DESC could contain a list of ENV-DATAS
            et_element.iterfind("ENV-DATA-DESCS/ENV-DATA-DESC/ENV-DATAS/ENV-DATA"),
        )
        env_datas = [
            EnvironmentData.from_et(env_data_element, doc_frags)
            for env_data_element in env_data_elements
        ]

        muxs = [
            Multiplexer.from_et(mux_element, doc_frags)
            for mux_element in et_element.iterfind("MUXS/MUX")
        ]

        if (spec_elem := et_element.find("UNIT-SPEC")) is not None:
            unit_spec = UnitSpec.from_et(spec_elem, doc_frags)
        else:
            unit_spec = None

        # TODO: Parse different specs.. Which of them are needed?
        for (path, name) in [
            ("STATIC-FIELDS", "static fields"),
            ("DYNAMIC-LENGTH-FIELDS/DYNAMIC-LENGTH-FIELD", "dynamic length fields"),
            (
                "DYNAMIC-ENDMARKER-FIELDS/DYNAMIC-ENDMARKER-FIELD",
                "dynamic endmarker fields",
            ),
        ]:
            num = len(list(et_element.iterfind(path)))
            if num > 0:
                logger.info(f"Not implemented: Did not parse {num} {name}.")

        sdgs = create_sdgs_from_et(et_element.find("SDGS"), doc_frags)

        return DiagDataDictionarySpec(
            data_object_props=NamedItemList(data_object_props),
            structures=NamedItemList(structures),
            end_of_pdu_fields=NamedItemList(end_of_pdu_fields),
            dynamic_length_fields=NamedItemList(dynamic_length_fields),
            dtc_dops=NamedItemList(dtc_dops),
            unit_spec=unit_spec,
            tables=NamedItemList(tables),
            env_data_descs=NamedItemList(env_data_descs),
            env_datas=NamedItemList(env_datas),
            muxs=NamedItemList(muxs),
            sdgs=sdgs,
        )

    def _build_odxlinks(self) -> Dict[OdxLinkId, Any]:
        # note that DataDictionarySpec objects do not exhibit an ODXLINK id.
        odxlinks = {}

        for obj in chain(
                self.data_object_props,
                self.dtc_dops,
                self.env_data_descs,
                self.env_datas,
                self.muxs,
                self.sdgs,
                self.structures,
                self.end_of_pdu_fields,
                self.dynamic_length_fields,
                self.tables,
        ):
            odxlinks.update(obj._build_odxlinks())

        if self.unit_spec is not None:
            odxlinks.update(self.unit_spec._build_odxlinks())

        return odxlinks

    def _resolve_odxlinks(self, odxlinks: OdxLinkDatabase) -> None:

        for obj in chain(self.data_object_props, self.dtc_dops, self.end_of_pdu_fields,
                         self.dynamic_length_fields, self.env_data_descs, self.env_datas, self.muxs,
                         self.sdgs, self.structures, self.tables):
            obj._resolve_odxlinks(odxlinks)

        if self.unit_spec is not None:
            self.unit_spec._resolve_odxlinks(odxlinks)

    def _resolve_snrefs(self, diag_layer: "DiagLayer") -> None:
        for obj in chain(self.data_object_props, self.dtc_dops, self.end_of_pdu_fields,
                         self.dynamic_length_fields, self.env_data_descs, self.env_datas, self.muxs,
                         self.sdgs, self.structures, self.tables):
            obj._resolve_snrefs(diag_layer)

        if self.unit_spec is not None:
            self.unit_spec._resolve_snrefs(diag_layer)

    @property
    def all_data_object_properties(self):
        return self._all_data_object_properties
