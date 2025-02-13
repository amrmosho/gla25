from ins_kit._options._map import Map, This
from ins_kit._data._db import Database 
from ins_kit._data._data import Data 
from ins_kit._data._data_collect import DataCollect 

from ins_kit._data._langs import Languages 
from ins_kit._data._date_time import DateTime 

from ins_kit._engine._bp import Temp,Ajax
from ins_kit._engine._engine import Engine
from ins_kit._engine._console import Console

from ins_kit._files._json import JSON
from ins_kit._ui.ui import Ui
from ins_kit._files._files import Files
from ins_kit._server ._server import Server
from ins_kit._apps._apps import Apps

from ins_kit._users.users import Users

class InsKit():
    def __init__(self) -> None:
        self._map = Map(self)
        self._this = This(self)
        self._tmp = Temp(self)
        self._json = JSON(self)
        self._eng = Engine (self)
        self._server = Server (self)
        self._ui = Ui (self)
        self._files = Files (self)
        self._db = Database (self)
        self._data = Data (self)
        self._data_collect = DataCollect (self)
        
        self._langs = Languages(self)
        self._ajax = Ajax(self)
        self._apps = Apps (self)
        self._date = DateTime (self)
        self._users = Users (self)
        self._console = Console (self)

    def test(self):
        return f"this is {__name__}"


ins = InsKit()

