import unittest
from huffman_compressor_analyzer import comprimir, generar_codigos, huffman_analysis

class HuffmanTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(comprimir(""), ("", None))
        self.assertEqual(huffman_analysis(""), "")

    def test_single_symbol_uses_bit(self):
        compressed, tree = comprimir("aaaaa")
        self.assertEqual(compressed, "00000")
        self.assertEqual(generar_codigos(tree), {"a": "0"})

    def test_no_mutable_dictionary_leak(self):
        _, tree_a = comprimir("aaa")
        _, tree_b = comprimir("bbb")
        self.assertEqual(generar_codigos(tree_a), {"a": "0"})
        self.assertEqual(generar_codigos(tree_b), {"b": "0"})

    def test_general_prefix_property(self):
        _, tree = comprimir("abracadabra")
        code = generar_codigos(tree)
        self.assertEqual(set(code), set("abracadabra"))
        for a in code:
            for b in code:
                if a != b:
                    self.assertFalse(code[b].startswith(code[a]))

if __name__ == "__main__":
    unittest.main()
