import configparser
import os
from utils.constants import *


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()

        # Check if the config file exists, if not create it
        if not os.path.exists(config_file):
            self.create_default_config()

        self.config.read(config_file)

        # Javier's speeds
        self.JAVIER_SPEED = self.config.getint("JavierSpeeds", JAVIER_SPEED_CONFIG)
        self.JAVIER_SPEED_BAD_SHAPE = self.config.getint(
            "JavierSpeeds", JAVIER_SPEED_BAD_SHAPE_CONFIG
        )
        self.JAVIER_SPEED_C51 = self.config.getint(
            "JavierSpeeds", JAVIER_SPEED_C51_CONFIG
        )
        self.ANDREINA_PACE_DIFFERENCE = self.config.getint(
            "JavierSpeeds", ANDREINA_PACE_DIFFERENCE_CONFIG
        )

        # Andreina's speeds
        self.ANDREINA_SPEED = self.JAVIER_SPEED + self.ANDREINA_PACE_DIFFERENCE
        self.ANDREINA_SPEED_BAD_SHAPE = (
            self.JAVIER_SPEED_BAD_SHAPE + self.ANDREINA_PACE_DIFFERENCE
        )
        self.ANDREINA_SPEED_C51 = self.JAVIER_SPEED_C51 + self.ANDREINA_PACE_DIFFERENCE

        # Graph Constants
        self.GRAPH_SIZE = self.config.getint("GraphConstants", GRAPH_SIZE_CONFIG)
        self.FIRST_AVENUE = self.config.getint("GraphConstants", FIRST_AVENUE_CONFIG)
        self.LAST_AVENUE = self.config.getint("GraphConstants", LAST_AVENUE_CONFIG)
        self.FIRST_STREET = self.config.getint("GraphConstants", FIRST_STREET_CONFIG)
        self.LAST_STREET = self.config.getint("GraphConstants", LAST_STREET_CONFIG)

        # Edge Constants
        self.BEGINNING_AVENUE_BAD_SHAPE = self.config.getint(
            "EdgeConstants", BEGINNING_AVENUE_BAD_SHAPE_CONFIG
        )
        self.END_AVENUE_BAD_SHAPE = self.config.getint(
            "EdgeConstants", END_AVENUE_BAD_SHAPE_CONFIG
        )
        self.HIGH_TRAFFIC_STREET = self.config.getint(
            "EdgeConstants", HIGH_TRAFFIC_STREET_CONFIG
        )

        # Important Locations
        self.JAVIER_HOME = tuple(
            map(
                int,
                self.config.get("ImportantLocations", JAVIER_HOME_CONFIG)
                .strip("()")
                .split(","),
            )
        )
        self.ANDREINA_HOME = tuple(
            map(
                int,
                self.config.get("ImportantLocations", ANDREINA_HOME_CONFIG)
                .strip("()")
                .split(","),
            )
        )
        self.THE_DARKNESS_CLUB = tuple(
            map(
                int,
                self.config.get("ImportantLocations", THE_DARKNESS_CLUB_CONFIG)
                .strip("()")
                .split(","),
            )
        )
        self.LA_PASION_BAR = tuple(
            map(
                int,
                self.config.get("ImportantLocations", LA_PASION_BAR_CONFIG)
                .strip("()")
                .split(","),
            )
        )
        self.MI_ROLITA_BREWERY = tuple(
            map(
                int,
                self.config.get("ImportantLocations", MI_ROLITA_BREWERY_CONFIG)
                .strip("()")
                .split(","),
            )
        )
        self.LOCATION_MAP = {
            JAVIER_HOME_CONFIG: JAVIER_HOME_STR,
            ANDREINA_HOME_CONFIG: ANDREINA_HOME_STR,
            THE_DARKNESS_CLUB_CONFIG: THE_DARKNESS_CLUB_STR,
            LA_PASION_BAR_CONFIG: LA_PASION_BAR_STR,
            MI_ROLITA_BREWERY_CONFIG: MI_ROLITA_BREWERY_STR,
        }

    def create_default_config(self):
        self.config["JavierSpeeds"] = {
            JAVIER_SPEED_CONFIG: "4",
            JAVIER_SPEED_BAD_SHAPE_CONFIG: "6",
            JAVIER_SPEED_C51_CONFIG: "8",
            ANDREINA_PACE_DIFFERENCE_CONFIG: "2",
        }

        self.config["GraphConstants"] = {
            GRAPH_SIZE_CONFIG: "36",
            FIRST_AVENUE_CONFIG: "10",
            LAST_AVENUE_CONFIG: "15",
            FIRST_STREET_CONFIG: "50",
            LAST_STREET_CONFIG: "55",
        }

        self.config["EdgeConstants"] = {
            BEGINNING_AVENUE_BAD_SHAPE_CONFIG: "12",
            END_AVENUE_BAD_SHAPE_CONFIG: "14",
            HIGH_TRAFFIC_STREET_CONFIG: "51",
        }

        self.config["ImportantLocations"] = {
            JAVIER_HOME_CONFIG: "(54, 14)",
            ANDREINA_HOME_CONFIG: "(52, 13)",
            THE_DARKNESS_CLUB_CONFIG: "(50, 14)",
            LA_PASION_BAR_CONFIG: "(54, 11)",
            MI_ROLITA_BREWERY_CONFIG: "(50, 12)",
        }

        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)
