import argparse
import json
import sys
from pathlib import Path
from typing import Any, List, Optional, Sequence, Union

import warnings


class Kwargs:
    def __init__(self):
        self.type = None
        self.default: Any = None
        self.required: bool = False
        self.help: Optional[str] = None
        self.action: Optional[str] = None
        self.choices: Optional[list] = None
        self.dest: Optional[str] = None


_deprecated_default = object()


def generate_action(*, true_prefix, false_prefix):
    if not true_prefix and not false_prefix:
        return 'store_true'

    class PrefixBooleanAction(argparse.Action):
        # pylint: disable=too-many-arguments
        def __init__(self,
                     option_strings,
                     dest,
                     default=None,
                     type=_deprecated_default,  # pylint: disable=redefined-builtin
                     choices=_deprecated_default,
                     required=False,
                     help=None,  # pylint: disable=redefined-builtin
                     metavar=_deprecated_default):
            _option_strings = []
            self.true_prefix = true_prefix
            self.false_prefix = false_prefix
            for option_string in option_strings:

                if option_string.startswith('--'):
                    if true_prefix:
                        _option_strings.append(f'--{self.true_prefix}-' + option_string[2:])
                    if false_prefix:
                        _option_strings.append(f'--{self.false_prefix}-' + option_string[2:])

            # We need `_deprecated` special value to ban explicit arguments that
            # match default value. Like:
            #   parser.add_argument('-f', action=BooleanOptionalAction, type=int)
            for field_name in ('type', 'choices', 'metavar'):
                if locals()[field_name] is not _deprecated_default:
                    remove = (3, 14)
                    warnings.warn(
                        f"{field_name!r} is deprecated as of Python 3.12 and will be "
                        f"removed in Python {remove}.",
                        DeprecationWarning
                    )

            if type is _deprecated_default:
                type = None
            if choices is _deprecated_default:
                choices = None
            if metavar is _deprecated_default:
                metavar = None

            super().__init__(
                option_strings=_option_strings,
                dest=dest,
                nargs=0,
                default=default,
                type=type,
                choices=choices,
                required=required,
                help=help,
                metavar=metavar)

        def __call__(self, parser, namespace, values, option_string=None):
            if option_string in self.option_strings:
                setattr(
                    namespace,
                    self.dest,
                    not option_string.startswith(f'--{self.false_prefix}-')
                )

        def format_usage(self):
            return ' | '.join(self.option_strings)
    return PrefixBooleanAction


def load_schema(schema: Union[dict, str, Path]) -> dict:
    if not isinstance(schema, dict):
        with open(str(schema), 'r', encoding="utf8") as schema_file:
            schema: dict = json.load(schema_file)
    return schema


def _extract_item_type_from_composition(composition: dict) -> List[str]:
    result = []
    for item in composition:
        _type = item.get('type')
        if _type == "null":
            continue
        result.extend(_type)
    return result


def _check_same_element(items: List[str]) -> bool:
    return len(set(items)) == 1


def _check_composition(value: dict, compositions: List[str]) -> bool:
    return any(key in compositions for key in value.keys())


def _get_composition(value: dict, compositions: List[str]) -> str:
    for key in value.keys():
        if key in compositions:
            return key
    return None


def get_parser(schema: Union[dict, str, Path]) -> argparse.ArgumentParser:
    schema = load_schema(schema)
    assert 'type' in schema and schema['type'] == 'object'
    assert 'properties' in schema

    required_set = set(schema.get('required', []))

    type_map = {
        'string': str,
        'integer': int,
        'number': float,
        'boolean': bool
    }

    composition_type_list = [
        "anyOf",
        "allOf",
        "oneOf"
    ]

    unsupported_composition_type_list = [
        "not"
    ]

    parser = argparse.ArgumentParser(description=schema.get('description'))
    for name, value in schema.get('properties', {}).items():
        assert isinstance(value, dict)

        kwargs = Kwargs()
        kwargs.default = value.get('default')
        kwargs.help = value.get('description')
        kwargs.required = name in required_set

        if kwargs.default is not None:
            kwargs.help = f'{kwargs.help}, [{kwargs.default}] in default'

        assert not _check_composition(value, unsupported_composition_type_list), \
            f"Composition type {value.get('type')} is not supported"

        if 'enum' in value:
            enum_list = value['enum']
            assert len(enum_list) > 0, "Enum List is Empty"
            arg_type = type(enum_list[0])
            assert all(arg_type is type(item) for item in enum_list), \
                f"Items in [{enum_list}] with Different Types"

            kwargs.type = arg_type
            kwargs.choices = enum_list
        elif _check_composition(value, composition_type_list):
            assert _check_same_element(value) == 1, \
                "Items in composition must be same type except for \"null\""
            value = value.get(_get_composition(value, composition_type_list))[0]
            kwargs.type = type_map[value.get('type')]
            del kwargs.choices
        else:
            kwargs.type = type_map[value.get('type')]
            del kwargs.choices

        if kwargs.type is bool:
            if not kwargs.default:
                kwargs.default = False
            kwargs.action = generate_action(
                true_prefix=value.get('true-prefix'),
                false_prefix=value.get('false-prefix')
            )
            del kwargs.type
        else:
            del kwargs.action

        positional = value.get('positional')
        if positional:
            del kwargs.required
            del kwargs.dest
        else:
            name = f'--{name}'

        parser.add_argument(name, **vars(kwargs))
    return parser


def parse(schema: Union[dict, str, Path], args: Optional[Sequence[str]] = None) -> dict:
    return vars(get_parser(schema).parse_args(args=args))


def main():  # pragma: no cover
    schema_path = parse(schema={
        'type': 'object',
        'properties': {
            'schema_path': {
                'type': 'string',
                'positional': True,
                'description': 'argparse schema file path'
            }
        },
        'required': [
            'schema_path'
        ],
    })['schema_path']

    sys.argv[0] = 'YOUR-COMMAND'
    print(f'Show help for schema file [{schema_path}]:')
    parse(schema=schema_path, args=['-h'])


if __name__ == '__main__':  # pragma: no cover
    main()
