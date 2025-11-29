DOMAIN = "delayed_action"
ATTR_ENTITY_ID = "entity_id"
ATTR_DELAY = "delay"
ATTR_ACTION = "action"
ATTR_DATETIME = "datetime"
ATTR_ADDITIONAL_DATA = "data"
ATTR_TASK_ID = "task_id"
CONF_DOMAINS = "domains"
ATTR_DOMAINS = ["automation", "climate", "cover", "fan", "humidifier", "input_boolean", "input_select", "lawn_mower", "light", "lock", "media_player", "scene", "script", "select", "switch", "vacuum", "water_heater"]

# UI-configurable action parameters
ATTR_BRIGHTNESS = "brightness"
ATTR_BRIGHTNESS_PCT = "brightness_pct"
ATTR_COLOR_TEMP = "color_temp"
ATTR_RGB_COLOR = "rgb_color"
ATTR_TEMPERATURE = "temperature"
ATTR_HVAC_MODE = "hvac_mode"
ATTR_POSITION = "position"
ATTR_TILT_POSITION = "tilt_position"
ATTR_VOLUME_LEVEL = "volume_level"
ATTR_MEDIA_CONTENT_ID = "media_content_id"
ATTR_MEDIA_CONTENT_TYPE = "media_content_type"
ATTR_OPTION = "option"
ATTR_PERCENTAGE = "percentage"
ATTR_HUMIDITY = "humidity"

# List of all UI-configurable parameters that should be passed to the service call
UI_ACTION_PARAMS = [
    ATTR_BRIGHTNESS,
    ATTR_BRIGHTNESS_PCT,
    ATTR_COLOR_TEMP,
    ATTR_RGB_COLOR,
    ATTR_TEMPERATURE,
    ATTR_HVAC_MODE,
    ATTR_POSITION,
    ATTR_TILT_POSITION,
    ATTR_VOLUME_LEVEL,
    ATTR_MEDIA_CONTENT_ID,
    ATTR_MEDIA_CONTENT_TYPE,
    ATTR_OPTION,
    ATTR_PERCENTAGE,
    ATTR_HUMIDITY,
]