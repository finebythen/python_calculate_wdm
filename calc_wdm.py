# --> CALCULATE ANY WDM PORT

# Examples:
# Ports per WDM: 64
# Testports: 38, 65, 154


def CalculateWDM(port, wdm):
    x = (port // wdm) + 1
    y = port % wdm

    return x, y


a, b = CalculateWDM(38, 64)
c, d = CalculateWDM(65, 64)
e, f = CalculateWDM(154, 64)
