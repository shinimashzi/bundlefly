from decimal import Decimal

config_00 = {  "topology":"bundlefly",
            "router" : "iq",
            "credit_delay": 2,
            "routing_delay": 2,
            "vc_alloc_delay": 1,
            "sw_alloc_delay": 1,
            "st_final_delay": 1,
            "input_speedup": 1,
            "output_speedup": 1,
            "internal_speedup": 2.0,
            "routing_function": "min",
            "num_vcs":6,
            "vc_buf_size":256,
            "wait_for_tail_credit":0,
            "injection_rate":0.01,
            "traffic": "uniform",
            "warmup_periods":3,
            "sim_count":1,
            "packet_size":1,
            "sample_period ":1000,
            "sim_type": "latency",
            "network_file": "bundlefly_config/bundlefly_file_00",
            "print_csv_results": 1,
          }

config_01 = {  "topology":"bundlefly",
            "router" : "iq",
            "credit_delay": 2,
            "routing_delay": 2,
            "vc_alloc_delay": 1,
            "sw_alloc_delay": 1,
            "st_final_delay": 1,
            "input_speedup": 1,
            "output_speedup": 1,
            "internal_speedup": 2.0,
            "routing_function": "min",
            "num_vcs":6,
            "vc_buf_size":256,
            "wait_for_tail_credit":0,
            "injection_rate":0.01,
            "traffic": "uniform",
            "warmup_periods":3,
            "sim_count":1,
            "packet_size":1,
            "sample_period ":1000,
            "sim_type": "latency",
            "network_file": "bundlefly_config/bundlefly_file_01",
            "print_csv_results": 1,}

if __name__ == "__main__":
    for i in range(1, 66):
        injection_rate = float(i/100)
        injection_rate = ("%.2f" % injection_rate)
        print(str(injection_rate))
        config_00["injection_rate"] = injection_rate
        file_config = str(injection_rate)
        with open("bundlefly_config/bundlefly_00/"+file_config, "w", encoding="utf-8") as f:
            for key in config_00:
                f.write(key + " = " + str(config_00[key]) + "; \n" )

    for i in range(1, 66):
        injection_rate = float(i/100)
        injection_rate = ("%.2f" % injection_rate)
        print(str(injection_rate))
        config_01["injection_rate"] = injection_rate
        file_config = str(injection_rate)
        with open("bundlefly_config/bundlefly_01/"+file_config, "w", encoding="utf-8") as f:
            for key in config_01:
                f.write(key + " = " + str(config_01[key]) + "; \n" )

