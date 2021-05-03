from FlowEstimator import FlowEstimator as flowest


# --- Inputs Construction ---
dT_set_construction = 20          # Kelvin
max_demand_construction = 28124  # Watt
dp_set_construction = 60         # Pascal/Meter

# .--- Inputs Use Phase ---
dT_set_use = 4          # Kelvin
max_demand_use = 3443  # Watt
dp_set_use = dp_set_construction # Pascal/Meter

# --- Constants ---


def main():

    # before retrofit:
    dn = flowest.get_fixed_diameter(
        dT_set=dT_set_construction,
        max_demand=max_demand_construction,
        dp_set=dp_set_construction)

    d_opt = flowest.get_optimal_diameter(
        dT_set=dT_set_construction,
        max_demand=max_demand_construction,
        dp_set=dp_set_construction)

    error_before = (1 - dn / d_opt) * 100

    # after retrofit:
    d_opt_rf = flowest.get_optimal_diameter(
        dT_set=dT_set_use,
        max_demand=max_demand_use,
        dp_set=dp_set_construction)

    error_after = (1 - dn / d_opt_rf) * 100


if __name__ == '__main()__':
    main()
