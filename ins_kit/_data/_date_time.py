from ins_kit.ins_parent import ins_parent
from datetime import datetime, timezone, timedelta
#import pytz # type: ignore



class DateTime(ins_parent):
    def __init__(self, Ins) -> None:
        super().__init__(Ins)

        """_summary_

        %a	Weekday, short version	Wed	
        %A	Weekday, full version	Wednesday	
        %w	Weekday as a number 0-6, 0 is Sunday	3	
        %d	Day of month 01-31	31	
        %b	Month name, short version	Dec	
        %B	Month name, full version	December	
        %m	Month as a number 01-12	12	
        %y	Year, short version, without century	18	
        %Y	Year, full version	2018	
        %H	Hour 00-23	17	
        %I	Hour 00-12	05	
        %p	AM/PM	PM	
        %M	Minute 00-59	41	
        %S	Second 00-59	08	
        %f	Microsecond 000000-999999	548513	
        %z	UTC offset	+0100	
        %Z	Timezone	CST	
        %j	Day number of year 001-366	365	
        %U	Week number of year, Sunday as the first day of week, 00-53	52	
        %W	Week number of year, Monday as the first day of week, 00-53	52	
        %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
        %C	Century	20	
        %x	Local version of date	12/31/18	
        %X	Local version of time	17:41:00	
        %%	A % character	%	
        %G	ISO 8601 year	2018	
        %u	ISO 8601 weekday (1-7)	1	
        %V	ISO 8601 weeknumber (01-53)	01


        Returns:
            _type_: _description_
        """

    def __tz(self):
        return timezone.utc

    def __localtz(self):
        return pytz.timezone("Africa/Cairo")


    def src(self, date="now"):

        if type(date) == dict:
            if "hour" not in date:
                date["hour"] = 0
            if "minute" not in date:
                date["minute"] = 0
            if "second" not in date:
                date["second"] = 0
            x = datetime(int(date["year"]), int(date["month"]), int(date["day"]), hour=int(
                date["hour"]), minute=int(date["minute"]), second=int(date["second"]), tzinfo=self.__tz()

            )
        elif date == "now":
            x = datetime.now(self.__tz())
        return x

    __local = False
    __ui_format = False

    def _local(self):
        self.__local = True
        return self
    def _ui(self):
        self.__ui_format = True
        return self
    
    def _to_local(self,date:datetime):
        date = date.astimezone(self.__localtz())
        return date
    
    def _get_format(self,format=""):
        if format == "":
            if self.__ui_format:
                format = self.ins._map.UI_DATETIME_FORMAT
            else :
                format = self.ins._map.DB_DATETIME_FORMAT
      
        if format == "date":
            if self.__ui_format:
                format = self.ins._map.UI_DATE_FORMAT
            else :
                format = self.ins._map.DB_DATE_FORMAT
                
        if format == "time":
            
            if self.__ui_format:
                format = self.ins._map.UI_TIME_FORMAT
            else :
                format = self.ins._map.DB_TIME_FORMAT
                
        return format
                

    def _format(self, date, format=""):
        if type(date) ==str:
            date = self._str_to_date(date)
        
        if format == "src":
            return date
        format =self._get_format(format)
        if self.__local:
            date = self._to_local(date)
        self.__local = False

        return date.strftime(format)

    def _date_time(self, format="", date="now"):
        return self._format(self.src(date), format)

    def _date(self, format="", date="now"):
        if format == "":
            format = self.ins._map.DB_DATE_FORMAT
        if self.__local:
            format = self.ins._map.UI_DATE_FORMAT
        return self._format(self.src(date), format)

    def _now(self, format=""):
        x = self.src("now")
        return self._format(x, format)

    def _plus(self, date="now",  format="", days=0, weeks=0, hours=0, minutes=0):
        end_date = self.src(date) + timedelta(days=days,
                                              weeks=weeks, hours=hours, minutes=minutes)
        return self._format(end_date, format)

    def _minus(self, date="now",  format="", days=0, weeks=0, hours=0, minutes=0):

        end_date = self.src(date) - timedelta(days=days,
                                              weeks=weeks, hours=hours, minutes=minutes)
        return self._format(end_date, format)

    def _date_range(self, from_date, to_date, format):
        r = []
        from_date = self.src(from_date)
        to_date = self.src(to_date)
        for n in range(int((from_date - to_date).days)+1):
            d = from_date + timedelta(n)
            r.append(self._format(d, format))
        return r

    def _is_aftre(self, check_date, date):
        check_date = self.src(check_date)
        date = self.src(date)
        return (check_date > date)

    def _is_befor(self, check_date, date):
        check_date = self.src(check_date)
        date = self.src(date)
        return (check_date < date)

    def _is_equal(self, check_date, date):
        check_date = self.src(check_date)
        date = self.src(date)
        return (check_date == date)

    def _is_between(self, check_date, start_date, end_date):
        check_date = self.src(check_date)
        start_date = self.src(start_date)
        end_date = self.src(end_date)
        return (check_date >= start_date and check_date <= end_date)
    def _str_to_date(self,date_string:str):
        """
        Attempts to convert a string to a datetime object without a specified format,
        trying several common formats.

        Args:
            date_string: The string to convert.

        Returns:
            A datetime object, or None if conversion fails.
        """
        formats = [
            "%Y-%m-%d",        # YYYY-MM-DD
            "%m/%d/%Y",        # MM/DD/YYYY
            "%d/%m/%Y",        # DD/MM/YYYY
            "%Y/%m/%d",        # YYYY/MM/DD
            "%m-%d-%Y",        # MM-DD-YYYY
            "%d-%m-%Y",        # DD-MM-YYYY
            "%Y%m%d",          # YYYYMMDD
            "%b %d, %Y",       # e.g., Nov 28, 2023
            "%B %d, %Y",       # e.g., November 28, 2023
            "%d %b %Y",       # 28 Nov 2023
            "%d %B %Y",       # 28 November 2023

            "%Y-%m-%d %H:%M:%S",  # YYYY-MM-DD HH:MM:SS
            "%m/%d/%Y %H:%M:%S",  # MM/DD/YYYY HH:MM:SS
            "%d/%m/%Y %H:%M:%S",  # DD/MM/YYYY HH:MM:SS
            "%Y/%m/%d %H:%M:%S",  # YYYY/MM/DD HH:MM:SS
            "%m-%d-%Y %H:%M:%S",  # MM-DD-YYYY HH:MM:SS
            "%d-%m-%Y %H:%M:%S",  # DD-MM-YYYY HH:MM:SS

            "%Y-%m-%d %H:%M",     # YYYY-MM-DD HH:MM
            "%m/%d/%Y %H:%M",     # MM/DD/YYYY HH:MM
            "%d/%m/%Y %H:%M",     # DD/MM/YYYY HH:MM
            "%Y/%m/%d %H:%M",     # YYYY/MM/DD HH:MM
            "%m-%d-%Y %H:%M",     # MM-DD-YYYY HH:MM
            "%d-%m-%Y %H:%M",     # DD-MM-YYYY HH:MM

            "%Y-%m-%dT%H:%M:%S", # ISO 8601 format (YYYY-MM-DDTHH:MM:SS) - often used in APIs
            "%Y-%m-%dT%H:%M",    # ISO 8601 format (YYYY-MM-DDTHH:MM)
        ]

        date_string=date_string.strip()
        for fmt in formats:
            try:
                return datetime.strptime(date_string, fmt)
            except ValueError:
                continue  # Try the next format

        return None  # No format matched