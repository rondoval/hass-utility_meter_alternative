"""Constants for the utility meter component."""
DOMAIN = "utility_meter"

QUARTER_HOURLY = "quarter-hourly"
HOURLY = "hourly"
DAILY = "daily"
WEEKLY = "weekly"
MONTHLY = "monthly"
BIMONTHLY = "bimonthly"
QUARTERLY = "quarterly"
YEARLY = "yearly"

METER_TYPES = [
    QUARTER_HOURLY,
    HOURLY,
    DAILY,
    WEEKLY,
    MONTHLY,
    BIMONTHLY,
    QUARTERLY,
    YEARLY,
]

DEFAULT = "default"
ALTERNATE = "alt"

METER_MODES =  [
    DEFAULT,
    ALTERNATE,
]

DATA_UTILITY = "utility_meter_data"

CONF_METER = "meter"
CONF_SOURCE_SENSOR = "source"
CONF_METER_TYPE = "cycle"
CONF_METER_MODE = "mode"
CONF_METER_OFFSET = "offset"
CONF_METER_NET_CONSUMPTION = "net_consumption"
CONF_PAUSED = "paused"
CONF_TARIFFS = "tariffs"
CONF_TARIFF = "tariff"
CONF_TARIFF_ENTITY = "tariff_entity"

ATTR_TARIFF = "tariff"
ATTR_VALUE = "value"

SIGNAL_START_PAUSE_METER = "utility_meter_start_pause"
SIGNAL_RESET_METER = "utility_meter_reset"

SERVICE_RESET = "reset"
SERVICE_SELECT_TARIFF = "select_tariff"
SERVICE_SELECT_NEXT_TARIFF = "next_tariff"
SERVICE_CALIBRATE_METER = "calibrate"