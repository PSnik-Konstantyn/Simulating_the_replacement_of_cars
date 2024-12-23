from app.model.Calculations import simulate_changing

years = 9
initial_dvz_share = 0.82
initial_ev_share = 0.18

fuel_price = 1.9
electricity_price = 0.75
dvz_maintenance_factor = 1.0
ev_maintenance_factor = 0.8
dvz_range = 600
ev_range = 300
charging_speed = 50
refueling_speed = 300
ev_subsidy = 5
dvz_subsidy = 1

fuel_price_trend = -9
electricity_price_trend = -0.03
dvz_maintenance_factor_trend = 0.02
ev_maintenance_factor_trend = -0.01
dvz_range_trend = 0.01
ev_range_trend = 0.02
charging_speed_trend = -0.02
refueling_speed_trend = 0.01
ev_subsidy_trend = 5
dvz_subsidy_trend = 1

simulate_changing(initial_dvz_share=initial_dvz_share,
                  initial_ev_share=initial_ev_share,
                  years=years,
                  fuel_price=fuel_price,
                  electricity_price=electricity_price,
                  dvz_maintenance_factor=dvz_maintenance_factor,
                  ev_maintenance_factor=ev_maintenance_factor,
                  dvz_range=dvz_range,
                  ev_range=ev_range,
                  charging_speed=charging_speed,
                  refueling_speed=refueling_speed,
                  ev_subsidy=ev_subsidy,
                  dvz_subsidy=dvz_subsidy,
                  fuel_price_trend=fuel_price_trend,
                  electricity_price_trend=electricity_price_trend,
                  dvz_maintenance_factor_trend=dvz_maintenance_factor_trend,
                  ev_maintenance_factor_trend=ev_maintenance_factor_trend,
                  dvz_range_trend=dvz_range_trend,
                  ev_range_trend=ev_range_trend,
                  charging_speed_trend=charging_speed_trend,
                  refueling_speed_trend=refueling_speed_trend,
                  ev_subsidy_trend = ev_subsidy_trend ,
                  dvz_subsidy_trend= dvz_subsidy_trend )
