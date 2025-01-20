

class appCrudParent():
    def __init__(self,  P) -> None:
        from ins_kit._apps.app_crud.app_crud import APPCRUD, AppCrudOps
        from ins_kit.ins import InsKit
        self.app: APPCRUD = P
        self.ins: InsKit = P.ins
        self.ops: AppCrudOps = P.ops
        self.get = self.ins._server._get()

