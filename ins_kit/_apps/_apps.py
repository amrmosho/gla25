from ins_kit.ins_parent import ins_parent
from ins_kit._apps.app_crud.app_crud import APPCRUD, AppCrudOps


class Apps(ins_parent):

    @property
    def _crud_ops(self) -> AppCrudOps:
        ops: AppCrudOps = AppCrudOps()
        return ops

    def _crud(self, ops: AppCrudOps = None , properties: dict ={}):
        
        if ops == None:
            ops = AppCrudOps()
        ap = APPCRUD(self.ins, ops ,properties)
        return ap.render()
