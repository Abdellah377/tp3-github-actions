import pytest
from app.texte import nettoyer_texte

@pytest.mark.parametrize("entree, attendu", [
    (" BONJOUR monde ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("PYTHON", "python")
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu

@pytest.mark.parametrize("entree", [123, None])
def test_texte_invalide(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)