import unittest
from unittest.mock import MagicMock
from main import consultar_llm

class TestResumo(unittest.TestCase):
    def test_consultar_llm_resposta_simulada(self):
        cliente_falso = MagicMock()
        cliente_falso.models.generate_content.return_value.text = "Este é um resumo de mentira para o teste."
        resultado = consultar_llm(cliente_falso, "Mensagem gigante do aluno", "modelo-falso")
        self.assertEqual(resultado, "Este é um resumo de mentira para o teste.")

if __name__ == "__main__":
    unittest.main()
