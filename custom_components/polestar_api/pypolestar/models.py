from dataclasses import dataclass
from datetime import date, datetime
from enum import StrEnum
from typing import Self

from .utils import (
    GqlDict,
    get_field_name_date,
    get_field_name_datetime,
    get_field_name_float,
    get_field_name_int,
    get_field_name_str,
)


class ChargingConnectionStatus(StrEnum):
    CHARGER_CONNECTION_STATUS_CONNECTED = "Connected"
    CHARGER_CONNECTION_STATUS_DISCONNECTED = "Disconnected"
    CHARGER_CONNECTION_STATUS_FAULT = "Fault"
    CHARGER_CONNECTION_STATUS_UNSPECIFIED = "Unspecified"


class ChargingStatus(StrEnum):
    CHARGING_STATUS_DONE = "Done"
    CHARGING_STATUS_IDLE = "Idle"
    CHARGING_STATUS_CHARGING = "Charging"
    CHARGING_STATUS_FAULT = "Fault"
    CHARGING_STATUS_UNSPECIFIED = "Unspecified"
    CHARGING_STATUS_SCHEDULED = "Scheduled"
    CHARGING_STATUS_DISCHARGING = "Discharging"
    CHARGING_STATUS_ERROR = "Error"
    CHARGING_STATUS_SMART_CHARGING = "Smart Charging"


@dataclass(frozen=True)
class CarInformation:
    vin: str | None
    internal_vehicle_identifier: str | None
    registration_no: str | None
    registration_date: date | None
    factory_complete_date: date | None
    image_url: str | None
    battery: str | None
    torque: str | None
    software_version: str | None

    @classmethod
    def from_dict(cls, data: GqlDict) -> Self:
        return cls(
            vin=get_field_name_str("vin", data),
            internal_vehicle_identifier=get_field_name_str(
                "internalVehicleIdentifier", data
            ),
            registration_no=get_field_name_str("registrationNo", data),
            registration_date=get_field_name_date("registrationDate", data),
            factory_complete_date=get_field_name_date("factoryCompleteDate", data),
            image_url=get_field_name_str("content/images/studio/url", data),
            battery=get_field_name_str("content/specification/battery", data),
            torque=get_field_name_str("content/specification/torque", data),
            software_version=get_field_name_str("software/version", data),
        )


@dataclass(frozen=True)
class CarOdometerData:
    average_speed_km_per_hour: float | None
    odometer_meters: int | None
    trip_meter_automatic_km: int | None
    trip_meter_manual_km: int | None
    event_update_timestamp: datetime | None

    @classmethod
    def from_dict(cls, data: GqlDict) -> Self:
        return cls(
            average_speed_km_per_hour=get_field_name_float(
                "averageSpeedKmPerHour", data
            ),
            odometer_meters=get_field_name_int("odometerMeters", data),
            trip_meter_automatic_km=get_field_name_int("tripMeterAutomaticKm", data),
            trip_meter_manual_km=get_field_name_int("tripMeterManualKm", data),
            event_update_timestamp=get_field_name_datetime(
                "eventUpdatedTimestamp/iso", data
            ),
        )


@dataclass(frozen=True)
class CarBatteryData:
    average_energy_consumption_kwh_per_100km: float | None
    battery_charge_level_percentage: int | None
    charger_connection_status: ChargingConnectionStatus
    charging_current_amps: int | None
    charging_power_watts: int | None
    charging_status: ChargingStatus
    estimated_charging_time_minutes_to_target_distance: int | None
    estimated_charging_time_to_full_minutes: int | None
    estimated_distance_to_empty_km: int | None
    event_update_timestamp: datetime | None

    @classmethod
    def from_dict(cls, data: GqlDict) -> Self:
        return cls(
            average_energy_consumption_kwh_per_100km=get_field_name_float(
                "averageEnergyConsumptionKwhPer100Km", data
            ),
            battery_charge_level_percentage=get_field_name_int(
                "batteryChargeLevelPercentage", data
            ),
            charger_connection_status=ChargingConnectionStatus[
                str(get_field_name_str("chargerConnectionStatus", data))
            ],
            charging_current_amps=get_field_name_int("chargingCurrentAmps", data),
            charging_power_watts=get_field_name_int("chargingPowerWatts", data),
            charging_status=ChargingStatus[
                str(get_field_name_str("chargingStatus", data))
            ],
            estimated_charging_time_minutes_to_target_distance=get_field_name_int(
                "estimatedChargingTimeMinutesToTargetDistance", data
            ),
            estimated_charging_time_to_full_minutes=get_field_name_int(
                "estimatedChargingTimeToFullMinutes", data
            ),
            estimated_distance_to_empty_km=get_field_name_int(
                "estimatedDistanceToEmptyKm", data
            ),
            event_update_timestamp=get_field_name_datetime(
                "eventUpdatedTimestamp/iso", data
            ),
        )
