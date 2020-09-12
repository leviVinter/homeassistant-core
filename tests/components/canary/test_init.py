"""The tests for the Canary component."""
from unittest.mock import patch

from homeassistant.components.canary import DOMAIN
from homeassistant.setup import setup_component


def test_setup_with_valid_config(hass, canary) -> None:
    """Test setup with valid YAML."""
    assert setup_component(hass, "persistent_notification", {})
    config = {DOMAIN: {"username": "test-username", "password": "test-password"}}

    with patch(
        "homeassistant.components.canary.alarm_control_panel.setup_platform",
        return_value=True,
    ), patch(
        "homeassistant.components.canary.camera.setup_platform",
        return_value=True,
    ), patch(
        "homeassistant.components.canary.sensor.setup_platform",
        return_value=True,
    ):
        assert setup_component(hass, DOMAIN, config)
        hass.block_till_done()
