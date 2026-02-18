from unittest.mock import patch
from app.main import cryptocurrency_action


def test_recommends_buy_when_prediction_over_5_percent_higher() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 1.6
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_recommends_buy_when_prediction_over_5_percent_lower() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 1
        assert cryptocurrency_action(1.6) == "Sell all your cryptocurrency"


def test_recommends_buy_when_prediction_is_the_same() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 1
        assert cryptocurrency_action(1) == "Do nothing"
