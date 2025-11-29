![delayed_action](https://github.com/bhuebschen/delayed_action/assets/1864448/fe84a672-b572-46ca-bb7e-73f236ab4306)

# Delayed Action Home Assistant Integration

[![hacs][hacs-image]][hacs-url]
[![GitHub Sponsors][gh-sponsors-image]][gh-sponsors-url]

The `delayed_action` integration allows you to schedule actions for Home Assistant entities with a delay or at a specific time. This integration supports various entities and actions, providing flexibility in controlling your devices.

*** WORKS IN BEST COMBINATION WITH [DELAYED-ACTION-CARD](https://github.com/bhuebschen/delayed-action-card) ***

## Features

- Schedule actions with a delay (in seconds).
- Schedule actions at a specific date and time (ISO 8601 format).
- Pass additional data to the actions.

## Installation:

### [HACS](hacs) (Home Assistant Community Store)

1. Go to HACS page on your Home Assistant instance
1. Add this repository (https://github.com/bhuebschen/delayed_action) via HACS Custom repositories [How to add Custom Repositories](https://hacs.xyz/docs/faq/custom_repositories/)
1. Select `Integration`
1. Press add icon and search for `Delayed Action`
1. Select Delayed Action repo and install,
1. Restart Home Assistant
1. Add delayed_action to your page

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=bhuebschen&repository=delayed_action&category=integration)

### Manual

1. Ensure your Home Assistant configuration directory has the following structure:

```
/config/custom_components/delayed_action/
├── init.py
├── manifest.json
├── config_flow.py
├── const.py
└── services.yaml
    ├── translations/de.json
    └── translations/en.json
```

2. Copy the provided files into the `custom_components/delayed_action/` directory.
3. Restart Home Assistant to load the new custom component.

## Configuration

1. Go to **Configuration** -> **Devices & Services**.
1. Click on the "+" button and add the "Delayed Action" integration.

## Usage

You can use the `delayed_action.execute` service to schedule actions with a delay or at a specific time.

### Service Data Attributes

**Required:**
- `entity_id`: The entity ID of the device to control.
- `action`: The action to perform (e.g., `turn_on`, `turn_off`, `set_brightness`, `set_temperature`).

**Timing (one required):**
- `delay`: The delay in seconds before performing the action.
- `datetime`: The specific date and time to perform the action (ISO 8601 format).

**UI-Configurable Action Parameters:**

These parameters can be configured directly in the Home Assistant UI when calling the service:

| Parameter | Description | Applicable Entities |
|-----------|-------------|---------------------|
| `brightness` | Brightness level (0-255) | Lights |
| `brightness_pct` | Brightness percentage (0-100%) | Lights |
| `color_temp` | Color temperature in mireds | Lights |
| `rgb_color` | RGB color [R, G, B] | Lights |
| `temperature` | Target temperature | Climate |
| `hvac_mode` | HVAC mode (heat, cool, auto, etc.) | Climate |
| `position` | Cover position (0-100%) | Covers |
| `tilt_position` | Tilt position (0-100%) | Covers |
| `volume_level` | Volume level (0.0-1.0) | Media Players |
| `media_content_id` | Media content ID | Media Players |
| `media_content_type` | Media content type | Media Players |
| `option` | Option to select | Input Select, Select |
| `percentage` | Fan speed percentage (0-100%) | Fans |
| `humidity` | Target humidity (0-100%) | Humidifiers |

**Advanced:**
- `data`: Any additional data to be passed to the service call as a dictionary (for advanced use cases).

### Examples

#### Script: Turn On with Delay

```yaml
script:
  turn_on_with_delay:
    sequence:
      - service: delayed_action.execute
        data:
          entity_id: switch.any_switch
          delay: 10  # Delay in seconds
          action: turn_on
```

#### Script: Set Brightness with Delay

```yaml
script:
  set_brightness_with_delay:
    sequence:
      - service: delayed_action.execute
        data:
          entity_id: light.any_light
          delay: 15  # Delay in seconds
          action: turn_on
          brightness: 128
```

#### Script: Set Climate Temperature with Delay

```yaml
script:
  set_temperature_with_delay:
    sequence:
      - service: delayed_action.execute
        data:
          entity_id: climate.living_room
          delay: 60  # Delay in seconds
          action: set_temperature
          temperature: 22
          hvac_mode: heat
```

#### Script: Set Cover Position at Specific Time

```yaml
script:
  close_blinds_at_sunset:
    sequence:
      - service: delayed_action.execute
        data:
          entity_id: cover.living_room_blinds
          datetime: "2024-06-23T20:00:00"
          action: set_cover_position
          position: 0
```

## Development

To develop and test this integration:

1. Clone the repository into your Home Assistant `custom_components` directory.
2. Make changes to the code as needed.
3. Restart Home Assistant to apply the changes.

## Troubleshooting

If you encounter issues, check the Home Assistant logs for error messages. Common issues include:

- Ensuring the `entity_id` is correct and exists.
- Verifying the `action` is supported for the specified entity.
- Confirming the date and time are in the correct format.

For more information on Home Assistant custom components, visit the [Home Assistant Developer Documentation](https://developers.home-assistant.io/docs/creating_integration_file_structure).

## Contributing

Contributions are welcome! Please submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

<!-- Badges -->

[hacs-url]: https://github.com/hacs/integration
[hacs-image]: https://img.shields.io/badge/hacs-custom-orange.svg?style=flat-square
[gh-sponsors-url]: https://github.com/sponsors/bhuebschen
[gh-sponsors-image]: https://img.shields.io/github/sponsors/bhuebschen?style=flat-square

<!-- References -->

[home-assistant]: https://www.home-assistant.io/
[hacs]: https://hacs.xyz
[latest-release]: https://github.com/bhuebschen/delayed_action/releases/latest
[ha-scripts]: https://www.home-assistant.io/docs/scripts/
[edit-readme]: https://github.com/bhuebschen/delayed_action/edit/master/README.md
