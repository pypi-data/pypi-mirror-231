import unittest
from pathlib import Path

import jsonschema

import argparse_from_jsonschema


class MyTestCase(unittest.TestCase):
    def test_argparse_schema(self):
        schema_path = Path(__file__).parent / 'argument_config.json'

        result = argparse_from_jsonschema.parse(schema_path, [
            '/path/to/config',
            '--resume',
            '--scale', '2.0'
        ])
        self.assertEqual(result, {
            'config': '/path/to/config',
            'resume': True,
            'foo': False,
            'scale': 2.0,
            'mode': 'happy'
        })

    def test_argparse_schema_without_boolean(self):
        schema_path = Path(__file__).parent / 'argument_config.json'
        result = argparse_from_jsonschema.parse(schema_path, [
            '/path/to/config',
            '--mode',
            'high'
        ])
        self.assertEqual(result, {
            'config': '/path/to/config',
            'resume': False,
            'foo': False,
            'scale': 1.0,
            'mode': 'high'
        })

    def test_argparse_schema_false_prefix(self):
        schema_path = Path(__file__).parent / 'argument_config.json'
        result = argparse_from_jsonschema.parse(schema_path, [
            '/path/to/config',
            '--no-foo',
        ])
        self.assertEqual(result, {
            'config': '/path/to/config',
            'resume': False,
            'foo': False,
            'scale': 1.0,
            'mode': 'happy'
        })

    def test_argparse_schema_true_prefix(self):
        schema_path = Path(__file__).parent / 'argument_config.json'
        result = argparse_from_jsonschema.parse(schema_path, [
            '/path/to/config',
            '--with-foo',
        ])
        self.assertEqual(result, {
            'config': '/path/to/config',
            'resume': False,
            'foo': True,
            'scale': 1.0,
            'mode': 'happy'
        })

    def test_argparse_schema_composition(self):
        schema_path = Path(__file__).parent / 'composition_config.json'
        result = argparse_from_jsonschema.parse(schema_path, [
            '--config',
            '/path/to/config',
        ])
        self.assertEqual(result, {
            'config': '/path/to/config'
        })
        jsonschema.validate(result,
                            argparse_from_jsonschema.load_schema(schema_path))
        result = argparse_from_jsonschema.parse(schema_path, [])
        self.assertEqual(result, {
            'config': None
        })
        jsonschema.validate(result,
                            argparse_from_jsonschema.load_schema(schema_path))

    def test_argparse_schema_unsupported_composition(self):
        schema_path = Path(__file__).parent / 'unsupported_composition.json'
        with self.assertRaises(AssertionError):
            argparse_from_jsonschema.parse(schema_path, [
                '--config',
                '/path/to/config',
            ])


#    def test_argparse_schema_true_prefix(self):
#        schema_path = Path(__file__).parent / 'argument_config.json'
#        with self.assertRaisesRegex(argparse.ArgumentError, 'unrecognized arguments: --foo'):
#            argparse_from_jsonschema.parse(schema_path, [
#                '/path/to/config',
#                '--foo',
#            ])

if __name__ == '__main__':
    unittest.main()
