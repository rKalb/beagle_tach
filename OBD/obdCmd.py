class obdCmd:
    def __init__(self,
            short_name,
            pid = '0x00',
            mode = '',
            long_name = '',
            bytes_returned = 0,
            description = "",
            minValue = 0.0,
            maxValue = 0.0,
            units = '',
            formula = ''):

        #ShortName, PID, Long_Name, Bytes Returned, Description, minValue
        #maxValue, units, formula


        self.short_name = short_name
        self.pid = pid
        self.mode = mode
        self.long_name = long_name
        self.bytes_returned = bytes_returned
        self.description = description
        self.minValue = minValue
        self.maxValue = maxValue
        self.units = units
        self.formula = formula

        return None


