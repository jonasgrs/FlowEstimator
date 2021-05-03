from FlowEstimator import FlowEstimator as flowest

# --- Inputs Construction ---
dT_set_construction = 20  # Kelvin
max_demand_construction = 10000  # Watt
dp_set_construction = 60  # Pascal/Meter

# .--- Inputs Use Phase ---
dT_set_use = 4  # Kelvin
max_demand_use = 5000  # Watt
dp_set_use = dp_set_construction  # Pascal/Meter


# --- Constants ---


def main():

    # size network
    dn = flowest.get_fixed_diameter(
        dT_set=dT_set_construction,
        max_demand=max_demand_construction,
        dp_set=dp_set_construction)

    max_allowed_velocity = flowest.get_max_allowed_flow_velocity(dn=dn)

    # before retrofit:
    pre_retrofit_velocity = flowest.get_flow_velocity(
        diameter=dn,
        max_demand=max_demand_construction,
        dT=dT_set_construction
    )

    # after retrofit:
    post_retrofit_velocity = flowest.get_flow_velocity(
        diameter=dn,
        max_demand=max_demand_use,
        dT=dT_set_use
    )

    print(f'velocity before retofit = {pre_retrofit_velocity:.2f} m/s \n'
          f'velocity after retrofit = {post_retrofit_velocity:.2f} m/s \n'
          f'max allowed velocity = {max_allowed_velocity} m/s')


if __name__ == '__main__':
    main()
