from datetime import datetime

class Task():
    def __init__(self, iid, title, desc, created_at = datetime.now().strftime("%d/%m/%Y %H:%M"), status="Pendente"):
        self.iid = iid
        self.title = title
        self.desc = desc
        self.created_at = created_at
        self.status = status

    def to_dict(self):
        """Converte o objeto para dicionário para salvar no JSON
        """
        return {
            "ID": self.iid,
            "Title": self.title,
            "Desc": self.desc,
            "Created at": self.created_at,
            "Status": self.status
        }

        

    
