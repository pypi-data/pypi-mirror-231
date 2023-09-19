import math

from numpy import nan

from rtctools_heat_network.pycml import Variable

from ._internal.heat_component import BaseAsset
from .heat_two_port import HeatTwoPort


class Buffer(HeatTwoPort, BaseAsset):
    def __init__(self, name, **modifiers):
        super().__init__(name, **modifiers)

        self.component_type = "buffer"

        self.Q_nominal = 1.0
        self.T_supply = nan
        self.T_return = nan
        self.T_supply_id = -1
        self.T_return_id = -1
        self.dT = self.T_supply - self.T_return
        self.cp = 4200.0
        self.rho = 988.0
        self.Heat_nominal = self.cp * self.rho * self.dT * self.Q_nominal

        self.heat_transfer_coeff = 1.0
        self.height = 5.0
        self.radius = 10.0
        self.volume = math.pi * self.radius**2 * self.height
        self.heat_loss_coeff = 2 * self.heat_transfer_coeff / (self.radius * self.rho * self.cp)
        # The hot/cold tank can have a lower bound on its volume.
        # Meaning that they might always be, for e.g., 5% full.
        self.min_fraction_tank_volume = 0.05

        # Initial values
        self.init_V_hot_tank = nan
        self.init_Heat = nan

        # Minimum/maximum values
        self.min_stored_heat = (
            self.volume * self.min_fraction_tank_volume * self.dT * self.cp * self.rho
        )
        self.max_stored_heat = (
            self.volume * (1 - self.min_fraction_tank_volume) * self.dT * self.cp * self.rho
        )

        # Stored_heat is the heat that is contained in the buffer.
        # Heat_buffer is the amount of heat added to or extracted from the buffer
        # per timestep.
        # HeatHot (resp. HeatCold) is the amount of heat added or extracted from
        # the hot (resp. cold) line.
        # As by construction the cold line should have zero heat, we fix HeatCold to zero.
        # Thus Heat_buffer = HeatHot = der(Stored_heat).
        self.add_variable(Variable, "Heat_buffer", nominal=self.Heat_nominal)
        # Assume the storage fills in about an hour at typical rate
        self._typical_fill_time = 3600.0
        self._nominal_stored_heat = self.Heat_nominal * self._typical_fill_time
        self.add_variable(
            Variable,
            "Stored_heat",
            min=self.min_stored_heat,
            max=self.max_stored_heat,
            nominal=self._nominal_stored_heat,
        )
        # For nicer constraint coefficient scaling, we shift a bit more error into
        # the state vector entry of `Heat_loss`. In other words, with a factor of
        # 10.0, we aim for a state vector entry of ~0.1 (instead of 1.0)
        self._heat_loss_error_to_state_factor = 10.0
        self._nominal_heat_loss = (
            self._nominal_stored_heat * self.heat_loss_coeff * self._heat_loss_error_to_state_factor
        )
        self.add_variable(Variable, "Heat_loss", min=0.0, nominal=self._nominal_heat_loss)
        self.add_variable(Variable, "Heat_flow", nominal=self.Heat_nominal)

        self._heat_loss_eq_nominal_buf = (self.Heat_nominal * self._nominal_heat_loss) ** 0.5

        self.add_equation(self.HeatIn.Q - self.HeatOut.Q)

        # Heat stored in the buffer
        self.add_equation(
            (self.der(self.Stored_heat) - self.Heat_buffer + self.Heat_loss)
            / self._heat_loss_eq_nominal_buf
        )
        self.add_equation(
            (self.Heat_loss - self.Stored_heat * self.heat_loss_coeff) / self._nominal_heat_loss
        )
        self.add_equation(
            (self.Heat_buffer - (self.HeatIn.Heat - self.HeatOut.Heat)) / self.Heat_nominal
        )
        self.add_equation((self.Heat_flow - self.Heat_buffer) / self.Heat_nominal)
