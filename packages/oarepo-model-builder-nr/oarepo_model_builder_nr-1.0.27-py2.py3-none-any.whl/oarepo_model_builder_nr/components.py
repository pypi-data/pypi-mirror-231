from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components.model import DefaultsModelComponent, RecordModelComponent, RecordDumperModelComponent

class NrSyntheticFieldsComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [DefaultsModelComponent, RecordModelComponent, RecordDumperModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        datatype.definition["record"]["imports"].append({
            "import": "nr_metadata.extensions.facets.dumper.SyntheticFieldsDumperExtension"
        })
        
        datatype.definition["record-dumper"]["extensions"].append("SyntheticFieldsDumperExtension()")
        
COMPONENTS = [
    NrSyntheticFieldsComponent
]