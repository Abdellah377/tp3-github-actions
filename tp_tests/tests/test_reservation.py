import pytest
from app.reservation import Stock, Reservation

@pytest.fixture
def stock():
    return Stock(5)

def test_reservation_reussie(stock):
    reservation = Reservation(stock)

    resultat = reservation.reserver(2)

    assert resultat == "confirmee"
    assert stock.quantite == 3
    
def test_reservation_refusee(stock):
    reservation = Reservation(stock)

    resultat = reservation.reserver(6)

    assert resultat == "refusee"
    assert stock.quantite == 5
    
def test_reservation_complete(stock):
    reservation = Reservation(stock)

    resultat = reservation.reserver(5)

    assert resultat == "confirmee"
    assert stock.quantite == 0
    
def test_reservation_quantite_nulle(stock):
    reservation = Reservation(stock)

    with pytest.raises(ValueError):
        reservation.reserver(0)

    assert stock.quantite == 5