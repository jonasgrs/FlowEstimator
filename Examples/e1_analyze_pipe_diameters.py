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

    error_before = (1 - d_opt / dn) * 100

    print(f'Error between sized and optimal diameter during construction '
          f'phase was {error_before:.2f} %')

    # after retrofit:
    dn_rf = flowest.get_fixed_diameter(
        dT_set=dT_set_use,
        max_demand=max_demand_use,
        dp_set=dp_set_construction)

    d_opt_rf = flowest.get_optimal_diameter(
        dT_set=dT_set_use,
        max_demand=max_demand_use,
        dp_set=dp_set_construction)

    error_after = (1 - d_opt_rf / dn) * 100

    remaining_error = (1 - dn_rf / dn) * 100

    error_after_new_pipes = (1 - d_opt_rf / dn_rf) * 100

    print(f'Error between originally sized pipes and optimal theoretical '
          f'diameter after building retrofit is {error_after:.2f} %')

    print(f'Error between originally sized pipes and newly sized pipes after '
          f'building retrofit is {remaining_error:.2f} %')

    print(f'Still, even with a newly dimensioned pipe system, the remaining '
          f'error to the optimal theoretical diameter after building retrofit'
          f'would still be {error_after_new_pipes:.2f} %')


if __name__ == '__main__':
    main()
