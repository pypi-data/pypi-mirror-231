import re
from typing import List, Optional, Set

from starlette.datastructures import FormData

from strictdoc.backend.sdoc.models.document import Document
from strictdoc.backend.sdoc.models.document_grammar import (
    DocumentGrammar,
    GrammarElement,
)
from strictdoc.backend.sdoc.models.type_system import (
    GrammarElementField,
    GrammarElementFieldString,
    RequirementFieldName,
)
from strictdoc.helpers.auto_described import auto_described
from strictdoc.server.error_object import ErrorObject


def is_reserved_field(field_name: str):
    return field_name in (
        RequirementFieldName.UID,
        RequirementFieldName.REFS,
        RequirementFieldName.TITLE,
        RequirementFieldName.STATEMENT,
        RequirementFieldName.RATIONALE,
        RequirementFieldName.COMMENT,
    )


@auto_described
class GrammarFormField:
    def __init__(
        self,
        field_name: str,
        previous_name: Optional[str],
        field_required: bool,
        reserved: bool,
    ):
        self.field_name: str = field_name
        self.previous_name: Optional[str] = previous_name
        self.field_required: bool = field_required
        self.reserved: bool = reserved

    @staticmethod
    def create_from_grammar_field(*, grammar_field: GrammarElementField):
        reserved = is_reserved_field(grammar_field.title)
        return GrammarFormField(
            field_name=grammar_field.title,
            previous_name=grammar_field.title,
            field_required=grammar_field.required,
            reserved=reserved,
        )

    @property
    def field_input_name(self):
        return f"document_grammar[{self.field_name}]"


@auto_described
class DocumentGrammarFormObject(ErrorObject):
    def __init__(
        self,
        *,
        document_mid: str,
        fields: List[GrammarFormField],
    ):
        assert isinstance(document_mid, str), document_mid
        super().__init__()
        self.document_mid = document_mid
        self.fields: List[GrammarFormField] = fields

    @staticmethod
    def create_from_request(
        *, document_mid: str, request_form_data: FormData
    ) -> "DocumentGrammarFormObject":
        # For now, the convention is that the new fields have empty
        # brackets, e.g., ('document_grammar[]', 'CUSTOM_FIELD_1').
        # The existing fields are:
        # ('document_grammar[RATIONALE]', 'RATIONALE')  # noqa: ERA001
        # This structure will be changed when not just field names, but also
        # their options will be passed to this parser.
        form_object_fields = []

        for field_name, field_value in request_form_data.multi_items():
            result = re.search(r"^document_grammar\[(.*)]$", field_name)
            if result is not None:
                previous_name: Optional[str] = None
                if len(result.group(1)) > 0:
                    previous_name = result.group(1)
                form_object_field = GrammarFormField(
                    field_name=field_value,
                    previous_name=previous_name,
                    field_required=False,
                    reserved=is_reserved_field(field_value),
                )
                form_object_fields.append(form_object_field)

        form_object = DocumentGrammarFormObject(
            document_mid=document_mid,
            fields=form_object_fields,
        )
        return form_object

    @staticmethod
    def create_from_document(
        *, document: Document
    ) -> "DocumentGrammarFormObject":
        assert isinstance(document, Document)
        assert isinstance(document.grammar, DocumentGrammar)

        grammar: DocumentGrammar = document.grammar
        element: GrammarElement = grammar.elements_by_type["REQUIREMENT"]

        grammar_form_fields: List[GrammarFormField] = []
        for grammar_field in element.fields:
            grammar_form_field = GrammarFormField.create_from_grammar_field(
                grammar_field=grammar_field
            )
            grammar_form_fields.append(grammar_form_field)
        return DocumentGrammarFormObject(
            document_mid=document.mid.get_string_value(),
            fields=grammar_form_fields,
        )

    def validate(self) -> bool:
        fields_so_far: Set[str] = set()
        for field in self.fields:
            if len(field.field_name) == 0:
                self.add_error(
                    field.field_name,
                    f"Grammar field {field.field_name} must not be empty.",
                )
                continue

            if field.field_name in fields_so_far:
                self.add_error(
                    field.field_name,
                    f"Grammar field {field.field_name} is not unique.",
                )
            else:
                fields_so_far.add(field.field_name)
        return len(self.errors) == 0

    def convert_to_document_grammar(self) -> DocumentGrammar:
        grammar_fields = []
        for field in self.fields:
            grammar_field = GrammarElementFieldString(
                parent=None,
                title=field.field_name,
                required="True" if field.field_required else "False",
            )
            grammar_fields.append(grammar_field)
        requirement_element = GrammarElement(
            parent=None, tag="REQUIREMENT", fields=grammar_fields
        )
        elements: List[GrammarElement] = [requirement_element]
        grammar = DocumentGrammar(parent=None, elements=elements)
        grammar.is_default = False
        return grammar
