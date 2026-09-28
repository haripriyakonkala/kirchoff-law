def check_kcl(currents_entering, currents_leaving):
    """
    Verify Kirchhoff's Current Law.
    """
    total_entering = sum(currents_entering)
    total_leaving = sum(currents_leaving)

    return total_entering, total_leaving, \
        abs(total_entering - total_leaving) < 1e-9


def check_kvl(voltage_sources, voltage_drops):
    """
    Verify Kirchhoff's Voltage Law.
    """
    total_source = sum(voltage_sources)
    total_drop = sum(voltage_drops)

    return total_source, total_drop, \
        abs(total_source - total_drop) < 1e-9


if __name__ == "__main__":

    # KCL Example
    entering = [5, 3]
    leaving = [6, 2]

    total_in, total_out, kcl_valid = check_kcl(
        entering, leaving
    )

    print("KCL Verification")
    print("-----------------")
    print("Current Entering :", total_in, "A")
    print("Current Leaving  :", total_out, "A")
    print("KCL Satisfied    :", kcl_valid)

    # KVL Example
    sources = [12]
    drops = [5, 7]

    total_source, total_drop, kvl_valid = check_kvl(
        sources, drops
    )

    print("\nKVL Verification")
    print("-----------------")
    print("Voltage Sources :", total_source, "V")
    print("Voltage Drops   :", total_drop, "V")
    print("KVL Satisfied   :", kvl_valid)